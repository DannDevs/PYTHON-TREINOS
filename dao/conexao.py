import mysql.connector


def obter_conexao():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="dbloja"
        )

    return conexao