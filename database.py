# database.py

import psycopg2
from psycopg2 import pool
from config import DATABASE_CONFIG

class Database:
    __connection_pool = None

    @staticmethod
    def initialise():
        Database.__connection_pool = pool.SimpleConnectionPool(1, 
                                                               10,
                                                               user=DATABASE_CONFIG['user'],
                                                               password=DATABASE_CONFIG['password'],
                                                               database=DATABASE_CONFIG['database'],
                                                               host=DATABASE_CONFIG['host'])

    @staticmethod
    def get_connection():
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()

# Initialise the connection pool
Database.initialise()