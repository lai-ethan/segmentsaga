from pydantic_settings import BaseSettings

# this file defines the settings for the application, including database connection details
# it uses pydantic's BaseSettings to manage configuration from environment variables
class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
# this wrapper function allows us to access the database URL as a property
    # it constructs the URL using the provided settings
    @property
    def database_url(self) -> str:
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

# this class is used to load environment variables from a .env file
# it inherits from BaseSettings, which automatically loads environment variables
# if the .env file is present in the same directory as this settings.py file
    # this allows us to easily manage configuration without hardcoding values
    class Config:
        env_file = '.env'

settings = Settings()
