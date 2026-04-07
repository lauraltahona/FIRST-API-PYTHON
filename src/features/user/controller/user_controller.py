from features.user.dtos.user_dto import UserDtoRegister

class UserController:

    def __init__(self, service):
        self.service = service

    def save(self, req: UserDtoRegister):
        pass