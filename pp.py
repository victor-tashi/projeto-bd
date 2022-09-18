# import psycopg2
import psycopg2

# config

host = 'localhost'
dbname = 'teste'
user = 'postgres'
password = '2301'
sslmode = 'require'

# string de conexão
conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print('conectado')
