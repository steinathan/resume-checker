import { createClient } from "@supabase/supabase-js";

const SUPABASE_KEY = import.meta.env.VITE_APP_SUPABASE_KEY;
const SUPABASE_URL = import.meta.env.VITE_APP_SUPABASE_URL;

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

export default supabase;
