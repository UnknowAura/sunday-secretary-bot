from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# รายการสินค้าในสต็อก
PRODUCTS = {
    "organizer.exe": {
        "price": 199,
        "link": "https://drive.google.com/uc?export=download&id=1wxh0RO_UZmo8NPt49m4LZoP4lUoUrfA5"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="สวัสดีค่ะนายท่าน! Sunday Secretary พร้อมรับใช้ค่ะ!\nพิมพ์ /menu ดูสินค้า หรือ /buy [ชื่อสินค้า] [จำนวน] เพื่อสั่งซื้อนะคะ!"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "รายการสินค้าพร้อมส่งค่ะ:\n"
    for item, info in PRODUCTS.items():
        msg += f"- {item}: {info['price']} บาท\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ใช้คำสั่ง: /buy [ชื่อสินค้า] [จำนวน]\nตัวอย่าง: /buy organizer.exe 1")
        return
    
    item = context.args[0]
    try:
        qty = int(context.args[1])
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="จำนวนต้องเป็นตัวเลขนะคะ!")
        return
    
    if item in PRODUCTS:
        total = PRODUCTS[item]['price'] * qty
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=f"รับทราบค่ะนายท่าน!\nออเดอร์: {item} จำนวน {qty} ชิ้น\nยอดรวม: {total} บาท\n\nโอนเงินผ่าน QR Code ที่ปักหมุดไว้ แล้วแคปสลิปแจ้งยืนยันได้เลยค่ะ!\nยืนยันแล้วเลขาจะส่งลิงก์ดาวน์โหลดให้ทันทีค่ะ!"
        )
        print(f"--- [NEW ORDER] ลูกค้าสั่ง {item} จำนวน {qty} ชิ้น ยอด {total} บาท ---")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="ขออภัยค่ะ สินค้านี้ไม่มีในสต็อก")

if __name__ == '__main__':
    # ใส่ Token ใหม่ล่าสุดตรงนี้
    TOKEN = '8860362270:AAHD3n2fXrFb7b7OXyobPhSaIYCQmrN0UgE'
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('menu', menu))
    application.add_handler(CommandHandler('buy', buy))
    
    print("--- เลขา AI Sunday Secretary พร้อมปฏิบัติหน้าที่แล้ว ---")
    application.run_polling()