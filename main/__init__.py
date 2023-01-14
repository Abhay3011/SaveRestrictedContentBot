#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=9544521, cast=int)
API_HASH = config("API_HASH", "5cf32e97dc94510e46524f2286c95116")
BOT_TOKEN = config("BOT_TOKEN", "5874353588:AAEKkbKzOnskfv4U2vUSXNFibK_dpk6f4Y8")
SESSION = config("SESSION",  "BQAtv8GtzHzQ50_inYgzFm7S_Q4vCHFjL5Ohg4ZEYF6_zVNtx-MutpGVXO44NO56chEynYh48H5K2vMkyppSWueYjg55rbYOoVdkoCLIV3LJXh_mGqgLMf-xAsIaywrb8OLnn9FvPvpHmT4eH30tk_YNeyQUFgx4L890lcrrxTIpgis9pc2XPePjXlYYaIkZOQtLERbNIbsAFW7d4Vhdu_XCIg_kovUOY53bitBOrtspkNzIkO9aY0NpTsOaGB19eYszQPuBWCqkzI6Jqb9tjKHZ1jY8laY1idd67V479w7JcQIxCi_H0_lSKBeQt8On_8oRJO7-rb7bM3tiHs0MYe-zUPt39wA")
FORCESUB = config("FORCESUB", "bot_logv4")
AUTH = config("AUTH", default=1358657527, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
