import logging

logging.basicConfig(level=logging.INFO)

import sys
import os
from swibots import Client, InlineKeyboardButton, InlineMarkup

LOG = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("INPUT_TOKEN")
if not BOT_TOKEN:
    LOG.error("'token' not entered!")
    sys.exit(1)

app = Client(BOT_TOKEN, receive_updates=False)

community_id = os.getenv("INPUT_COMMUNITY_ID")
channel_id = os.getenv("INPUT_CHANNEL_ID")
group_id = os.getenv("INPUT_GROUP_ID")
user_id = os.getenv("INPUT_USER_ID")

if not ((community_id and (channel_id or group_id)) or user_id):
    LOG.error(
        "Chat identifiers are missing! Either fill user_id or channel_id/group_id with community_id"
    )
    exit()

document = os.getenv("INPUT_DOCUMENT")
message = os.getenv("INPUT_MESSAGE")

thumb = os.getenv("INPUT_THUMB")
button_text = os.getenv("INPUT_BUTTON_TEXT")
button_url = os.getenv("INPUT_BUTTON_URL")



async def main():
    LOG.debug("sending message on switch!")
    markup = None

    if button_text and button_url:
        markup = InlineMarkup([[InlineKeyboardButton(text=button_text, url=button_url)]])

    msg = await app.send_message(
        document=document,
        message=message,
        description=os.getenv("INPUT_DESCRIPTION") or message,
        caption=message,
        thumb=thumb,
        channel_id=channel_id,
        group_id=group_id,
        user_id=user_id,
        community_id=community_id,
        inline_markup=markup
    )
    LOG.info(f"Sent message, Message Id: {msg.id}")


app.run(main())
