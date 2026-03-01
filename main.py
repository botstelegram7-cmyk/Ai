import os
import asyncio
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

# ─── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)

# ─── Flask App ────────────────────────────────────────────────────────────────
flask_app = Flask(__name__)

@flask_app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "Grok AI Telegram Bot is Running 🤖"})

@flask_app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# ─── Bot Runner (async, apna event loop) ─────────────────────────────────────
async def run_bot_async():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",   start_command))
    app.add_handler(CommandHandler("ask",     ask_command))
    app.add_handler(CommandHandler("imagine", imagine_command))
    app.add_handler(CommandHandler("clear",   clear_command))
    app.add_handler(CommandHandler("status",  status_command))
    app.add_handler(CommandHandler("help",    help_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot polling shuru ho gaya...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)

    # Infinite wait — bot chalata rahe
    await asyncio.Event().wait()

def run_bot_in_thread():
    """Thread ke andar fresh event loop banao"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(run_bot_async())
    except Exception as e:
        print(f"❌ Bot thread error: {e}")
    finally:
        loop.close()

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))

    bot_thread = threading.Thread(target=run_bot_in_thread, daemon=True)
    bot_thread.start()

    print(f"🌐 Flask server port {PORT} par chal raha hai...")
    flask_app.run(host="0.0.0.0", port=PORT)
