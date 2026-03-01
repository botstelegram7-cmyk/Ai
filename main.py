import os
import threading
import logging
from flask import Flask, jsonify
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters
)
from bot import (
    start_command, ask_command, imagine_command,
    clear_command, status_command, help_command,
    handle_message, button_handler,
    BOT_TOKEN
)

# ─── Flask App ────────────────────────────────────────────────────────────────
flask_app = Flask(__name__)

@flask_app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "Grok AI Telegram Bot is Running 🤖"})

@flask_app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# ─── Bot Runner ───────────────────────────────────────────────────────────────
def run_bot():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        level=logging.INFO
    )

    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start",   start_command))
    app.add_handler(CommandHandler("ask",     ask_command))
    app.add_handler(CommandHandler("imagine", imagine_command))
    app.add_handler(CommandHandler("clear",   clear_command))
    app.add_handler(CommandHandler("status",  status_command))
    app.add_handler(CommandHandler("help",    help_command))

    # Inline Buttons
    app.add_handler(CallbackQueryHandler(button_handler))

    # Free text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot polling shuru ho gaya...")
    app.run_polling(drop_pending_updates=True)

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))

    # Bot ko alag thread mein chalao
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

    # Flask web server
    print(f"🌐 Flask server port {PORT} par chal raha hai...")
    flask_app.run(host="0.0.0.0", port=PORT)
