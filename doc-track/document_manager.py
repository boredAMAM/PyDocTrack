import os
from dotenv import load_dotenv
load_dotenv()

class MyClass:
    def __init__(self):
        self.my_var = os.getenv('MY_ENV_VARIABLE', 'default_value')
    
    def show_env_var(self):
        print(f'The value of MY_ENV_VARIABLE is: {self.my_var}')

obj = MyClass()
obj.show_env_var()