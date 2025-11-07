import psycopg2

class conexao:
    def __init__(self):
        self.conn = psycopg2.connect(
            host ="192.168.200.171",
            database ="dbloja",
            user ="admin",
            password ="miRRor10"
        )

        self.con.autocommit = True
        self.cur = self.con.cursor()