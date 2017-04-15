import pymysql
import pymysql.cursors
import config

def connect_to_database():
  # options = {
  #   'host': config.env['host'],
  #   'user': config.env['user'],
  #   'passwd': config.env['password'],
  #   'db': config.env['db'],
  #   'cursorclass' : pymysql.cursors.DictCursor
  # }
  # db = pymysql.connect(**options)
  db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root', db='yuxi', cursorclass=pymysql.cursors.DictCursor)
  db.autocommit(True)
  return db
