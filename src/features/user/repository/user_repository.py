from abc import ABC, abstractmethod

class ICrudUserRepository(ABC):

    @abstractmethod
    def save(self):
        """Guarda un usuario en la base de datos"""
        pass

    @abstractmethod
    def delete(self):
        """Elimina un usuario de la base de datos"""
        pass
    
    @abstractmethod
    def update(self):
        """Actualiza un usuario en la base de datos"""
        pass

    @abstractmethod
    def get_by_id(self):
        """Obtiene un usuario por ID"""
        pass

