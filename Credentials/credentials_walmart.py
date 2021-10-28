from decouple import config

user_id = config('user_id', default = '')
user_secret = config('user_secret', default = '')
