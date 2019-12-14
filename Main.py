from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup
apiToken = '955780479:AAGrgKDPiRQtI9YExK7Q0NPCUX_FJYimSYk'

bot = Bot(token=apiToken)
dp = Dispatcher(bot)

#Главное меню
user_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_menu_markup.row('Windows', 'Linux', 'MacOs')



#Функция логирования сообщений
async def log(message, answer):
    print(datetime.now)
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3} \n ID Сообщение: {4} \n".format(message.from_user.first_name,
                                                                                        message.from_user.username,
                                                                                        message.from_user.id,
                                                                                        message.text,
                                                                                        message.message_id))



#Функция которая реагирует на слово привет отвечая 'Привет собака'
@dp.message_handler(content_types=['text'])
async def answers(message: types.Message):

    #Реакция 1
    if message.text == 'Привет':
        answer = 'Привет Собака'
        await log(message,answers)
        await bot.send_message(message.chat.id, answer)

     #Реакция 2
    if message.text == 'Как дела?':
        await bot.send_message(message.chat.id, 'Жить можно')

    if message.text == 'Покажи меню':
        await  bot.send_message(message.from_user.id, 'Открываю меню...', reply_markup=user_menu_markup)




#Ответ на неизвестные сообщения
@dp.message_handler()
async def random_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'че тебе надо?')



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
