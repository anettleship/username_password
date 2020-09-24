import keyring
from getpass import getpass

def get_user_credentials_recurse(namespace):

    username, password = get_user_credentials(namespace)

    if password != False and username != False:
        print("Username retrieved: {}".format(username))
        print("Password retrieved.")
    else:
        print(
            'Now forcing get_user_credentials to re-request input from user, for when username and password are rejected...')

        # Force function to re-request credentials from user.
        username, password = get_user_credentials('test_namespace', force=True)

        if password != False and username != False:
            print("Username retrieved: {}".format(username))
            print("Password retrieved: {}".format(password))

    return username, password

def get_user_credentials(service_id, force = None):
    """
    Handles saving username and password to the system keychain and retrieving them, using a namespace 'service_id' for the specific
    application to test if username and password are already stored. A single username and password pair is supported for each
    namespace. To use in your script, make up a namespace for your script that won't be in use already.
    """

    # From https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options
    MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

    # Try to get a username and password from keychain for this namespace.
    try:
        username = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
        password_retrieved = keyring.get_password(service_id, username)
        if password_retrieved == None or username == None:
            raise Exception('No Username or Password Stored for service_id: {}'.format(service_id))
        # Check optional parameter to force the function to re-request input from user.
        if force == True:
            raise Exception('Function was forced to re-request input from user by parameter force = True. for service_id: {}'.format(service_id))
        #print(username)
        #print(password_retrieved)

        return (username, password_retrieved)
    # If this fails, get input from user and save to keychain for next time.
    except:
        print('Requesting from user...\n')
        # Get Username in the clear, then password hidden as the user types.
        username = input('Input Username: ')
        print('Username Entered: '+username)
        password = getpass()

        # save password
        keyring.set_password(service_id, username, password)

        # optionally, abuse `set_password` to save username onto keyring
        # we're just using some known magic string in the username field
        keyring.set_password(service_id, MAGIC_USERNAME_KEY, username)

        return (username, password)
