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
            print("Erro ao Inserir" + erro)
        
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def listar(self):
        
        try: 
            conexao = obter_conexao()
            cursor = conexao.cursor()

            sql = "SELECT codigo,nome,saldo FROM cliente" 
            cursor.execute(sql)

            resultados = cursor.fetchall()
            clientes = []

            for linha in resultados:
                c = cliente(linha[0],linha[1],linha[2])
                clientes.append(c)
            
            return clientes
                

        except mysql.connector.Error as erro:
            print(f"Erro na consultar")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
                
    def excluir(self,cliente):
        try:
            conexao = obter_conexao()
            cursor = conexao.cursor()

            sql = "DELETE FROM cliente where codigo = (%s)"
            valores = (cliente.codigo)
            cursor.execute(sql,valores)

            conexao.commit()
        
            print("Cliente deletado com sucesso")

        except mysql.connector.Error as error:
        
            print(f"Erro ao excluir: {error}")
        
        finally:
            if conexao:
                conexao.close()
            if cursor:
                cursor.close()


           
           

    

