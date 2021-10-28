from decouple import config

user_name = config('user_name', default = '')
user_password = config('user_password', default = '')