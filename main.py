import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import requests

# إعدادات التسجيل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ضع توكن البوت الخاص بك هنا
TOKEN = '7611831885:AAFqR6X3893kG-EOfUjXk9Xz-9Ea3ZkY0Kk'

async def download_tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if 'tiktok.com' in url:
        await update.message.reply_text("جاري التحميل... انتظر لحظة ⏳")
        try:
            # استخدام API مجاني لتحميل الفيديو
            api_url = f"https://api.tiklydown.eu.org/api/download?url={url}"
            response = requests.get(api_url).json()
            video_url = response['video']['noWatermark']
            
            await update.message.reply_video(video=video_url, caption="تم التحميل بواسطة بوتك الخاص ✅")
        except Exception as e:
            await update.message.reply_text("عذراً، حدث خطأ أثناء التحميل. تأكد من الرابط.")
    else:
        await update.message.reply_text("أرسل رابط تيك توك صحيح.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_tiktok))
    application.run_polling()
