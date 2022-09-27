from security.users import *
from security.sessions import *


class Auth():

    def authenticate_user(login: str, password: str):
        return Users.login(login, password)

    def desauthenticate_user(user):
        Users.logout(user)

    def validate_token(token: str):
        return Session.validate_token(token)
        

Users.create_user('gabriel', '123')

#userobj = Auth.authenticate_user('gabriel', '123')
#userobj.block_user()
#userobj.logout()
#userobj.unblock_user()
#
#userobj2 = Auth.authenticate_user('gabriel', '123')
#print('')

