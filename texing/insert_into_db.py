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
        # create a new project
        project = ("Cool beans", "8957456436577");
        project_id = create_project(conn, project)
 
        # # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
 
        # # create tasks
        # create_task(conn, task_1)
        # create_task(conn, task_2)
 
 
if __name__ == '__main__':
    main()