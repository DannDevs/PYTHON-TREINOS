import psycopg2

class conexao:
    def __init__(self):
        self.conn = psycopg2.connect(
            host ="192.168.",
            database ="",
            user ="",
            password =""
        )

        self.con.autocommit = True
        self.cur = self.con.cursor()