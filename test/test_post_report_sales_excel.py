import datetime
import io
import pandas as pd
from client.assistant.client import AssistantClient
from client.assistant.enum import RoleUser
from client.assistant.model.exceles import ExcelRequest
from client.utils import save_json

def test_post_report_sales_excel():
    """Получение отчета о продажах за период
    """
    admin_user = RoleUser.ADMIN
    client_assistant = AssistantClient(admin_user)

    try:
        # Создаем даты и форматируем их в ISO 8601 с UTC
        date_end = datetime.datetime.now(tz=datetime.UTC)
        date_start = date_end - datetime.timedelta(days=30)
        
        # Получаем bytes из API
        excel_bytes = client_assistant.post_report_sales_excel(
            dateStart=date_start.isoformat(),
            dateEnd=date_end.isoformat(),
            divisions=[]
        )
        
        excel_file = io.BytesIO(excel_bytes)
        
        # Читаем Excel из памяти
        df = pd.read_excel(excel_file)
        
        print("Отчет о продажах (первые 10 строк):")
        print(df.head(10))
        
    finally:
        client_assistant.close_session()
