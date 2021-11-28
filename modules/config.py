import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8763029"))
API_HASH = getenv("API_HASH", "5d0648a0d427266ec999d75f709376db")
BOT_USERNAME = getenv("BOT_USERNAME", "CandyMusic_Robot")
BOT_TOKEN = getenv("BOT_TOKEN")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/d5e8dbeb5654c8ed71e23.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
STRING_SESSION = getenv("STRING_SESSION")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2074956907").split()))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AbhumanyuXMusic/Heromusic")
aiohttpsession = aiohttp.ClientSession()
