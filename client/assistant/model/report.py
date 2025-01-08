from pydantic import BaseModel

class ReportRequest(BaseModel):
    dateStart: str | None = None
    dateEnd: str | None = None
    divisions: list[str] | None = None


class InfoReport(BaseModel):
    division: str
    divisionName: str
    manager: str
    managerName: str
    amount: int
    quantity: int
    assistantAmount: int
    assistantQuantity: int


class ReportResponse(BaseModel):
    dateStart: str
    dateEnd: str
    data: list[InfoReport] | None = None
    totalAmount: int
    totalQuantity: int
    totalAssistantAmount: int
    totalAssistantQuantity: int

