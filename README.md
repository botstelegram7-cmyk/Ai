# 🤖 Grok AI Telegram Bot

**Owner:** @xuoqui_xin  
**AI Engine:** xAI Grok API  
**Stack:** Python · python-telegram-bot · Flask · Docker

---

## 📁 File Structure

```
├── bot.py              # Bot logic + Grok AI integration
├── main.py             # Flask server + Bot runner (entry point)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image config
├── docker-compose.yml  # Docker Compose config
├── .env.example        # ENV template (copy → .env)
└── README.md
```

---

## ⚙️ Setup

### 1. .env file banao

```bash
cp .env.example .env
```

Phir `.env` mein apni values bharo:

```env
BOT_TOKEN=your_telegram_bot_token
GROK_API_KEY=your_grok_api_key
OWNER_USERNAME=xuoqui_xin
GROK_MODEL=grok-3-latest
PORT=5000
```

---

## 🚀 Deploy Options

### Option A — Docker Compose (Recommended)

```bash
docker-compose up -d --build
```

Logs dekhne ke liye:
```bash
docker-compose logs -f
```

Stop karne ke liye:
```bash
docker-compose down
```

---

### Option B — Direct Docker

```bash
# Build
docker build -t grok-bot .

# Run
docker run -d \
  --name grok_bot \
  --restart always \
  -p 5000:5000 \
  --env-file .env \
  grok-bot
```

---

### Option C — Local Python

```bash
pip install -r requirements.txt
cp .env.example .env   # .env fill karo
python main.py
```

---

### Option D — Render / Railway / Fly.io

1. Repo push karo GitHub pe
2. ENV variables platform ke dashboard mein daalo
3. Start command: `python main.py`
4. Port: `5000`

---

## 🤖 Bot Commands

| Command | Description |
|---|---|
| `/start` | Bot start karo |
| `/ask <sawaal>` | Grok se kuch poochho |
| `/imagine <desc>` | Creative AI response |
| `/status` | Bot + Grok API status |
| `/clear` | Context clear karo |
| `/help` | Commands list |

> ⚠️ Sirf **@xuoqui_xin** ka message accept karega!

---

## 🌐 Flask Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Bot status check |
| `/health` | GET | Health check (for Docker/uptime monitors) |

---

## 🔑 Keys Kahan Se Milenge?

- **BOT_TOKEN** → [@BotFather](https://t.me/BotFather) se
- **GROK_API_KEY** → [console.x.ai](https://console.x.ai)
