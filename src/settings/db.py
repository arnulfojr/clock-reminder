
import os


DB_USER = os.getenv('DB_USER')

DB_SCHEMA = os.getenv('DB_SCHEMA', 'sqlite')

DB_URI = os.getenv('DB_URI', None)

DB_ECHO = os.getenv('DB_ECHO', 'False') == 'True'

