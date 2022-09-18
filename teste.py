import sqlite3
from random import randint

db = sqlite3.connect('primeiro_banco.db')

cursor = db.cursor()
# nome = str(input('digite seu nome: '))
# iD = randint(100, 1000)
# email = str(input('digite seu email: '))
# senha = str(input('digite sua senha'))
s1 = 100

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
# cursor.execute("INSERT INTO pessoas VALUES('edvan',14, 'edvan.@gmail.com')")

# cursor.execute("CREATE TABLE produtos (nome text, quantidade integer)")
cursor.execute("INSERT INTO produtos VALUES('cimento' ,"+str(s1)+")")
# cursor.execute("CREATE TABLE teste (nome text, id integer, email text, senha text)")
# cursor.execute("INSERT INTO teste VALUES(" + nome + "," + str(iD) + "," + email + "," + senha + ")")
qtd = int(input('quantos você vai comprar'))

s2 = s1 - qtd

db.commit()
#
cursor.execute("SELECT * FROM teste")
print(cursor.fetchall())
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
