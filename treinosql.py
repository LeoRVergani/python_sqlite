# Criar o banco de dados e conexão
import sqlite3
con = sqlite3.connect("cinema.db")

# Criar um objeto cursor
cur = con.cursor()

# Criar uma tabela
# cur.execute("CREATE TABLE filme (titulo text, ano integer, duracao integer)")

# Verificar se tabela foi criada
# res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchone()

# Inserir linhas na tabela
cur.execute("""
            INSERT INTO filme VALUES
                ('O Senhor dos Anéis: A Sociedade do Anel', 2001, 178),
            ('Conan, o Bárbaro', 1982, 129)
""")
con.commit()

cur.execute("SELECT * FROM filme")
print(cur.fetchall())

