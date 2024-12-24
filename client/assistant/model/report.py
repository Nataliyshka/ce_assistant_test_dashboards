from pydantic import BaseModel


class Division(BaseModel):
    guid: str


class ReportRequest(BaseModel):
    dateStart: str | None = None
    dateEnd: str | None = None
    divisions: list[Division] | None = None


class InfoReport(BaseModel):
    division: str
    divisionName: str
    manager: str
    amount: int
    quantity: int
    assistantAmount: int
    assistantQuantity: int


class ReportResponse(BaseModel):
    dateStart: str
    dateEnd: str
    data: list[InfoReport]
    totalAmount: int
    totalQuantity: int
    totalAssistantAmount: int
    totalAssistantQuantity: int

