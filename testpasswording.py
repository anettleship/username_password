import passwordings
from getpass import getpass


def main():
    # Get Username
    username = input('Username:')
    print(username)
    password = getpass()
    print(password)



if __name__ == '__main__':
    main()
