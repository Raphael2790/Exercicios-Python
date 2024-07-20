import os
import dotenv

dotenv.load_dotenv()

senha = os.getenv('SENHA')
usuario = os.environ['USUARIO']

print(usuario, senha)
