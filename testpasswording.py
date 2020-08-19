import passwordings

def main():

    username, password = passwordings.get_user_credentials('test_namespace')

    if password != False and username != False:
        print("Username retrieved: {}".format(username))
        print("Password retrieved: {}".format(password))

if __name__ == '__main__':
    main()
