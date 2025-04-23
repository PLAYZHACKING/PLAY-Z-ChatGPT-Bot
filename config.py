import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "22161204"))
API_HASH = environ.get("API_HASH", "fdffc74281153b3338e4474f5640095e")
BOT_TOKEN = environ.get("BOT_TOKEN", "7644909159:AAFnUuXIsCT_5Tzw6ljOi0kdKgZqfvsvgfQ")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002644127305"))
ADMINS = int(environ.get("ADMINS", "7107162691"))
DB_URI = environ.get("DB_URI", "mongodb+srv://play-z-hacking:No-name-no@cluster0.dogzhpo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "play-z-hacking")
OPENAI_API = environ.get("OPENAI_API", "HIa96RvNJONEFGt7WyxRwb82DdjFGq6W")
AI = is_enabled((environ.get("AI","True")), False)
