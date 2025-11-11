# 🎟️ Support Bot

> Full-featured Telegram bot for ticket management, feedback collection, and customer support automation

![Version](https://img.shields.io/badge/version-2.5.8-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## 📋 Description

**Support Bot** is a scalable ticket management system via Telegram that enables:

✅ Users to quickly create tickets without bureaucracy  
✅ Administrators to manage all tickets from a single interface  
✅ Feedback collection and support quality tracking  
✅ Automation of routine operations  
✅ **Automatic ticket closure when users don't respond** 🆕

---

## 🚀 Key Features

### 👤 For Users

| Feature | Description |
|---------|-------------|
| 📨 **Create Tickets** | Quick ticket creation with problem description |
| 💬 **Feedback & Suggestions** | Send service quality feedback |
| ⭐ **Quality Rating** | Rate support (1-3 stars) |
| 🌐 **Multi-language Support** | Russian and English support |
| ⏱️ **Spam Protection** | Cooldown system between tickets |
| 🔔 **Auto-close Notifications** | Get notified when ticket closes automatically 🆕 |

### 👨‍💼 For Administrators

| Feature | Description |
|---------|-------------|
| 📋 **Admin Panel** | Manage all incoming tickets |
| 💬 **Direct Replies** | Communicate directly with users |
| 🔄 **Status Management** | Transitions: new → in progress → closed |
| 🚫 **User Blocking System** | Block/unblock users |
| 💾 **Automatic Backups** | Data backup and recovery |
| 📊 **Statistics** | View metrics and analytics |
| 📢 **Notifications** | Alerts for new tickets |
| ⏰ **Auto-close Tickets** | Automatically close inactive tickets 🆕 |

---

## 🔧 Tech Stack

- **Language:** Python 3.11+
- **Framework:** python-telegram-bot 21+
- **Database:** JSON (embedded)
- **Containerization:** Docker & Docker Compose
- **Localization:** i18n (Russian/English)
- **Scheduler:** Async job scheduler for automation

---

## 📦 Requirements

- Docker and Docker Compose
- Python 3.11+ (for local run)
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Telegram User ID of administrator

---

## 🚀 Quick Start

### 1️⃣ Clone Repository

git clone https://github.com/JuraZZik/bot_support.git
cd bot_support


### 2️⃣ Configuration

Create `.env` file:

🔴 MANDATORY!
BOT_TOKEN=
ADMIN_ID=
DEFAULT_LOCALE=

📋 RECOMMENDED (for notifications)
ALERT_CHAT_ID=
ALERT_TOPIC_ID=
START_ALERT=
SHUTDOWN_ALERT=
TIMEZONE=

⏰ AUTO-CLOSE SETTINGS (optional)
AUTO_CLOSE_AFTER_HOURS=
BOT_TOKEN=
ADMIN_ID=
DEFAULT_LOCALE=

📋 RECOMMENDED (for notifications)
ALERT_CHAT_ID=
ALERT_TOPIC_ID=
START_ALERT=
SHUTDOWN_ALERT=
TIMEZONE=

⏰ AUTO-CLOSE SETTINGS (optional)
AUTO_CLOSE_AFTER_HOURS=


**Where to find:**

| Parameter | Where to find |
|-----------|--------------|
| `BOT_TOKEN` | `@BotFather` → `/newbot` |
| `ADMIN_ID` | Send `/id` to bot, get your ID |
| `ALERT_CHAT_ID` | Group ID (send message in debug) |
| `DEFAULT_LOCALE` | `ru` (Russian) or `en` (English) |
| `AUTO_CLOSE_AFTER_HOURS` | Hours to wait before auto-closing ticket (default: 24) |

### 3️⃣ Run with Docker

docker compose up -d


### 4️⃣ Local Run

Install dependencies
pip install -r requirements.txt

Run bot
python main.py


---

## 📚 Usage

### For User:

1. Write `/start` to bot
2. Choose needed menu item
3. Create tickets, send feedback, rate quality
4. Respond to support replies to keep ticket active

### For Administrator:

1. Open **Inbox** – view all tickets
2. Press **Take in progress** – start working with ticket
3. Press **Reply** – send reply to user
4. Press **Close** – finish ticket
5. Check **Statistics** – work analytics
6. Monitor auto-closed tickets via notifications

---

## ⏰ Auto-Close Tickets Feature

### How It Works

The bot automatically closes tickets when users don't respond after admin replies:

1. **Admin replies** to user ticket
2. **User doesn't respond** within configured timeout (default: 24 hours)
3. **Ticket closes automatically**
4. **Notifications sent** to both admin and user in their languages

### Key Features

- ✅ Only closes tickets where **admin sent last message**
- ✅ Doesn't close tickets where **user is waiting for admin reply**
- ✅ **Hourly checks** for inactive tickets
- ✅ **Localized notifications** for admin and user
- ✅ **Configurable timeout** via environment variable

### Configuration

Set timeout in hours (default: 24)
AUTO_CLOSE_AFTER_HOURS=24



### Examples

**Scenario 1: Ticket closes automatically**
12:00 - User creates ticket (last_actor: user)
12:30 - Admin replies (last_actor: support)
36:30 - Check runs: No user response for 24h → CLOSE ✅


**Scenario 2: Ticket stays open**
12:00 - User creates ticket (last_actor: user)
12:30 - Admin replies (last_actor: support)
13:00 - User replies (last_actor: user)
37:00 - Check runs: User waiting for reply → KEEP OPEN ❌


---

## 🗂️ Project Structure

bot_support/
├── main.py # Entry point
├── config.py # Configuration
├── requirements.txt # Dependencies
├── docker-compose.yml # Docker config
├── .env.example # Example .env
├── handlers/ # Command handlers
├── services/ # Services
│ ├── tickets.py # Ticket management
│ ├── ticket_auto_close.py # Auto-close logic 🆕
│ ├── feedback.py # Feedback system
│ ├── scheduler.py # Job scheduler
│ └── alerts.py # Notifications
├── storage/ # Data management
├── locales/ # Localization (ru, en)
├── utils/ # Helper functions
└── bot_data/ # Data (created automatically)
├── data.json # Main data
├── banned.json # Ban list
├── bot.log # Logs
└── backups/ # Backups


---

## 🛠️ Additional Configuration

### Backups

BACKUP_ENABLED=
BACKUP_FULL_PROJECT=
BACKUP_SEND_TO_TELEGRAM=
BACKUP_MAX_SIZE_MB=
BACKUP_ENABLED=
BACKUP_FULL_PROJECT=
BACKUP_SEND_TO_TELEGRAM=
BACKUP_MAX_SIZE_MB=


### Spam Protection

FEEDBACK_COOLDOWN_ENABLED=
FEEDBACK_COOLDOWN_HOURS=
ASK_MIN_LENGTH=
FEEDBACK_COOLDOWN_ENABLED=
FEEDBACK_COOLDOWN_HOURS=
ASK_MIN_LENGTH=


### Auto-Close Settings

Enable auto-close (always enabled, timeout configurable)
AUTO_CLOSE_AFTER_HOURS=24 # Hours to wait for user response


### Error Notifications

ERROR_ALERTS_ENABLED=
ERROR_ALERT_THROTTLE_SEC=
ERROR_ALERTS_ENABLED=
ERROR_ALERT_THROTTLE_SEC=


### Detailed Documentation

See `.env` file for all available options.

---

## 📊 API Endpoints

Bot works through Telegram Bot API. No public REST endpoints.

---

## 🤝 Contributing

Suggestions, feedback, and bug reports are welcome!

Write to me:
- 🐛 About bugs
- 💡 About ideas
- ✨ About features

---

## 📝 License

MIT License – free for personal and commercial use.

---

## 👨‍💻 Author

**JuraZZik**

- Telegram: [@JuraZZik](https://t.me/JuraZZik)
- Bot: [@JuraZZik_SupportBot](https://t.me/JuraZZik_SupportBot)
- GitHub: [github.com/JuraZZik](https://github.com/JuraZZik)

---

## 📈 Versioning

| Version | Date       | Description                                     |
| ------- | ---------- | ----------------------------------------------  |
| 2.5.8   | 2025-11-11 | 🆕 Latest version update                        |
| 2.5.1   | 2025-11-08 | ⏰ Complete auto-close tickets implementation🆕 |
| 2.5.0   | 2025-11-07 | 🔧 Fixed localization and feedback system       |
| 2.4.1   | 2025-11-06 | ✨ Stable version with multi-language support   |
| 2.3.9   | 2025-10-29 | 🎉 First release                                |

>>>>>>> 50f37a4 (Update README.md)

## 📋 Changelog

### [2.5.1] - 2025-11-08

#### Added
- ⏰ Automatic ticket closure when user doesn't respond after admin reply
- 🔔 Localized notifications for auto-closed tickets (admin & user)
- 📊 Last actor tracking (user/support) for better ticket lifecycle management
- ⚙️ Configurable timeout via `AUTO_CLOSE_AFTER_HOURS` environment variable

#### Changed
- 🔄 Improved `last_actor` update logic when admin takes ticket
- 📅 Scheduler now runs hourly checks for inactive tickets

#### Fixed
- ✅ Completed auto-close functionality with proper scheduler registration
- 🎯 Only closes tickets where admin sent last message (not user-waiting tickets)

---

## ⭐ Support

If you like the project – give it a star! ⭐


  ⭐
 ⭐⭐
⭐⭐⭐


---

**Thank you for using Support Bot!** 🎉
