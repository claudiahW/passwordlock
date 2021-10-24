from random import *
from user import User
from user import Details
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser