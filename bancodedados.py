import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

# Criar a tabela no banco de dados

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# Inserir dados na tabela

# cursor.execute("INSERT INTO pessoas VALUES('Maria',40,'maria_123@gmail.com')")
# cursor.execute("INSERT INTO pessoas VALUES('Leonardo',36,'leorverga@gmail.com')")

# banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())