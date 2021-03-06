import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import errors
from modules.config import BOT_USERNAME

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear@{BOT_USERNAME}", "clear"]) & ~filters.edited)
@errors
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **deleted all downloaded files**")
    else:
        await message.reply_text("❌ **no files downloaded**")

        
@Client.on_message(command(["rmw", "clean@{BOT_USERNAME}", "clean"]) & ~filters.edited)
@errors
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **deleted all raw files**")
    else:
        await message.reply_text("❌ **no raw files**")


@Client.on_message(command(["cleanup", "cleanup@{BOT_USERNAME}", "fresh"]) & ~filters.edited)
@errors
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **cleaned**")
    else:
        await message.reply_text("✅ **already cleaned**")
