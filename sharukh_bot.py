from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# বটের ইনফো টেক্সট
INFO_TEXT = """<b>ᴋʜᴀɴ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 👑</b>
➡️ <b>Nᴀᴍᴇ :</b> 𝚂𝚑𝚊𝚛𝚞𝚔𝚑 𝚔𝚑𝚊𝚗 ✅
➡️ <b>N‌ɪᴄᴋɴᴀᴍᴇ :</b> ᴋʜᴀɴ 💚
➡️ <b>C‌ʟᴀss :</b> 12th ✅
➡️ <b>Cɪᴛʏ :</b> Mumbai  
➡️ <b>Wɪsʜ ᴍᴇ :</b> 20 December 🎂
➡️ <b>Cᴏᴜɴᴛʀʏ :</b> INDIA 
➡️ <b>S‌ᴛᴀᴛᴜs :</b> S‌ɪɴɢʟᴇ 👍
➡️ <b>𝚁𝚎𝚕𝚒𝚐𝚒𝚘𝚗 :</b> 𝙸𝚜𝚕𝚊𝚖 💕
➡️ <b>Lᴀɴɢᴜᴀɢᴇ ɪ ᴋɴᴏᴡ :</b> 💬 𝐁𝐚𝐧𝐠𝐥𝐚 /𝐇𝐢𝐧𝐝𝐢/ 𝐄𝐧𝐠𝐥𝐢𝐬𝐡 ❤️
❤️‍🔥 <b>𝗠𝘆 𝗛𝗼𝗯𝗯𝗶𝗲𝘀:</b> 💀 Hᴀᴄᴋɪɴɢ, Cᴀʀᴅɪɴɢ, Whhttt Mᴀᴋᴇɪɴɢ, Movies Wᴀᴛᴄʜɪɴɢ 4️⃣2️⃣0️⃣

<b>🅒🅞🅝🅣🅐🅒🅣 Username:</b> ➡️ @khan420sm  
<b>🅒🅗🅐🅝🅝🅔🅛 :</b> https://t.me/khan420smSKtricks

<b>Whatsapp business:</b>

🔞 <b>< Dɪꜱᴄʟᴀɪᴍᴇʀ ></b> 🔞  
✨ I have no special talent. I'm just passionately curious. My hobby is learning. ❗️  
<b>4️⃣2️⃣0️⃣𝚂𝚑𝚊𝚛𝚞𝚔𝚑</b>
"""

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(INFO_TEXT, parse_mode='HTML')

# মূল অ্যাপ রান করার ফাংশন
async def main():
    app = ApplicationBuilder().token("7969889390:AAFKEZHSUVyI06EQpl0UmdV-AjuCodMzhdU").build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

# রান করাও
import asyncio
asyncio.run(main())
