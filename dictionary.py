import telebot
import json


bot = telebot.TeleBot('5593178492:AAEU7jndyMi7nLeHHSP43ikFxUeRZLWy2eI')

class User:
    id = 0
    first_name = ""
    text_message = ""

    def __init__(self, id, first_name, text_message):
        self.id = id
        self.first_name = first_name
        self.text_message = text_message

    def get_user_data(self):
        return "ID is: {0} " \
               "first name is: {1}, " \
               "Message is: {2} \n".format(self.id,self.first_name, self.text_message)


def log(message, answer):
    print("\n ------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))

def get_info_user(message):
    u = User(message.from_user.id, message.from_user.first_name, message.text)

    file = open('SubUser.txt', 'a')
    file.write(u.get_user_data())
    file.close()


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать в словарь для начинающего программиста! '
                                           'Введи интересующее тебя слово и я '
                                           'постараюсь его найти.')
    get_info_user(message)


@bot.message_handler(commands=["stop"])

def handle_stop(message):
    bot.send_message(message.from_user.id, 'пока')
    get_info_user(message)
    bot.stop_polling()




@bot.message_handler(content_types=["text"])

def search_in_dict(message):
    file = open("try_unicode.json", "r")
    result = json.load(file)
    answer = "Извините, я еще не научился отвечать на такие сообщения"
    flag = False

    for i in result:
            if i['Rus'] == message.text:
                bot.send_message(message.chat.id, i['Eng']+"; "+i['Definition'])
                flag = True
            if i['Eng'] == message.text:
                bot.send_message(message.chat.id, i['Rus']+"; "+i['Definition'])
                flag = True

    if flag == False:
        bot.send_message(message.chat.id, answer)

    log(message, answer)
    get_info(message)
    get_info_user(message)
    file.close()


def get_info(message):

    from datetime import datetime
    f = open('users.json', 'a')
    f.write("\n Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                     datetime.now(),
                                                                   str(message.from_user.id),
                                                                     message.text))
    f.close()




bot.polling(none_stop=True, interval=0)
