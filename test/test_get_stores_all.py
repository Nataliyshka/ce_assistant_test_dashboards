from client.assistant.client import AssistantClient
from client.assistant.enum import RoleUser


def test_get_stores_all():
    admin_user = RoleUser.ADMIN
    client_assistant = AssistantClient(admin_user)

    try:
        stores = client_assistant.get_stores()
        assert stores is not None, "stores is None"

        print("Список магазинов:", stores)

    finally:
        client_assistant.close_session()
