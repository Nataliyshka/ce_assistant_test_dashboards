from client.assistant.client import AssistantClient
from client.assistant.enum import RoleUser
from client.utils import save_json


def test_post_report_sales():
    """Тест получения отчета о продажах
    """
    admin_user = RoleUser.ADMIN
    client_assistant = AssistantClient(admin_user)

    try:
        report_sales = client_assistant.post_report_sales()
        assert report_sales is not None, "report_sales is None"
        assert report_sales.totalQuantity > report_sales.totalAssistantQuantity, "Количество продаж меньше суммы продаж по Ассистсенту"

        save_json(report_sales, "report_sales.json")

        print("Отчет о продажах:", report_sales)

    finally:
        client_assistant.close_session
    


