from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# 🔑 API Key Gemini
genai.configure(api_key=" ")

# Inisialisasi model Gemini
model = genai.GenerativeModel('gemini-2.0-flash')

# Ganti dengan token bot kamu
TOKEN = " "

# Fungsi saat ada /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Yahoo!, saya Hanabi. tanyakan apa saja tentang Bahasa Jepang saya akan bantu menjawabnya.
""")

# Fungsi saat menerima pesan teks biasa
prompt_template = """
Anda adalah bot yang memiliki pemahaman tentang Bahasa Jepang, anda harus memberikan respon dari pertanyaan berikut:
"{pertanyaan}"
sesuai dengan permintaan user. Baik tentang kanji, kosakata, atau apapun yang berkatian dengan bahasa Jepang
"""

# Fungsi untuk menangani pesan teks
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text("Tunggu Sebentar, saya sedang berpikir... ")

    try:
        response = model.generate_content(prompt_template.format(pertanyaan=user_input))
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan: {e}")

# Jalankan aplikasi bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    app.run_polling()
