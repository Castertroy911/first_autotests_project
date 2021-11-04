from decouple import config

user_id_amazon = config('user_id_amazon', default='')
user_secret_amazon = config('user_secret_amazon', default='')
two_step_auth = config('two_step_auth', default='')