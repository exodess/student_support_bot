
from ctypes.wintypes import HTASK
from gc import callbacks
from os import execle
from os.path import exists
import asyncio
from aiogram import F, Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from pymysql import connect

from botinfo import TOKEN
import emoji
from database import *
from aiogram.types import Message, CallbackQuery
from keyboards import (keyboard_after_start, keyboard_directions,
                       keyboard_to_start, keyboard_need_help, keyboard_return_to_need_help, keyboard_to_directions,
                       keyboard_if_user_already_registration, button_url, keyboard_start, keyboard_for_need_help,
                       keyboard_for_need_help_1, deadline_buttons)


dct_desire = dict()
dct_need = dict()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dict_para = dict()
dict_message_last_id = dict()

@dp.message(F.text == '/start')
async def send_start(message:Message):
    execute_query(connection, create_seekshelp_table)
    user_name = message.from_user.username
    user_id = message.from_user.id
    exists_text = ''
    admins = ''
    if not exists_user(connection, user_name, NAME_TB_ADMINS):
        print("Зашел админ")
        admins += "Приветствую вас, админ!\n"
    if not exists_user(connection, user_name, NAME_TB_SEEKSHELP):
        print("Такой пользователь уже есть")
        exists_text += 'Кстати, вы уже раньше общались со мной, предлагаю продолжить наш разговор'
    else :
        print("Новый пользователь запустил бота")
        add_users_seeks(connection, user_name, user_id)
    await message.answer(text= admins + f'Здарова {emoji.emojize(":hand_with_fingers_splayed:")}\nЯ бот, который выстраивает сеть взаимопомощи между студентами КАИ\n' + exists_text, reply_markup=keyboard_after_start)

@dp.callback_query(F.data.in_({'start', 'button_return_to_desire_help_pressed', 'button_return_to_start_pressed'}))
async def send_menu(callback:CallbackQuery):
    await callback.message.edit_text(text=f'Выбери нужное тебе из этого меню', reply_markup=keyboard_after_start)


# НАЧАЛО
@dp.callback_query(F.data == 'button_the_desire_to_help_pressed') # хочу помочь
@dp.callback_query(F.data == 'button_return_to_directions') # вернуться назад (после хочу помочь)
async def pressed_desire_to_help(callback:CallbackQuery):
    dct_desire[callback.from_user.id] = False
    #Проверка на нахождение user в бд
    #если нет то он проходит регистрацию
    #если есть пишет: вы хотите поменять данные о себе? и все тоже самое
    s = ''
    if exists_user(connection, callback.from_user.username, NAME_TB_OFFERSHELP):
        s += 'Ваши данные частично сохранены\n'
    await callback.message.edit_text(text= s + '<u>Выберите сферу(-ы) деятельности, в которой(-ых) вы могли бы кому-нибудь помочь</u>', reply_markup=keyboard_directions)


# создание администратора (потом уберу)
@dp.message(F.text == '/admin')
async def to_admin(message: Message):
    user_name = message.from_user.username
    if exists_user(connection, user_name, NAME_TB_ADMINS):
        add_admins(connection, user_name)
        await bot.send_message(message.from_user.id, "Вы теперь новый админ!")
        print("Новый админ")
    else:
        print("Такой админ уже есть")
        await bot.send_message(message.from_user.id, "Вы уже и так являетесь админом, займитесь делами")




# НАЧАЛО -> Хочу кому-то помочь ->
@dp.callback_query(F.data.in_({'button_directions_1_pressed', 'button_directions_2_pressed'})) # кнопки учеба и труд деятельность
async def put_in_bd(callback:CallbackQuery):
    username = callback.from_user.username
    userid = callback.from_user.id
    s = ''
    if callback.data == 'button_directions_1_pressed' and '1' not in s:
        s += '1'
    if callback.data == 'button_directions_2_pressed' and '2' not in s:
        s += '2'
    dct_desire[callback.from_user.id] = (s != '')
    await callback.answer(text='Данные сохранились в базу данных', show_alert=True)
    print(username)
    if exists_user(connection, username, NAME_TB_OFFERSHELP):
        add_spheres_in_bd(connection, username, userid, s, NAME_TB_OFFERSHELP)
    else:
        update_spheres_in_bd(connection, username, s, NAME_TB_OFFERSHELP)
# НАЧАЛО -> Вам нужна помощь? -> С чем нужна помощь? -> Краткое описание проблемы -> Дедлайн
# @dp.callback_query(F.data.in_({button_to_deadline}))


# НАЧАЛО -> Хочу помочь -> Выбор сферы ->
@dp.callback_query(F.data == 'button_next_pressed')
async def describing(callback:CallbackQuery):
    if callback.from_user.id in dct_desire and dct_desire[callback.from_user.id]:
        await callback.message.edit_text(text='Кратко опишите себя', reply_markup=keyboard_to_directions)
    else:
        await callback.answer(text='Вы должны выбрать что-то из специальностей', show_alert=True)



@dp.callback_query(F.data == 'button_need_help_pressed')
@dp.callback_query(F.data == 'button_return_to_need_help_pressed')
async def send_need_help(callback:CallbackQuery):
    dct_need[callback.from_user.id] = False
    await callback.message.edit_text(text='С чем нужна помощь?', reply_markup=keyboard_need_help)



# НАЧАЛО -> нужна помощь -> в каких сферах нужна помощь?
@dp.callback_query(F.data.in_({'button_need_help_1_pressed', 'button_need_help_2_pressed',
                               'button_need_help_3_pressed', 'button_need_help_4_pressed'}))
async def get_describe_need_help(callback:CallbackQuery):
    result = ''
    username = callback.from_user.username
    userid = callback.from_user.id
    if callback.data == 'button_need_help_1_pressed':
        result += '1'
    elif callback.data == 'button_need_help_2_pressed':
        result += '2'
    elif callback.data == 'button_need_help_3_pressed':
        result += '3'
    elif callback.data == 'button_need_help_4_pressed':
        result += '4'
    dct_need[callback.from_user.id] = result
    if not exists_user(connection, username, NAME_TB_SEEKSHELP):
        update_spheres_in_bd(connection, username, result, NAME_TB_SEEKSHELP)
    else:
        add_spheres_in_bd(connection, username, userid, result, NAME_TB_SEEKSHELP)
    await callback.message.edit_text(text='Кратко опишите, что нужно сделать, чтобы вам помочь?',
                                     reply_markup=keyboard_return_to_need_help)

@dp.message(F.text == '/ready')
async def offers_ready(message: Message):
    print(dict_para)
    id_offers = dict_para[f'{message.from_user.id}']
    if message.from_user.id in dict_para:
        del dict_para[f'{message.from_user.id}']
    print(id_offers)
    await bot.send_message(int(id_offers), "Спасибо за успешно выполненное задание!\nВам начисленно 20 баллов")
    sql_offers = f"UPDATE {NAME_TB_OFFERSHELP} SET `points` = points + 20 WHERE `id` = {id_offers};"
    execute_query(connection, sql_offers)
    sql_status = f"UPDATE {NAME_TB_OFFERSHELP} SET `status` = 1 WHERE `id` = {id_offers}"
    execute_query(connection, sql_status)
    await bot.send_message(message.from_user.id, "Ваше задание было выполнено!")

#Сохраняем описание в бд если регистрация
#если нужна помощь то
@dp.message(F.text)
async def get_describe(message:Message):
    username = message.from_user.username
    description = message.text
    if message.from_user.id in dct_desire and dct_desire[message.from_user.id]:
        # написать функцию, записывающую описание человека в бд   s и description
        # Также сохранить username и id
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass
        add_description_in_bd(connection, username, description, NAME_TB_OFFERSHELP)
        await message.answer(text='Вы прошли регистрацию.\nТеперь можете пользоваться ботом\nсо спокойной душой,'
                                  '\nтак как вы теперь его пользователь.',
                                reply_markup=keyboard_start)
    elif message.from_user.id in dct_need and dct_need[message.from_user.id]:
        #для тех кому нужна помощь
        #функция которая записывает специальность и описание кому нужна помощь
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass
        add_description_in_bd(connection, username, description, NAME_TB_SEEKSHELP)
        await bot.send_message(message.from_user.id, 'Отлично!\nНаконец, выберите, в течении какого времени вам нужно помочь:', reply_markup=deadline_buttons)
    dct_desire[message.from_user.id] = False
    dct_need[message.from_user.id] = False


# дедлайн
@dp.callback_query(F.data.in_({'3hours', '12hours',
                               '1day', '2days',  '3days'}))
async def get_deadline_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    deadline = callback.data
    add_deadline_in_bd(connection, username, deadline)
    await callback.message.edit_text(text="Мы записали вашу проблему, скоро я подберу вам человека, который ее решит", reply_markup=keyboard_start)
    sql_sphere = f"SELECT spheres from {NAME_TB_SEEKSHELP} WHERE username='{username}'"
    sphere = execute_read_query(connection, sql_sphere)[0]["spheres"]
    sql_description = f"SELECT short_description from {NAME_TB_SEEKSHELP} WHERE username='{username}'"
    task_description = execute_read_query(connection, sql_description)[0]["short_description"]
    await mailing_users(user_id, sphere, task_description, deadline)

# -------------------------------------------------------------------------------

# ПОСЛЕ РЕГИСТРАЦИИ -> принятие или отказ от задания
async def mailing_users(id_seeks, sphere, task_description, deadline):
 #рассылка первым 10 челам по рейтингу
    sql = f"SELECT id FROM {NAME_TB_OFFERSHELP} WHERE status = '1' && spheres = '{sphere}' ORDER BY rating DESC"
    ids = execute_read_query(connection, sql)
    with open('text.txt', 'w+') as f:
        f.write(f"{id_seeks}")
    for idu in ids:
        await bot.send_message(chat_id=int(idu["id"]), text=f"Для вас есть работа!\n Задача: {task_description}\n Дедлайн: {deadline}", reply_markup=keyboard_for_need_help)

#функция если человек, который хотел помогать, согласится помочь
@dp.callback_query(F.data == 'btn_accept')
async def accept(callback:CallbackQuery):
    id_offers = callback.from_user.id
    with open('text.txt', 'r') as f:
        id_seeks = f.readline()
        f.close()
    with open('text.txt', 'w+') as f:
        f.write(f"{id_offers}")
    sql = f"SELECT * FROM offers_help WHERE id='{id_offers}'"
    info = execute_read_query(connection, sql)
    rating = info[0]["rating"]
    skills = info[0]["short_description"]
    dict_message_last_id[f'{callback.from_user.id}'] = callback.message.message_id
    print(dict_message_last_id)
    await bot.send_message(chat_id= id_seeks, text=f"\nНа вашу заявку откликнулся: @{callback.from_user.username}\n\nРейтинг: {rating}\nСкиллы: {skills}", reply_markup=keyboard_for_need_help_1)


#функция если человек, который хотел помогать, отказался помогать
@dp.callback_query(F.data=='btn_disagree')
async def delete_mess(callback:CallbackQuery):
    await callback.message.edit_text(text='Хорошо, вы не захотели помогать этому студенту, но я надеюсь, что в следующий раз ты поможешь своему товарищу!')


#функция если тот кто нуждается в помощи принял помощь из представляемых ему кандидатов
@dp.callback_query(F.data=='btn_accept_1')
async def the_application_accepted(callback:CallbackQuery):
    id_seeks = callback.from_user.id
    with open("text.txt", "r") as f:
        id_offers = f.readline()
    ####здесь функция которая ставит помогающему челу   status = False -занят
    sql = f"UPDATE `{NAME_TB_OFFERSHELP}` SET `status` = 0 WHERE `id` = {id_offers}"
    execute_query(connection, sql)
    dict_para[f"{id_seeks}"] = id_offers
    print(dict_para)
    await callback.message.edit_text(text=f'<b>Заявка принята</b>\n{callback.message.text}')
    await bot.edit_message_text(chat_id=id_offers, message_id=dict_message_last_id[f"{id_offers}"], text=f'Ваша кандидатура принята. Постарайтесь выполнить работу до дедлайна\nЕсли у вас есть вопросы, пишите ему(ей) @{callback.from_user.username}')


@dp.callback_query(F.data=='btn_disagree1')
async def delete_mess(callback:CallbackQuery):
    with open("text.txt", "r") as f:
        id_offers = f.readline()
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await bot.send_message(id_offers, "К сожалению, этот студент не захотел, чтобы вы выполнили его задачу")


if __name__ == '__main__':
    dp.run_polling(bot)

