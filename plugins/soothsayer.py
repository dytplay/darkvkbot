# -*- coding: utf-8 -*-

import random

from plugin_system import Plugin

plugin = Plugin('Ответы на вопросы',
                usage=['шар [строка] - вероятность того, что высказывание правдиво'])

# Инициализируем возможные ответы
answers = '''Абсолютно точно!
Да.
Нет.
Скорее да, чем нет.
Не уверен...
Однозначно нет!
Если ты не фанат аниме, у тебя все получится!
Можешь быть уверен в этом.
Перспективы не очень хорошие.
А как же иначе?.
Да, но если только ты не смотришь аниме.
Знаки говорят — «да».
Не знаю.
Мой ответ — «нет».
Весьма сомнительно.
Не могу дать точный ответ.
'''.splitlines()


@plugin.on_command('Вопрос', 'вопрос')
async def tell_truth(msg, args):
    await msg.answer("Бот говорит" + random.choice(answers))
