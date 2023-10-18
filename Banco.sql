-- Criar o banco de dados OrbitChat
-- Exclui o banco de dados se ele já existir
DROP DATABASE IF EXISTS OrbitChat;
CREATE DATABASE OrbitChat;
USE OrbitChat;

-- Criar a tabela Usuarios
CREATE TABLE Usuarios (
  id INT UNIQUE AUTO_INCREMENT,
  usuario VARCHAR(15) UNIQUE NOT NULL,
  email VARCHAR(255) PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  senha VARCHAR(255) NOT NULL,
  qtd_seguidores INT DEFAULT 0,
  qtd_seguindo INT DEFAULT 0,
  banner VARCHAR(255) DEFAULT '/static/img/banner.jpg',
  perfil VARCHAR(255) DEFAULT '/static/img/perfil.svg',
  descricao VARCHAR(255) DEFAULT 'Sem descrição',
  profissao VARCHAR(255) DEFAULT 'Sem profissão'
);

-- Criar a tabela Comentarios
CREATE TABLE Comentarios (
  id INT PRIMARY KEY AUTO_INCREMENT,
  fk_id INT NOT NULL,
  fk_nome VARCHAR(255) NOT NULL,
  fk_usuario VARCHAR(15) NOT NULL,
  resposta INT,
  qtd_respostas INT DEFAULT 0,
  qtd_likes INT DEFAULT 0,
  comentario TEXT NOT NULL,
  data DATETIME DEFAULT CURRENT_TIMESTAMP,
  fk_perfil VARCHAR(255) DEFAULT '/static/img/perfil.svg',
  FOREIGN KEY (fk_id) REFERENCES Usuarios(id),
  FOREIGN KEY (resposta) REFERENCES Comentarios(id),
  FOREIGN KEY (fk_usuario) REFERENCES Usuarios(usuario)
);

-- Criar a tabela Likes
CREATE TABLE likes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  tweet_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Usuarios(id),
  FOREIGN KEY (tweet_id) REFERENCES Comentarios(id)
);

-- Criar a tabela Seguidor
CREATE TABLE Seguidor (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_email VARCHAR(255) NOT NULL,
  fk_id INT NOT NULL,
  FOREIGN KEY (user_email) REFERENCES Usuarios(email),
  FOREIGN KEY (fk_id) REFERENCES Usuarios(id)
);
