from core.app import app

TOKEN = "7061932990:AAEsXWz3_sFmfJheER39JJGrSCXQUjR-gR8"
# proxy = 'socks5://127.0.0.1:2080'

bot = app(TOKEN=TOKEN)

if __name__ == "__main__":
    bot.start()