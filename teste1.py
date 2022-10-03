# teste => este é um banco de dados quase concluido // proxima vez que alterar anotas coisas que faltam
# pip install db-sqlite3 // para instalar a biblioteca

import sqlite3

db = sqlite3.connect('segundo_banco.db')

cursor = db.cursor()

nome = str(input('qual o nome do aluno? '))
serie = str(input('qual sua serie: '))
n1 = float(input('digite a 1° nota: '))
n2 = float(input('digite a 2° nota: '))
n3 = float(input('digite a 3° nota: '))
n4 = float(input('digite a 4° nota: '))
media = float((n1 + n2 + n3 + n4)/4)

# cursor.execute("CREATE TABLE alunos (nome text, 1nota real, nota2 real, nota3 real, nota4 real, media real,
#               "serie text)")
cursor.execute("CREATE TABLE "+nome+" (nome text, nota1 real, nota2 real, nota3 real, nota4 real, media real )")
cursor.execute("INSERT INTO alunos VALUES('"+nome+"',"+str(n1)+","+str(n2)+","+str(n3)+","+str(n4)+","+str(media)+", '"
               + serie + "')")
cursor.execute("INSERT INTO "+nome+" VALUES('"+nome+"',"+str(n1)+","+str(n2)+","+str(n3)+","+str(n4)+","+str(media)+")")

db.commit()

cursor.execute("SELECT nota1 FROM "+nome)
print(cursor.fetchall())
