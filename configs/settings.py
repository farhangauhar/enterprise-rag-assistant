try:
    # pydantic v2+: BaseSettings moved to pydantic-settings package
    from pydantic_settings import BaseSettings
except Exception:
    # fallback for older pydantic versions where BaseSettings was in pydantic
    from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Enterprise RAG Assistant"
    VERSION: str = "1.0"


settings = Settings()
