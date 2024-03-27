from typing import Optional
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str = "hidden"
    openai_base_url: Optional[str] = None
    database_uri: str = "hidden"
    primary_model: str = "gpt-4-turbo-preview"
    secondary_model: str = "gpt-3.5-turbo"
    embedding_model: str = "text-embedding-3-small"
    input_path: str = "data/input"
    output_path: str = "data/output"

    class Config:
        env_file = ".env"


settings = Settings()

os.makedirs(settings.input_path, exist_ok=True)
os.makedirs(settings.output_path, exist_ok=True)


