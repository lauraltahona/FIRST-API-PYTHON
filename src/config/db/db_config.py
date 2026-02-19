from sqlalchemy import create_engine, Engine, text
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

# engine = create_engine(os.environ.get('DATABASE_CONNECTION'), echo=True)

# session_local = sessionmaker(engine, autoflush=False) # crea la maquina creadora de sesiones

# session = Session() # crea la sesion

class Database:

    _connection:str = None # el _ antes del atrbiuto indica que son privados
    _session:Session = None
    _engine:Engine = None
 
    def __init__(self):
        self._connection = os.environ.get('DATABASE_CONNECTION')
        self._engine = create_engine(self._connection, echo=True)
        self._session = sessionmaker(self._engine, autoflush=False) 
    
    def get_db(self):
        return self._session() # esto es como hacer Session()
    
    def get_engine(self) -> Engine:
        return self._engine
    
    def connect(self):
        try:
            connect = self._engine.connect()
            connect.execute(text("SELECT 1"))
            print(f"Database connected✅")
            return True
        except Exception as error:
            print(f"Error connection database: {error}")
            return False


   


