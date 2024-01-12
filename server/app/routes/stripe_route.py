import os

import stripe
from fastapi import APIRouter, Header, Request
from starlette.responses import JSONResponse

router = APIRouter(
    tags=["stripe"],
)


@router.post("/stripe/get-checkout-url")
async def get_stripe_session():
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
    frontend_base = os.getenv("FRONTEND_BASE_URL")

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1OX7VcBSae2LEN6syD6W7sV7',
            'quantity': 1,
        }],
        mode='subscription',
        success_url=f'{frontend_base}/stripe',
        cancel_url=f'{frontend_base}/stripe?cancel=true',
        metadata={
            'userId': "dummy-user-id",
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
        user_id = session.get('metadata', {}).get('userId')
        print("user_id", user_id)

    elif event_type == 'invoice.paid':
        print('invoice paid')
    elif event_type == 'invoice.payment_failed':
        print('invoice payment failed')
    else:
        print(f'unhandled event: {event_type}')

    return {"status": "success"}
