# import traceback
import psycopg2

class DBManager(object):
    "Singleton class that manager the database conection"

    # Instance of database
    _db_instance = None

    # data for conection with database
    _user = None
    _password = None
    _host = None
    _port = None
    _database = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, user, password, host, port, database):
        if cls._db_instance is None:
            print('Creating new DBManager instance')
            
            cls._user = user
            cls._password = password
            cls._host = host
            cls._port = port
            cls._database = database

            cls._db_instance = cls.__new__(cls)
            
        return cls._db_instance

    @classmethod
    def connect_with_database(cls):

        if cls._db_instance == None :
            raise RuntimeError('First instance DBManager connection instead')
            # return None

        return psycopg2.connect(
            user = cls._user, 
            password = cls._password,
            host = cls._host, 
            port = cls._port,
            database = cls._database
        )
    