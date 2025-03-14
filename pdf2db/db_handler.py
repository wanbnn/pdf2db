import sqlite3

class DBHandler:
    """Classe para gerenciar operações com o banco de dados SQLite."""

    def __init__(self, db_file):
        """
        Inicializa a conexão com o banco de dados.

        Args:
            db_file (str): Caminho para o arquivo do banco de dados.
        """
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Cria uma conexão com o banco de dados SQLite.

        Args:
            db_file (str): Caminho para o arquivo do banco de dados.

        Returns:
            sqlite3.Connection: Conexão com o banco de dados.
        """
        try:
            conn = sqlite3.connect(db_file)
            print(f"Conexão com o banco de dados estabelecida: {sqlite3.sqlite_version}")
            return conn
        except sqlite3.Error as e:
            print(e)
            return None

    def create_table(self):
        """
        Cria a tabela 'book_content' no banco de dados.
        """
        try:
            sql_create_table = """
            CREATE TABLE IF NOT EXISTS book_content (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "from" TEXT NOT NULL,
                type TEXT NOT NULL,
                content TEXT NOT NULL
            );
            """
            cursor = self.conn.cursor()
            cursor.execute(sql_create_table)
            self.conn.commit()
            print("Tabela 'book_content' criada com sucesso.")
        except sqlite3.Error as e:
            print(e)

    def insert_content(self, book_name, content_type, content_text):
        """
        Insere conteúdo processado na tabela 'book_content'.

        Args:
            book_name (str): Nome do livro.
            content_type (str): Tipo de conteúdo ('paragraph', 'dialogue', 'quote').
            content_text (str): Conteúdo extraído.
        """
        try:
            sql_insert = """
            INSERT INTO book_content ("from", type, content)
            VALUES (?, ?, ?);
            """
            cursor = self.conn.cursor()
            cursor.execute(sql_insert, (book_name, content_type, content_text))
            self.conn.commit()
            print(f"Dados inseridos com sucesso: {book_name}, {content_type}")
        except sqlite3.Error as e:
            print(e)

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")