# import mysql.connector
import psycopg2


def obter_conexao():
    
    conexao = psycopg2.connect(
        dbname="dbloja",
        user="admin",
        password="miRRor10",
        host="192.168.200.171",
        port="5432"
    )

    # conexao = mysql.connetor.connect(
    #     host="127.0.0.1",
    #     port=3306,
    #     user="root",
    #     password="",
    #     database="dbloja"
    #     )

    return conexao

 

    