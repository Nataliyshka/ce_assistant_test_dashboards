from enum import Enum
from client.assistant.model.auth import AuthUser
from config import settings

admin_user = AuthUser(username=settings.ADMIN_LOGIN, password=settings.ADMIN_PASSWORD)

class RoleUser(Enum):
    ADMIN = admin_user