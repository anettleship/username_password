import passwordings
import keyring
from getpass import getpass


def main():
    # Get Username in the clear, then password hidden as the user types.
    username = input('Username:')
    print(username)
    password = getpass()

    # From https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options
    MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

    # the service is just a namespace for your app
    service_id = 'PASSWORDINGS_NAMESPACE'

    # save password
    keyring.set_password(service_id, username, password)

    # optionally, abuse `set_password` to save username onto keyring
    # we're just using some known magic string in the username field
    keyring.set_password(service_id, MAGIC_USERNAME_KEY, username)

    username_retrieved = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
    password_retrieved = keyring.get_password(service_id, username)
    print(username_retrieved)
    print(password_retrieved)



if __name__ == '__main__':
    main()
