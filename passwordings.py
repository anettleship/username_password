def user_input(message, hide):
    """
    Requests input from the user with the 'message' parameter (string). Hides the input on screen if 'hide' (optional, boolean)
    is true. Returns the text the user inputs.
    """
    inputstr = input(message)
    return inputstr

def get_user_credentials(namespace):
    """
    Handles saving username and password to the system keychain and retrieving them, using a namespace for the specific
    application to test if username and password are already stored. A single username and password pair is supported for each
    namespace. To use in your script, make up a namespace for your script that won't be in use already.
    """
    
