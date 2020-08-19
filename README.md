# username_password
simple python functions to save username and password to users keychain, using keyring module.

Handles saving username and password to the system keychain and retrieving them, using a namespace 'service_id' for the specific application to test if username and password are already stored. A single username and password pair is supported for each namespace. To use in your script, make up a namespace for your script that won't be in use already.

Usage example: 

Place passwordings.py along side your script. test_password_namespace is my example namespace for this script. the function get_user_credentials will try to get a username and password from the keychain and prompt the user to input these if they are not present, saving the result to the keychain under the specified service_id namespace.


----


import passwordings

username, password = passwordings.get_user_credentials('test_password_namespace')

if password != False and username != False:
    print("Username retrieved: {}".format(username))
    print("Password retrieved: {}".format(password))
