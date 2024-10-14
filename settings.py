from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    GOOGLE_API_KEY:str = None



def get_settings():
    settings = Settings()
    return settings