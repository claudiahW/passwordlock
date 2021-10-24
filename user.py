class User:
    """
    Creates new user instances.
    """
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
        """
        __init__ defines the properties of self.
        Args:
        firstname: User's first name
        lastname: User's last name
        username: New username
        password: New password
        """
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
        """
        save_user saves objects to the userslist.
        """
        User.userslist.append(self)
    def delete_user(self):
        """
        delete_user deletes a saved user from the userslist.
        """
        User.userslist.remove(self)
    @classmethod
    def display_users(cls):
        """
        display_user returns the userlist.
        """
        return cls.userslist
    @classmethod
    def find_by_number(cls,number):
        """
        Takes in username and returns a user that matches the phone number.
        Args:
        number: Phone number Returns: Contact of person that matches the number.
        """
        for user in cls.userslist:
            if user.password == number:
                return user
    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username == number:
                return True
                return False