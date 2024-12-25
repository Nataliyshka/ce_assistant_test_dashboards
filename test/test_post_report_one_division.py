import random
from client import utils
from client.assistant.client import AssistantClient
from client.assistant.enum import RoleUser


def test_post_report_one_division():
    """Тест получения отчета о продажах по одному подразделению
    1.Получение отчета о продажах
    2.Выбор случайного подразделения
    3.Получение отчета о продажах по выбранному подразделению
    4.Проверка, что все продажи по выбранному подразделению
    """
    admin_user = RoleUser.ADMIN
    client_assistant = AssistantClient(admin_user)

    try:
        # 1.Получение отчета о продажах
        report_sales = client_assistant.post_report_sales()
        assert report_sales is not None, "report_sales is None"
        
        # 2.Выбор случайного подразделения
        divisions = list(set(sale.division for sale in report_sales.data))
        random_division = random.choice(divisions)

        # 3.Получение отчета о продажах по выбранному подразделению
        report_sales = client_assistant.post_report_sales(divisions=[random_division])
        assert report_sales is not None, "report_sales is None"

        # 4.Проверка, что все продажи по выбранному подразделению
        isSalesByDivision = all(sale.division == random_division for sale in report_sales.data)
        assert isSalesByDivision, "Продажи не по отобранному подразделению"

        utils.save_json(report_sales, "report_sales_one_division.json")

        print("Отчет о продажах:", report_sales)
    finally:
        client_assistant.close_session()
