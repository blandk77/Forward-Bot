import datetime
import re
from os import environ 
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API = environ.get("API", "bfabf898bffa9192f184455d7d82954a26bf87eb") # shortlink api
URL = environ.get("URL", "gplinks.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/the_tgguy") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "not_ur_robot") # bot username without @
VERIFY = environ.get("VERIFY", "True")

class Config:
    API_ID = environ.get("API_ID", "26728872")
    API_HASH = environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7825342391:AAHcA9HPcf2uEzKWlZwTHKxIksPwIRvPNX4") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Telegram_Guy:I6AfG9KKBJ5397xF@botstore.t3cuf.mongodb.net/?retryWrites=true&w=majority&appName=Botstore")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Telegram_Guy")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1705634892').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002288135729'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/the_tgguy") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
