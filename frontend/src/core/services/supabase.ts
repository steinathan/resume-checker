import {createClient} from '@supabase/supabase-js'


const SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJic2Nja2pqYnpuZWxsbXB6ZW1mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDM0NDQ4NTUsImV4cCI6MjAxOTAyMDg1NX0.RYRCyrCs4xf8R1U820x6dVtbRVqAKPddDSv2n--T4Eg"
const SUPABASE_URL = "https://rbscckjjbznellmpzemf.supabase.co"

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)

export default supabase