class UserLoginInfo:

    def __init__(self,Username,Password):
        self.Username = Username
        self.old_password = [Password]

    # Create method to check password validation

    def is_valid(self,pwd):
        # Length of password should be greater than 7
        if len(pwd) < 8 :
            return False
        # First letter should be in uppercase
        if pwd[0].istitle() != True:
            return False
        # Password should contain only (alphabets or numerics or both)
        if pwd.isalnum() != True:
            return False
        else:
            return True
