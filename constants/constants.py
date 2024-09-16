import os, logging

from dotenv import load_dotenv

load_dotenv()

PRODUCTION = os.getenv("ENVIRONMENT") == "PRODUCTION"
LOGGING_LEVEL = logging.WARNING if PRODUCTION else logging.NOTSET

BOT_TOKEN = ''
