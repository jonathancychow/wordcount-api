from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv() 

class Config(BaseSettings):
  
    DATETIME_FORMAT:str = "%Y-%m-%d"

config = Config()
