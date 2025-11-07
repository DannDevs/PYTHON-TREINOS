from dao.conexao import obter_conexao
from model.cliente import cliente
import mysql.connector

class clientedao:

    def inserir(self,cliente):
        try:
         
            conexao = obter_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO cliente(codigo,nome,saldo) VALUES (%s,%s,%s)"
            valores = (cliente.codigo,cliente.nome,cliente.saldo)
            cursor.execute(sql,valores)

            conexao.commit()

            print("Cliente Inserido com sucesso")

        except mysql.connector.Error as erro:
            print(erro)
        
        finally:
        
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def exibir():
        
        try: 
            conexao = obter_conexao()
            cursor = conexao.cursor()
        except:
            pass
        finally:
            pass

           
           

    

