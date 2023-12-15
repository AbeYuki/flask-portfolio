import os

class Config(object):
  DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  SQLALCHEMY_DATABASE_URI  = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
      **{
        'user': os.getenv('MARIADB_USER'),
        'password': os.getenv('MARIADB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('MARIADB_DATABASE'),
      })