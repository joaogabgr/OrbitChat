# OrbitChat

Uma rede social baseada no Twitter, desenvolvida como projeto de estudo.

## Visão Geral

O OrbitChat é uma plataforma de rede social que se inspira no Twitter para fornecer uma experiência de comunicação rápida e direta. Este projeto foi criado com o intuito de aprimorar habilidades em HTML, CSS, JavaScript, Python (utilizando Flask) e integração com MySQL.

## Tecnologias Utilizadas

- HTML
- CSS
- JavaScript
- Python (Flask)
- MySQL

## Requisitos minimos

- MySQL Server
- Python
- VirtualEnv

## Funcionalidades Principais

- **Postagem de Mensagens:** Assim como no Twitter, os usuários podem compartilhar mensagens curtas com seus seguidores.
- **Autenticação de Usuário:** Login seguro e autenticação para proteger as contas dos usuários.
- **Persistência de Dados:** Utilização de um banco de dados MySQL para armazenar informações de usuários e postagens.
- **Pesquisa Avançada de Usuários e Mensagens:** Permita que os usuários pesquisem por palavras-chave, hashtags ou outros critérios para encontrar usuários e mensagens específicos.
- **Perfil do Usuário Personalizado:** Permita que os usuários personalizem seus perfis com fotos, biografias e outras informações relevantes.
- **Sistema de Hashtags e Trending Topics:** Permita que os usuários utilizem hashtags para categorizar suas postagens e vejam os tópicos mais populares.
- **Sistema de Comentários:** Possibilidade de comentar em postagens e interagir com outros usuários.
- **Sistema de Likes e Retweets:** Permita que os usuários curtam e compartilhem postagens de outros usuários.
- **Personalização do Feed:** Os usuários podem personalizar o conteúdo exibido em seu feed com base em suas preferências e quem estão seguindo.
- **Mensagens Privadas:** Capacidade de enviar mensagens privadas para outros usuários.

## Capturas de Tela

_(Adicione capturas de tela do projeto aqui, se disponíveis)_

## Configuração do Ambiente

Para configurar o ambiente e iniciar o projeto, siga os passos abaixo:

1. Clone este repositório:

```bash
git clone https://github.com/seu_usuario/orbit-chat.git
```

2. Ative a maquina virtual:

```bash
py -m venv venv
```

3. Ativar a venv:

```bash
.\venv\Scripts\activate.bat
```

4. Baixar dependencias:

```bash
pip install -r requirements.txt
```

5. Rodar banco de dados:

```bash
python banco.py
```

6. Iniciar programa:

```bash
python app.py
```
