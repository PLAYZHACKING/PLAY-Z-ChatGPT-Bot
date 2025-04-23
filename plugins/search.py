from pyrogram import Client, filters
from config import OPENAI_API, LOG_CHANNEL, AI
import asyncio
import requests

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i+max_length])


@Client.on_message(filters.private & filters.text & ~filters.command(['start', 'broadcast']))
async def ai_answer(client, message):
    if AI == True:
        user_id = message.from_user.id
        if user_id:
            try:
                msg = await message.reply_text("**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ᴡʜɪʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ ʀᴇsᴘᴏɴᴅs ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ . . .**")
                users_message = message.text

                headers = {
                    "Authorization": f"Bearer {OPENAI_API}",
                    "Content-Type": "application/json"
                }

                data = {
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": users_message}
                    ],
                    "max_tokens": 1200,
                    "temperature": 0.6
                }

                r = requests.post(
                    "https://api.deepinfra.com/v1/openai/chat/completions",
                    headers=headers,
                    json=data
                )

                response_data = r.json()
                ai_response = response_data["choices"][0]["message"]["content"].strip()

                footer_credit = "<b><a href='https://t.me/vj_bot_disscussion'>• ʀᴇᴘᴏʀᴛ ɪꜱꜱᴜᴇ •</a>══<a href='https://t.me/kingvj01'>• ᴄᴏɴᴛᴀᴄᴛ ᴍᴀꜱᴛᴇʀ •</a></b>"

                await msg.delete()
                await send_message_in_chunks(client, message.chat.id, f"**ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀɴsᴡᴇʀ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ** 👇\n\n{ai_response}\n\n{footer_credit}")
                await send_message_in_chunks(client, LOG_CHANNEL, f"**⭕ ᴀ ᴜsᴇʀ ɴᴀᴍᴇᴅ:** {message.from_user.mention} **ᴡɪᴛʜ ᴜsᴇʀ ɪᴅ -** {user_id}.\n🔍 **ᴀsᴋᴇᴅ ᴍᴇ ᴛʜɪs ǫᴜᴇʀʏ...**👇\n\n🔻 **ǫᴜᴇʀʏ:** `{users_message}`\n\n🔻 **ʜᴇʀᴇ ɪs ᴀɴsᴡᴇʀ ɪ ʀᴇsᴘᴏɴᴅᴇᴅ:**\n🖍️ {ai_response}\n\n\n🔻 **ᴜsᴇʀ ɪᴅ :-** {user_id} \n🔻 **ᴜsᴇʀ ɴᴀᴍᴇ :-** {message.from_user.mention}")

            except Exception as error:
                print(error)
                await message.reply_text(f"**An error occurred:**\n\n**{error}**\n\n**Forward This Message To @KingVJ01**")
    else:
        return