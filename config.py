import datetime
from os import environ 
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API = environ.get("API", "") # shortlink api
URL = environ.get("URL", "") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "") # bot username without @
VERIFY = environ.get("VERIFY", "True")

class Config:
    API_ID = environ.get("API_ID", "26728872")
    API_HASH = environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7825342391:AAHcA9HPcf2uEzKWlZwTHKxIksPwIRvPNX4") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://python21java:<8ZFGYMKJCqAPwsiO>@cluster0.4ieuy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "TS")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1705634892').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002288135729'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
