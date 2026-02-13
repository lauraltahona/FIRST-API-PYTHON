from sqlalchemy import Column, Integer, String
from src.config.db.base_declarative import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, index=True) # el index es recomendable declararlo en atributos que son de constante búsqueda en la base de datos
    # ya que index "crea una tabla" exclusiva de "id" y pone todos los id de los usuarios en esa tabla, por tanto
    # cuando queramos buscar por id, se busca en esa tabla
    email = Column(String(100), unique=True, index=True)
    password = Column(String(150))

