#!/usr/bin/python3
# -*- coding: utf-8 -*-
from uuid import uuid1

from pattern import Singleton


class Session:
    def __init__(self, user_id, login_uid, page_stack):
        self.user_id = user_id
        self.login_uid = login_uid
        self.page_stack = page_stack


class SessionManager(Singleton):

    def __init__(self):
        self.__session_id = None
        self.__session = None
        self.__createSessionId()

    def getSessionId(self):
        return self.__session_id

    def getSession(self):
        return self.__session

    def setSession(self, session):
        self.__session = session

    def __createSessionId(self):
        self.__session_id = uuid1()


def main():
    session_manager1 = SessionManager.getInstance()
    session_manager2 = SessionManager.getInstance()
    print(f"session_manager1's session key :: {session_manager1.getSessionId()}")
    print(f"session_manager2's session key :: {session_manager2.getSessionId()}")

    session_vo1 = Session(123, 123, [1, 3, 4, 7])
    session_manager1.setSession(session_vo1)
    print(session_manager1.getSession().page_stack)
    print(session_manager2.getSession().page_stack)

if __name__ == '__main__':
    main()
