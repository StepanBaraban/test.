import telebot
import random
from bot_logic import gen_pass

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("token")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я бот который поможет тебе узнать что лучше делать с предметами которые вам не нужны\
""")
choice = random.randint(1,2)
ar =['Вот несколько идей для поделок из бытового пластика:1. Кашпо для растений: Используйте пластиковые бутылки, обрезав их и украсив красками или тканью. Можно сделать подвесные кашпо, прикрепив веревки.2. Органайзер для канцелярии: Сложите несколько пластиковых контейнеров вместе и украсьте их, чтобы создать органайзер для ручек, карандашей.3. Подставка для телефона: Изогните пластиковую бутылку или используйте крышки от бутылок, чтобы создать подставку для телефона.4. Светильник: Сделайте светильник из пластиковых бутылок, вырезав узоры на стенках и вставив внутрь LED-лампочку.5. Игрушки для детей: Изготавливайте простые игрушки, такие как машинки из крышек или куклы из бутылок.6. Плетеные корзинки: Нарежьте пластиковые пакеты на полоски и сплетите их в корзинки или другие формы.7. Декор для сада: Используйте пластиковые бутылки, чтобы создать фигурки животных или цветы для украшения сада.8. Мозаика: Нарежьте пластиковые крышки на мелкие кусочки и используйте их для создания мозаичных картин или панно.10. Кормушка для птиц: Превратите пластиковую бутылку в кормушку, сделав отверстия для семян и подвесив ее на дереве.']






er =['Также ты наверное видел что есть корзины для мусора с надписями пластик и.т.д  так вот если например в корзину где написано пластик выкинуть пластиковый стакан потом его переработают и он снова станет полезным для чего нибудь . Если же ты просто выкинишь что нибудь например телефон то он будет разлагатся 100 лет']



@bot.message_handler(commands=['ecology'])
def send_ecology(message):
    if choice == 1:
        bot.reply_to(message, ar)
    elif choice == 2:
        bot.reply_to(message, er)
bot.polling()
