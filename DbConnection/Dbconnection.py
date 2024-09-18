import cx_Oracle

class DbConnection:
    def __init__(self):
        # Configurações da conexão com o banco de dados
        self.username = "cvd31722"  # Coloque seu nome de usuário
        self.password = "sua_senha_aqui"  # Coloque sua senha
        self.dsn = cx_Oracle.makedsn(
            "200.131.242.43",  # Hostname do banco de dados
            1521,  # Porta do banco de dados
            service_name="IFNMGPDB"  # Nome do serviço
        )
        self.connection = None

    def connect(self):
        try:
            # Estabelecendo a conexão com o banco de dados
            self.connection = cx_Oracle.connect(
                user=self.username,
                password=self.password,
                dsn=self.dsn
            )
            print("Conexão com o banco de dados estabelecida com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados foi encerrada.")

# Instância e conexão
db = DbConnection()
db.connect()  # Faz a conexão

# Não precisa executar nada, mas pode encerrar a conexão quando quiser
# db.close()
