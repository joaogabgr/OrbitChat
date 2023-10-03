SECRET_KEY = 'API'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'fatec',
        servidor = 'localhost',
        database = 'OrbitChat'
    )