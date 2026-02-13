from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')
ID = TypeVar('ID')

class ICrudRepository(ABC, Generic[T, ID]):

    @abstractmethod
    def save(self, entity: T) -> T:
        """Guarda un usuario en la base de datos"""
        pass

    @abstractmethod
    def delete(self, id: ID) -> bool:
        """Elimina un usuario de la base de datos"""
        pass
    
    @abstractmethod
    def update(self, id: ID, entity: T) -> T:
        """Actualiza un usuario en la base de datos"""
        pass

    @abstractmethod
    def get_by_id(self, id: ID) -> ID:
        """Obtiene un usuario por ID"""
        pass


    @abstractmethod
    def get_all(self):
        """Obtiene todas las entidades"""
        pass

