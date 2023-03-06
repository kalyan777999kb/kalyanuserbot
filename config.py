import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25566413")) #optional
API_HASH = getenv("API_HASH", "5f4dcf21daeac7c01bb229e3e3349f3d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5655356960").split()))
OWNER_ID = int(getenv("OWNER_ID",  "5655356960"))
MONGO_URL = getenv("MONGO_URL",  "mongodb+srv://king777:king777@cluster0.apwndso.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6297634599:AAExITGpFSJgKdT_eAog6QdbL-zR6efwhtk")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/cf527681316908d4c1eeb.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP",  "-1001642786913")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAg9sYcZAa-rnFjgO003mvCjaiSUojhSR0Y7gl60eNYB6kWtWTYsB3UQzG_43Uq5Ebzm6nwt754qlKHmyHfX2miuHaY7eR_tS1AIGcmJ7L0AriTs90UCBpsWoJRxI75XTAeuOsOeaVeuyS6AezQ6-zVfpnBtiCP23-el8E5JzZLjXH4WE-cAX7Za5F8qwdYoXj1XKxRXMLl3fxcPQhjb9qZKegKxnjwdgsw28YJ5s4P9LgMvdvkJLjW0mZVVA8SpJP2hr0p5Ottwu3xHOHajznd8HTMznQOkF2Zxa8fStygeVyGWJAsH23hlDZHcNV-UooQ54dbmJ6ODn6EVlRMtbErQAAAAFRFeYgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
