"""Check if userbot awake or not . 

"""

import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime, CMD_HELP
from . import legend
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Config.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = "https://telegra.ph/file/fc22c880e9b4c74b9f33f.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TSF USER"

global ghanti
tag = borg.uid
ALIVE_MESSAGE= " ⚡ TSF ⚡  IS ON 🔥 FIRE ⚜️ \n\n"
ALIVE_MESSAGE += "🔱 SYSTEM STATUS🔱\n"
ALIVE_MESSAGE += "🔱TELETHON VERSION🔱 : 6.0.9\n⭕ Python: 3.9.2\n"
ALIVE_MESSAGE += "🔱DATABASE STATUS🔱 : Functional\n"
ALIVE_MESSAGE += "🔱Current Branch🔱 : Master\n"
ALIVE_MESSAGE += "🔱TSF OS🔱 :   `1.0`\n"
#op Bolte uptime add krna h
ALIVE_MESSAGE += f"⚜️ MY BOSS ⚜️: [{DEFAULTUSER}](tg://user?id={tag})\n"
ALIVE_MESSAGE += "⚜️MADE BY⚜️ 😎 : [STARK](https://t.me/CAD_BALY)\n\n"
ALIVE_MESSAGE += ":⚜️Deploy⚜️ **TSF BOT** : [ᖇᏋᎵᏫ](https://github.com/StarkX200/TSF-USERBOT)\n"           

@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "**Plugin : **`awake`\
    \n\n**Syntax : **`.awake`\
    \n**Function : **you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)

