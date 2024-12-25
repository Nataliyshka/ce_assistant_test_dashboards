from pydantic import BaseModel


def check_status_code(code: int) -> bool:
    if code >= 200 and code < 400:
        return True
    
    return False
    
def save_json(data: BaseModel, file_name: str) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(data.model_dump_json(indent=4))
