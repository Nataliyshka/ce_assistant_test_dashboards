from client.assistant.client import AssistantClient
from client.assistant.enum import RoleUser


def test_post_report_sales():
    admin_user = RoleUser.ADMIN
    client_assistant = AssistantClient(admin_user)

    try:
        report_sales = client_assistant.post_report_sales()
        assert report_sales is not None, "report_sales is None"

    finally:
        client_assistant.close_session
    
print(test_post_report_sales())


