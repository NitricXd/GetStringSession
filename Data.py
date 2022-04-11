from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hɪɪ.. {}
Wᴇʟᴄᴏᴍᴇ ᴛᴏ \n{}
Bᴏᴛ Fᴏʀ Hᴇʟᴘ Yᴏᴜ Tᴏ Cʀᴇᴀᴛᴇ Sᴇssɪᴏɴ.
[➼](https://telegra.ph/file/8b29630aadd3ae5b4fb5c.jpg) Sᴏ Wʜʏ Aʀᴇ Yᴏᴜ Wᴀɪᴛɪɴɢ Fᴏʀ Gᴇɴᴇʀᴀᴛᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.
───────────────────────

Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Pʏʀᴏɢʀᴀᴍ Aɴᴅ Tᴇʟᴇᴛʜᴏɴ Sᴛʀɪɴɢ Sᴇssɪᴏɴ. Usᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs Tᴏ Lᴇᴀʀɴ Mᴏʀᴇ ! 

Pᴏᴡᴇʀᴇᴅ  Bʏ: [Nɪᴛʀɪᴄ xD](https://t.me/MrNitric)
    """   

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("📡Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ🔰", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("📡Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ🔰", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("📡Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ🔰", callback_data="generate")],
        [InlineKeyboardButton("Jᴏɪɴ Gʀᴏᴜᴘ", url="https://t.me/The_Friend_Circle")],
        [
            InlineKeyboardButton("Hᴏᴡ Tᴏ Usᴇ", callback_data="help"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ", url="https://t.me/Sanki_Bots")],
    ]

    # Help Message
    HELP = """
**Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs** 🛠



/about - Aʙᴏᴜᴛ Tʜᴇ Bᴏᴛ
/help - Tʜɪs Mᴇssᴀɢᴇ
/start - Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
/generate - Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ
/cancel - Cᴀɴᴄᴇʟ Tʜᴇ Pʀᴏᴄᴇss
/restart - Cᴀɴᴄᴇʟ Tʜᴇ Pʀᴏᴄᴇss
"""

    # About Message
    ABOUT = """
**Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ** 

A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ᴍᴀɴᴀɢᴇ ɢʀᴏᴜᴘ ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ 

Fʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

Lᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)
    """
