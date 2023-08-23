import pg8000

class PostgresDB:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.conn = pg8000.connect(
                host=self.host,
                database=self.dbname,
                user=self.user,
                password=self.password
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("Conectado")

        except pg8000.Error as e:
            print("Erro na conexão do Banco:", e)

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Conexão Encerrada")

    def insert(self, table_name, values):
        try:
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(values))})"
            self.cursor.execute(insert_query, values)
            print("Inserção realizada")
        except pg8000.Error as e:
            print("Erro na inserção", e)

    def select_all(self, table_name):
        try:
            select_query = f"SELECT * FROM {table_name}"
            with self.conn.cursor() as cursor:
                cursor.execute(select_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except pg8000.Error as e:
            print("Error selecting data:", e)

if __name__ == "__main__":
    db = PostgresDB(
        host="bd-t01-markkyn.clawdtcf3hq2.us-east-1.rds.amazonaws.com",
        dbname="postgres",
        user="professor",
        password="professor"
    )

    db.connect()

    dados = (2, "andre_britto@email.com", 'senhatop123')
    db.select_all("usuario")
    db.insert("usuario", dados)


    db.close()
