#!/usr/bin/python3
# -*- conding: utf-8 -*-

#from django.contrib.sessions.backends.db import SessionStore as DBStore
#from django.contrib.sessions.base_session import AbstractBaseSession
#from django.db import models

class DBStore:

    def __init__(self): pass

    def create_model_instance(self, data):
        return TestClass(data)
        
class TestClass:
    def __init__(self, data):
        self.data = data

#class CustomSession(AbstractBaseSession):
class CustomSession:
    """
    A session model with a column for an account ID.
    """

    #account_id = models.IntegerField(null=True, db_index=True)
    account_id = None

    @classmethod
    def get_session_store_class(cls):
        return SessionStore


class SessionStore(DBStore):
    """
    A database session store, that handles updating the account ID column
    inside the custom session model.
    """

    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        print(obj) #

        try:
            print(data)#
            account_id = int(data.get("_auth_user_id"))
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id

        return obj

    def get_session_cookie_age(self):
        return 60 * 60 * 24  # One day.


def main():
    print('Test comment > Class docstring print test')
    print(f'CustomSession.__doc__ :: \n{CustomSession.__doc__}')
    print(f'SessionStore.__doc__ :: \n{SessionStore.__doc__}')
    
    print('Test comment > SEssionStore.get_model_class().get_session_store_class()')
    print(SessionStore.get_model_class().get_session_store_class())

    data = {"_auth_user_id": "sample_data"}
    ss = SessionStore()
    ss.create_model_instance(data)


if __name__ == '__main__':
    main()
