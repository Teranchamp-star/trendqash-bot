
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8392366699:AAFcjWOy9294CD-8oJ76HVc5-aUZutD-keI"
REFERRAL_LINK = "https://www.trendqash.com/user/register.php?ref=Teranchamp"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("🔥 Join TrendQash Now", url=REFERRAL_LINK)],
        [InlineKeyboardButton("📘 How to Join", callback_data="how_to_join")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        f"Hey {update.effective_user.first_name}! 👋\n\n"
        "Want to earn **Ksh 2,000+ daily** from your phone?\n\n"
        "Join *TrendQash Agencies* today and start earning by referring others.\n"
        "Tap below to begin 👇",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "how_to_join":
        instructions = (
            "📌📌📌📌📌📌📌 *HOW TO JOIN TRENDQASH AGENCIES*\n\n"
            "1️⃣ Tap this link using Chrome:\n"
            f"{REFERRAL_LINK}\n\n"
            "2️⃣ Choose a *unique username* (no spaces, mix characters e.g. Maxke097)\n"
            "3️⃣ Use a *valid email* 📩\n"
            "4️⃣ Use a *password you’ll remember* 🔐\n"
            "5️⃣ Use the *same number you’ll pay with* 📱\n"
            "6️⃣ Pay *Ksh550 activation* to complete registration ✅\n\n"
            "📸 Screenshot your dashboard & send to me for help\n"
            "📞 DM me if you get stuck 😊"
        )
        await query.edit_message_text(instructions, parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
from telegram.ext import CallbackQueryHandler
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
