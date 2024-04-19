# Criar o banco de dados e conexão
import sqlite3
con = sqlite3.connect("cinema.db")

# Criar um objeto cursor
cur = con.cursor()

# Criar uma tabela
cur.execute("CREATE TABLE filme(titulo, ano, duracao)")
