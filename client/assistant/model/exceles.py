from pydantic import BaseModel

class ExcelRequest(BaseModel):
    dateStart: str | None = None
    dateEnd: str | None = None
    divisions: list[str] | None = None
