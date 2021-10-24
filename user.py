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
