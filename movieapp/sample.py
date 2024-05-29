import os

virtual_env = os.getenv('VIRTUAL_ENV')
if virtual_env:
    print("Current virtual environment:", virtual_env)
else:
    print("No virtual environment active.")
