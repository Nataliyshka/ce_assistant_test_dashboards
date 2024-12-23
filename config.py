from pydantic_settings import BaseSettings, SettingsConfigDict 


class Settings(BaseSettings):
    BASE_URL: str
    BASE_AUTH_URL: str

    BASE_ONEC_URL: str

    ADMIN_LOGIN: str
    ADMIN_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
