'''

    @Author:pooja
    @Date:04-09-2024
    @last modified by:pooja
    @last modified time:04-09-2024
    @title:program to acces env variable

'''




import os

# Get a specific environment variable
env_var_name = input("Enter the environment variable name: ")
env_var_value = os.getenv(env_var_name)

# Print the value of the environment variable
if env_var_value is not None:
    print(f"{env_var_name} = {env_var_value}")
else:
    print(f"{env_var_name} is not set.")

# Print all environment variables (optional)
# print(os.environ)
