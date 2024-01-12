import os

import stripe
from fastapi import APIRouter, Header, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.handlers.user_handler import find_user_by_id, update_user

router = APIRouter(
    tags=["stripe"],
)


class CheckoutPayload(BaseModel):
    email_address: str
    user_id: str
    plan_name: str


@router.post("/stripe/get-checkout-url")
async def get_stripe_session(payload: CheckoutPayload):
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
    frontend_base = os.getenv("FRONTEND_BASE_URL")

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1OX7VcBSae2LEN6syD6W7sV7',
            'quantity': 1,
        }],
        mode='subscription',
        success_url=f'{frontend_base}/stripe?status=success',
        cancel_url=f'{frontend_base}/dashboard',
        metadata={
            'user_id': payload.user_id,
            'email_address': payload.email_address,
            'plan_name': payload.plan_name,
        },
    )

    return JSONResponse(content={'id': session.id})


@router.post("/stripe/webhook")
async def webhook_received(request: Request, stripe_signature: str = Header(None)):
    webhook_secret = os.environ["STRIPE_WEBHOOK_SECRET"]
    data = await request.body()
    try:
        event = stripe.Webhook.construct_event(
            payload=data,
            sig_header=stripe_signature,
            secret=webhook_secret
        )
        event_data = event['data']
    except Exception as e:
        return {"error": str(e)}

    event_type = event['type']

    if event_type == 'checkout.session.completed':
        print('checkout session completed')
        session = event_data['object']
        meta = session.get('metadata', {})

        user_id = meta.get('user_id')
        email_address = meta.get('email_address')
        plan_name = meta.get('plan_name')

        subscription_id = session.get('subscription')
        subscription = stripe.Subscription.retrieve(subscription_id)

        print("got meta info:", user_id, email_address, plan_name)
        user = find_user_by_id(user_id)
        if user:
            user.stripe_customer_id = session.get('customer')
            user.stripe_subscription_id = subscription_id
            user.stripe_subscription_status = subscription.status
            user.stripe_subscription_current_period_start = subscription.current_period_start
            user.stripe_subscription_current_period_end = subscription.current_period_end
            user.stripe_subscription_cancel_at_period_end = subscription.cancel_at_period_end

            # ~!
            update_user(user)

    elif event_type == 'invoice.paid':
        print('invoice paid')
    elif event_type == 'invoice.payment_failed':
        print('invoice payment failed')
    else:
        print(f'unhandled event: {event_type}')

    return {"status": "success"}
