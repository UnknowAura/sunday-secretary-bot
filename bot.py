import os
from telegram.ext import ApplicationBuilder, CommandHandler

# ดึงค่า Token จาก Railway
TOKEN = os.getenv('TOKEN')

async def start(update, context):
    await update.message.reply_text('สวัสดีค่ะนายท่าน! Sunday Secretary พร้อมรับใช้แล้วค่ะ')

async def menu(update, context):
    await update.message.reply_text('นี่คือเมนูสำหรับนายท่านค่ะ...')

async def buy(update, context):
    await update.message.reply_text('รับทราบค่ะ กำลังดำเนินการสั่งซื้อให้นายท่านค่ะ')

if __name__ == '__main__':
    # สร้าง Application ด้วย Token ที่ดึงมาจาก Environment
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('menu', menu))
    application.add_handler(CommandHandler('buy', buy))

    print("--- เลขา AI Sunday Secretary พร้อมปฏิบัติหน้าที่แล้ว ---")
    application.run_polling()
