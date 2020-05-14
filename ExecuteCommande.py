"Installer mysql client : pip install mysqlclient ou https://pypi.org/project/mysqlclient/#files"
"Entrer les parametres de la dataBase dans settings"
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "Nom de la BASE DE Donnée",
        'USER':"root",
        'PASSWORD':"tKyD4bRJ",
        'HOST':"localhost",
        'PORT':"3306",
    }
}
"""
#Dans le main  :

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_books(books):
    #Query=commande à réaliser
    query = "INSERT INTO Tables(Les Valeurs de la tables) " \
            "VALUES(Les Valeurs de la tables)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()
        