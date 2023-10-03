import mysql.connector
from mysql.connector import errorcode

print("Conectando...")

try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2412'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `OrbitChat`;")

cursor.execute("CREATE DATABASE `OrbitChat`;")

cursor.execute("USE `OrbitChat`;")

# criando tabelas
TABLES = {}
TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      id INT UNIQUE auto_increment,
      email VARCHAR(255) PRIMARY KEY,
      nome VARCHAR(255) not null,
      senha VARCHAR(255) not null            
)''')

TABLES['Comentarios'] = ('''
      CREATE TABLE Comentarios (
      id INT PRIMARY KEY auto_increment,
      fk_id INT not null,
      fk_nome VARCHAR(255) not null,            
      comentario LONGTEXT not null,
      foreign key (fk_id) references usuarios(id)
)''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()