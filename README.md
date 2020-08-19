# username_password
simple python functions to save username and password to users keychain, using keyring module, applying code from this stack overflow thread:

https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options

Handles saving username and password to the system keychain and retrieving them, using a namespace 'service_id' for the specific application to test if username and password are already stored. A single username and password pair is supported for each namespace. To use in your script, make up a namespace for your script that won't be in use already.

This project was created using a pipenv virtual environment. With pipenv installed, clone this repository and run 'pipenv install' to install the correct version of all dependencies (though really this project is pretty simple and shouldn't rely on anything more than Python 3). Here's an excellent guide to pipenv: https://realpython.com/pipenv-guide/

Usage example:

Place passwordings.py along side your script. test_password_namespace is my example namespace for this script. the function get_user_credentials will try to get a username and password from the keychain and prompt the user to input these if they are not present, saving the result to the keychain under the specified service_id namespace.

Run this once and the user will be prompted to enter username and password. On the second run, these will be retrieved from keychin and printed to the screen.

----


import passwordings

username, password = passwordings.get_user_credentials('test_password_namespace')

if password != False and username != False:
    print("Username retrieved: {}".format(username))
    print("Password retrieved: {}".format(password))
