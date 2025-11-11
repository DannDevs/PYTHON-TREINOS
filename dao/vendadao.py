from model.venda import venda
from dao.conexao import obter_conexao
from dao.clientedao import clientedao
# import mysql.connector
import psycopg2

dao = clientedao()

class vendadao:
    def inserir(self,venda):
        try:
            conexao = obter_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO venda(codigo,valor,fkcliente,fkfuncionario) VALUES(%s,%s,%s,%s)"
            valores = (venda.codigo, venda.valor, venda.cliente.codigo, venda.funcionario.codigo)

            cursor.execute(sql,valores)
            dao.atualizarsaldo(venda.cliente.codigo, venda.cliente.saldo, venda.valor)
            
            conexao.commit()
            print("Venda Gravada com Sucesso")

        except psycopg2.Error as erro:
            print(f"Erro ao inserir venda: {erro}")
        finally:
            if conexao:
                conexao.close()
            if cursor:
                cursor.close()

    def listar(self):
        try:
            conexao = obter_conexao()
            cursor = conexao.cursor()
            
            sql = "SELECT codigo,valor,fkcliente,fkfuncionario from venda"
            cursor.execute(sql)

            resultados = cursor.fetchall()
            vendas = []

            for linha in resultados:
                f = venda(linha[0],linha[1],linha[2],linha[3])
                vendas.append(f)

            return vendas
        
        except psycopg2.Error as erro:
            print(f"Erro ao listar: {erro}")
            
        finally:
            if conexao:
                conexao.close()
            if cursor:
                cursor.close()




