# from mysql.connector import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config
 
# def insert_movies(movies):
#     query = "INSERT INTO movies(id,title) " \
#             "VALUES(%s,%s)"
 
#     try:
#         db_config = read_db_config()
#         conn = MySQLConnection(**db_config)
 
#         cursor = conn.cursor()
#         cursor.executemany(query, movies)
 
#         conn.commit()
#     except Error as e:
#         print('Error:', e)
 
#     finally:
#         cursor.close()
#         conn.close()
 
# def main():
#     movies = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
#              ('Gone with the Wind', '9780446675536'),
#              ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
#     insert_movies(movies)
 
# if __name__ == '__main__':
#     main()







import sqlite3
from sqlite3 import Error

import tmdbsimple as tmdb

from dotenv import load_dotenv  
import os

load_dotenv()
tmdb_token = os.getenv('TMDB_TOKEN')
tmdb.API_KEY = tmdb_token

import re
 
 
def create_connection(db_file):
		""" create a database connection to the SQLite database
				specified by db_file
		:param db_file: database file
		:return: Connection object or None
		"""
		conn = None
		try:
				conn = sqlite3.connect(db_file)
		except Error as e:
				print(e)
 
		return conn
 
 
def create_project(conn, project):
		"""
		Create a new project into the projects table
		:param conn:
		:param project:
		:return: project id
		"""
		sql = ''' INSERT INTO movies(id, title)
							VALUES(?,?) '''
		cur = conn.cursor()
		cur.execute(sql, project)
		return cur.lastrowid
 
 
# def create_task(conn, task):
#     """
#     Create a new task
#     :param conn:
#     :param task:
#     :return:
#     """
 
#     sql = ''' INSERT INTO movies(name,priority,status_id,project_id,begin_date,end_date)
#               VALUES(?,?,?,?,?,?) '''
#     cur = conn.cursor()
#     cur.execute(sql, task)
#     return cur.lastrowid
 
 
def main():
		# database = r"C:\sqlite\db\pythonsqlite.db"
 
		# create a database connection
		conn = create_connection("movies.db")
		with conn:
			count = 1
			with open("../Flash_drive/index.txt","r") as index:
			  for ln in index:
			    if ln.startswith("Title: "):
			    	movie = ln[7:].rstrip("\n\r")
			    	project = (count, movie);
			    	project_id = create_project(conn, project)
			    	count += 1


				# create a new project
				# project = ("8957456436577", "Cool beans");
				# project_id = create_project(conn, project)
 
				# # tasks
				# task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
				# task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
 
				# # create tasks
				# create_task(conn, task_1)
				# create_task(conn, task_2)
 
 
if __name__ == '__main__':
	# index = open("../Flash_drive/index.txt","r") 
	# index.read()
	# index.close() 

	# with open("../Flash_drive/index.txt","r") as index:
	#   movies = []
	#   for ln in index:
	#     if ln.startswith("Title: "):
 #      	movies.append(ln[7:].rstrip("\n\r"))
	# print(movies)

	search = tmdb.Search()
	response = search.movie(query='Divergent')
	id_movie = search.results[0]['id']
	print (id_movie)

	# with open("../Flash_drive/index.txt","r") as index:
	#   for ln in index:
	#     if ln.startswith("Title: "):
	#     	movie = ln[7:].rstrip("\n\r")
	#     	# print (movie)
	#     	search = tmdb.Search()
	#     	response = search.movie(query=movie)
	#     	if len(search.results) > 0:
	#     		id_movie = search.results[0]['id']
	#     		# print (id_movie)
	#     	else:
	#     		id_movie = 0
	#     		print (movie, id_movie)




	# main()

	# test = "step up"
	# conn = sqlite3.connect('movies.db')
	# c = conn.cursor()
	# for row in c.execute('SELECT * FROM movies'):
	# 	if test.lower() == row[1].lower():
	# 		print ("Found")


	 
	 






