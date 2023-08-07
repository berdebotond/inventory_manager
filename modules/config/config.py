"""
Config for inventory manager
"""
import os
import dataclasses


@dataclasses.dataclass
class Config:
    # postgres config
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', '5432')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'postgres')

    # app config
    APP_HOST: str = os.getenv('APP_HOST', 'localhost')
    APP_PORT: str = os.getenv('APP_PORT', '8000')
    APP_DEBUG: bool = os.getenv('APP_DEBUG', True)


config = Config()
