import telebot
from sqlighter import SQLighter
import os
bot = telebot.TeleBot(str(os.environ.get('BOT_TOKEN')))
from telebot import types  # кнопки


def get_db_value(x):
    return x[0][0]


def main():
    db = SQLighter('user.db')  # подключаемся к базе данных

    @bot.message_handler(commands=['start'])
    def send_welcome(message):

        if not db.subscriber_exists(message.from_user.id):
            # если юзера нет в базе, добавляем его
            db.add_subscriber(message.from_user.id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('5')
        itembtn2 = types.KeyboardButton('4')

        markup.add(itembtn1, itembtn2)
        msg = bot.send_message(message.chat.id, "Здравствуйте "
                               + message.from_user.first_name
                               + ", я бот, напишите какую вы хотите оценку, чтобы вычеслить, сколько вам нужно оценок для повышения среднего балла?",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, какой_балл)

    def какой_балл(message):

        if not db.subscriber_exists(message.from_user.id):
            # если юзера нет в базе, добавляем его
            db.add_subscriber(message.from_user.id)
        db.update_ball(message.chat.id, message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        msg = bot.send_message(message.chat.id, "Сколько "
                               + message.from_user.first_name
                               + ", пятёрок?",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, пятёрок)

    def пятёрок(message):
        db.update_5(message.from_user.id, message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        msg = bot.send_message(message.chat.id, "Сколько у вас "
                               + message.from_user.first_name
                               + ", четвёрок?",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, четвёрок)

    def четвёрок(message):
        db.update_4(message.from_user.id, message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        msg = bot.send_message(message.chat.id, "Сколько у вас "
                               + message.from_user.first_name
                               + ", троек?",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, троек)

    def троек(message):
        db.update_3(message.from_user.id, message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        msg = bot.send_message(message.chat.id, "Сколько у вас "
                               + message.from_user.first_name
                               + ", двоек?",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, двоек)

    def двоек(message):
        db.update_2(message.from_user.id, message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        msg = bot.send_message(message.chat.id, "Идёт подсчёт...",
                               reply_markup=markup)
        сумма_оценок = (get_db_value(db.get_5(message.chat.id)) * 5) + (get_db_value(db.get_4(message.chat.id)) * 4) + (
                    get_db_value(db.get_3(message.chat.id)) * 3) + (get_db_value(db.get_2(message.chat.id)) * 2)
        количество_оценок = get_db_value(db.get_5(message.chat.id)) + get_db_value(
            db.get_4(message.chat.id)) + get_db_value(db.get_3(message.chat.id)) + get_db_value(
            db.get_2(message.chat.id))
        print(db.get_3(message.chat.id))
        средний_балл = сумма_оценок / количество_оценок


        if get_db_value(db.get_ball(message.chat.id)) == 5:
            i = 0
            while средний_балл < 4.5:
                i = i + 1

                количество_оценок = количество_оценок + 1

                сумма_оценок = сумма_оценок + 5

                средний_балл = сумма_оценок / количество_оценок

            bot.send_message(message.chat.id, f"Вам надо получить пятёрок: {i} будет балл: {средний_балл}")


        elif get_db_value(db.get_ball(message.chat.id)) == 4:
            i = 0
            while средний_балл < 3.5:
                i = i + 1

                количество_оценок = количество_оценок + 1

                сумма_оценок = сумма_оценок + 4

                средний_балл = сумма_оценок/количество_оценок

            bot.send_message(message.chat.id, f"Вам надо получить четвёрок: {i}  будет балл:  {средний_балл}")


if __name__ == '__main__':
    main()
    bot.polling(none_stop=True)
