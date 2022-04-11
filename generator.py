import Config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="DeecodeStringbot"),
)

app.storage.SESSION_STRING_FORMAT = ">B?256sQ?"

# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Yᴏᴜʀ API_ID/API_HASH ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.")
    except AccessTokenInvalid:
        raise Exception("Yᴏᴜʀ BOT_TOKEN ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.")
    uname = app.get_me().username
    print(f"@{uname} Sᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!")
    idle()
    app.stop()
    print("Bᴏᴛ Sᴛᴏᴘᴘᴇᴅ. Aʟᴠɪᴅᴀᴀ!")
