# encoding: utf-8
class BnConnect:
    db_handler=None
    email_hander=None

def set_connect_user_account(userinfodb) :
        BnConnect.db_handler =userinfodb

def get_connect_user_account():
        return BnConnect.db_handler

def set_email_server(emailserver):
        BnConnect.email_hander=emailserver

def get_email_server():
        return BnConnect.email_hander

