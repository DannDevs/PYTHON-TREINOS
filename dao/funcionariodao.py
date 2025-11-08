from model.funcionario import funcionario
from dao.conexao import obter_conexao
import mysql.connector


class funcionariodao:
    def inserir(self,funcionario):
        try:
            conexao = obter_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO funcionario(codigo,nome,salario,cargo) VALUES(%s,%s,%s,%s)"
            valores = (funcionario.codigo,funcionario.nome,funcionario.salario,funcionario.cargo)
            cursor.execute(sql,valores)

            conexao.commit()
            print("Funcionario inserido com sucesso")

        except mysql.connector.Error as error:
            print(f"Erro ao inserir {error}")
        finally:
            if conexao:
                conexao.close()
            if cursor:
                cursor.close()
    
    def listar(self):
        try:
            conexao = obter_conexao()
            cursor = conexao.cursor()

            sql = "SELECT codigo,nome,salario,cargo FROM funcionario"
            cursor.execute(sql)
            resultados = cursor.fetchall()

            funcionarios = []

            for linha in resultados:
                f = funcionario(linha[0],linha[1],linha[2],linha[3])
                funcionarios.append(f)

            return funcionarios
        except mysql.connector.Error as error:
            print(f"Erro ao listar: {error}")
        finally:
            if conexao:
                conexao.close()
            if cursor:
                cursor.close()



    


