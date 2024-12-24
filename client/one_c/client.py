import requests
from client.assistant.enum import RoleUser
from config import settings


class OneCClient:
    """Клиент для работы с 1С
    """    
    def __init__(self, role: RoleUser) -> None:
        self.__session = self.__get_authed_session(role)
        self.__base_url: str = settings.BASE_ONEC_URL

    def __get_authed_session(self, role: RoleUser) -> requests.Session:
        session = requests.Session()
        session.auth = (role.value.username.encode("utf-8"), role.value.password.encode("utf-8"))

        return session
    

    def close_session(self) -> None:
        self.__session.close()