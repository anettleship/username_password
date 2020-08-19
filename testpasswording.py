import passwordings



def main():

    password = passwordings.get_user_credentials('adrian_test_password_namespace')

    if password != False:
        print("password retrieved: {}".format(password))



if __name__ == '__main__':
    main()
