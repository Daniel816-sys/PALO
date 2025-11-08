from config import TOKEN
from logic import gen_pass
import telebot
import random    

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['password'])
def random_password(message):
    bot.send_message(message.chat.id, str(gen_pass(10)))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_bye(message):
    words = message.text.split()
    if len(words) == 2:
        result = gen_pass(int(words[1]))
    else:
        result = gen_pass(8)
    bot.reply_to(message, f"Ваш пароль : {result}")

# NEW: Подбрасывание монетки
@bot.message_handler(commands=['coin'])
def coin_flip(message):
    result = random.choice(["Орёл 🦅", "Решка 🪙"])
    bot.reply_to(message, f"Монетка показала: {result}")

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
