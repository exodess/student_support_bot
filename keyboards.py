from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji
from config import URL_WITHOUT_UN

with open('users.txt', 'r') as k:
    a = k.readline()

button_start = InlineKeyboardButton(text='start', callback_data='start')
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[[button_start]])

button_url = InlineKeyboardButton(text='Переход на наш сайт', url=URL_WITHOUT_UN + str(a))
button_the_desire_to_help = InlineKeyboardButton(text='Хочу кому-то помочь', callback_data='button_the_desire_to_help_pressed')
button_need_help = InlineKeyboardButton(text='Мне нужна помощь', callback_data='button_need_help_pressed')
keyboard_after_start = InlineKeyboardMarkup(inline_keyboard=[[button_need_help],
                                                             [button_the_desire_to_help], [button_url]])

button_desire_help_describe = InlineKeyboardButton(text='Напишите ваше описание, что вы умеете',
                                                   callback_data='button_desire_help_describe_pressed')
button_return_to_start = InlineKeyboardButton(text='Вернуться в начало', callback_data='button_return_to_start_pressed')
keyboard_to_start = InlineKeyboardMarkup(inline_keyboard=[[button_return_to_start]])

# кнопка для возврата назад после кнопки "Хочу помочь"
button_return_to_direction = InlineKeyboardButton(text='Вернуться назад', callback_data='button_return_to_directions')
keyboard_to_directions = InlineKeyboardMarkup(inline_keyboard=[[button_return_to_direction]])



button_next = InlineKeyboardButton(text='Следующий шаг', callback_data='button_next_pressed')
button_directions_1 = InlineKeyboardButton(text='Учёба', callback_data='button_directions_1_pressed')
button_directions_2 = InlineKeyboardButton(text='Трудовая деятельность', callback_data='button_directions_2_pressed')
button_return_to_desire_help = InlineKeyboardButton(text='Вернуться назад', callback_data='button_return_to_desire_help_pressed')
keyboard_directions = InlineKeyboardMarkup(inline_keyboard=[[button_directions_1],
                                                            [button_directions_2],
                                                            [button_next],
                                                            [button_return_to_desire_help]])

# Принятие или отказ от задачи




button_need_help_1 = InlineKeyboardButton(text=f'{emoji.emojize(":heart_on_fire:")}  Учёба  '
                                               f'{emoji.emojize(":heart_on_fire:")}', callback_data='button_need_help_1_pressed')
button_need_help_2 = InlineKeyboardButton(text='Организация чего-либо', callback_data='button_need_help_2_pressed')
button_need_help_3 = InlineKeyboardButton(text=f'{emoji.emojize(":flexed_biceps:")}  Трудовая помощь  '
                                               f'{emoji.emojize(":flexed_biceps:")}', callback_data='button_need_help_3_pressed')
button_need_help_4 = InlineKeyboardButton(text='Другая помощь', callback_data='button_need_help_4_pressed')
keyboard_need_help = InlineKeyboardMarkup(inline_keyboard=[[button_need_help_1],
                                                           [button_need_help_2],
                                                           [button_need_help_3],
                                                           [button_need_help_4],
                                                           [button_return_to_start]])


button_return_to_need_help = InlineKeyboardButton(text='Вернуться назад', callback_data='button_return_to_need_help_pressed')
keyboard_return_to_need_help = InlineKeyboardMarkup(inline_keyboard=[[button_return_to_need_help]])


button_change_acc = InlineKeyboardButton(text='Изменить свои данные аккаунта', callback_data='button_change_acc')
keyboard_if_user_already_registration = InlineKeyboardMarkup(inline_keyboard=[[button_need_help],
                                                                              [button_change_acc]])

# Для указания дедлайна
dl1 = InlineKeyboardButton(text="3 часа", callback_data='3hours')
dl2 = InlineKeyboardButton(text="12 часов", callback_data="12hours")
dl3 = InlineKeyboardButton(text="1 день", callback_data="1day")
dl4 = InlineKeyboardButton(text="2 дня", callback_data="2days")
dl5 = InlineKeyboardButton(text="3 дня", callback_data="3days")
deadline_buttons = InlineKeyboardMarkup(inline_keyboard=[[dl1, dl2, dl3, dl4, dl5]])

# для принятия и отказа заявок
btn_accept = InlineKeyboardButton(text='Принять', callback_data='btn_accept')
btn_disagree = InlineKeyboardButton(text='Отказаться', callback_data='btn_disagree')
btn_accept_1 = InlineKeyboardButton(text='Принять', callback_data='btn_accept_1')
btn_disagree_1 = InlineKeyboardButton(text='Отказаться', callback_data='btn_disagree_1')
keyboard_for_need_help_1 = InlineKeyboardMarkup(inline_keyboard=[[btn_accept_1, btn_disagree_1]])
keyboard_for_need_help = InlineKeyboardMarkup(inline_keyboard=[[btn_accept, btn_disagree]])