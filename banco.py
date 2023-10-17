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
      usuario varchar(15) UNIQUE not null,
      email VARCHAR(255) PRIMARY KEY,
      nome VARCHAR(255) not null,
      senha VARCHAR(255) not null,
      qtd_seguidores INT DEFAULT 0,
      qtd_seguindo INT DEFAULT 0,
      banner VARCHAR(255) DEFAULT '/static/img/banner.jpg',
      perfil VARCHAR(255) DEFAULT '/static/img/perfil.svg',
      descricao VARCHAR(255) DEFAULT 'Sem descrição'        
)''')

TABLES['Comentarios'] = ('''
      CREATE TABLE Comentarios (
      id INT PRIMARY KEY auto_increment,
      fk_id INT not null,
      fk_nome VARCHAR(255) not null,
      fk_usuario VARCHAR(15) not null,
      resposta INT,
      qtd_respostas INT DEFAULT 0,
      qtd_likes INT DEFAULT 0,
      comentario TEXT not null,
      data DATETIME DEFAULT CURRENT_TIMESTAMP,
      fk_perfil VARCHAR(255) DEFAULT '/static/img/perfil.svg',
      foreign key (fk_id) references usuarios(id),
      foreign key (resposta) references comentarios(id),
      foreign key (fk_usuario) references usuarios(usuario),
      foreign key (fk_perfil) references usuarios(perfil)
)''')

TABLES['Likes'] = ('''
      CREATE TABLE Likes (
      id INT PRIMARY KEY auto_increment,
      user_id INT not null,
      tweet_id INT not null,
      foreign key (user_id) references usuarios(id),
      foreign key (tweet_id) references comentarios(id)
)''')

TABLES['Seguidor'] = ('''
      CREATE TABLE Seguidor (
      id INT PRIMARY KEY auto_increment,
      user_email VARCHAR(255) not null,
      fk_id INT not null,
      foreign key (user_email) references usuarios(email),
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