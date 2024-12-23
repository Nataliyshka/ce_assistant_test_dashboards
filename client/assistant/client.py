import requests
import json
from client.assistant.enum import RoleUser
from client.assistant.model.auth import AuthRequest, AuthResponse
from client.utils import check_status_code
from config import settings


class AssistantClient:
    def __init__(self, role: RoleUser) -> None:
        self.__base_url__: str = settings.BASE_URL
        self.__base_url_auth: str = settings.BASE_AUTH_URL
        self.__session = self.__get_authed_session(role)


    def __get_authed_session(self, role: RoleUser) -> requests.Session:
        session = requests.Session()
        req = AuthRequest(data=role.value)
        resp = session.post(self.__base_url_auth, + '/api/v1/auth/login', json=req.model_dump())

        assert check_status_code(resp.status_code), 'status code is not positive'
        token = AuthResponse(**resp.json())

        session.headers['Authorization'] = f'Bearer {token.access_token}'
        return session


    def close_session(self) -> None:
        self.__session.close()
