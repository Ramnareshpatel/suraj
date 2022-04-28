from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "**ᴍᴀᴅᴇ ʙʏ [會؄𝚂𝚄𝚁𝙰𝙹؄會](https://t.me/KingOf_univers)**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("💫 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Movies4youBackup")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "**ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇxᴛ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ.**"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "**ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇxᴛ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ.**"
        )
    user_id = message.from_user.id
    m = await message.reply_text("**ᴜᴘʟᴏᴀᴅɪɴɢ ᴄᴀʀʙᴏɴ...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ ᴄᴀʀʙᴏɴ...**")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
