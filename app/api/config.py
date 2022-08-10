import os
import secrets
from dotenv import load_dotenv

from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

load_dotenv() 

class Config(BaseSettings):
  

    DATETIME_FORMAT:str = "%Y-%m-%d"



   


config = Config()
