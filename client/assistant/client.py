import requests
import json
from client.assistant.enum import RoleUser
from client.assistant.model.auth import AuthRequest, AuthResponse
from client.assistant.model.report import ReportRequest, ReportResponse
from client.assistant.model.store import StoreResponse
from client.utils import check_status_code
from config import settings


class AssistantClient:
    """Клиент для работы с ЦЕ Ассистентом
    """
    def __init__(self, role: RoleUser) -> None:
        self.__base_url__: str = settings.BASE_URL
        self.__base_url_auth: str = settings.BASE_AUTH_URL
        self.__session = self.__get_authed_session(role)

    def __get_authed_session(self, role: RoleUser) -> requests.Session:
        session = requests.Session()
        req = AuthRequest(data=role.value)
        resp = session.post(
            self.__base_url_auth + "/api/v1/auth/login", json=req.model_dump()
        )

        assert check_status_code(resp.status_code), "status code is not positive"
        token = AuthResponse(**resp.json())

        session.headers["Authorization"] = f"Bearer {token.access_token}"
        return session


    def post_report_sales(
        self,
        dateStart: str | None = None,
        dateEnd: str | None = None,
        divisions: list[str] | None = None,
    ) -> ReportResponse:
        """Получение отчета о продажах
        Args:
            dateStart (str | None): Дата начала периода
            dateEnd (str | None): Дата конца периода
            divisions (list[str] | None): Список подразделений
        Returns:
            ReportResponse: Ответ от сервиса
        """
        req = ReportRequest(dateStart=dateStart, dateEnd=dateEnd, divisions=divisions)
        resp = self.__session.post(
            self.__base_url__ + "/api/report/sales", json=req.model_dump()
        )
        assert check_status_code(resp.status_code), "status code is not positive"
        validated_resp = ReportResponse(**resp.json())
        return validated_resp
    

    def get_stores(self) -> StoreResponse:
        """Получение списка магазинов
        Returns:
            StoreResponse: Ответ от сервиса
        """
        resp = self.__session.get(self.__base_url__ + "/api/store/all")
        assert check_status_code(resp.status_code), "status code is not positive"
        validated_resp = StoreResponse(**resp.json())
        return validated_resp
    

    def close_session(self) -> None:
        self.__session.close()
