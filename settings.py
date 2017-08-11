"""
Описание возможных значений:
False - нет, True - да
() - кортеж, заполняется элементами через запятую
'' - строка, само содержимое пишется между кавычками
"""

# Данные для авторизации бота
# Кортеж из одного элемента - токен группы
# Кортеж из 2х элементов - логин/ пароль пользователя
# Если в кортеже 1 элемент - запятая в конце обязательна!

# Если ввести несколько пользователей, методы, требующие пользователя будут выполняться по
# очереди от лица этих аккаунтов.

# Если ввести несколько токенов групп, метода, которые можно выполнить от лица группы
# Будут выполняться от лица этих групп.

# # # Не рекомендуется вводить токены разных групп
# # # Не рекомендуется вводить несколько пользователей, если не введена группа(т.к. бот будет отвечать
# # # по очереди от разных аккаунтов).
USERS = (
       #  ("a77c6f6968363d899839fff83860044f827e7d185ff4c648a01455cf23b3146138a553b26b6e33a48735e",),
         (),
)
# Прокси для подключения к VK API с помощью данных из USERS
PROXIES = (
        # ("ADDRESS", PORT, "USER", "PASSWORD"),
)

# Префиксы сообщений, с помощью которых бот будет понимать, что обращаются к нему.
PREFIXES = ('', )

# ID приложения, через которое бот будет авторизовываться
APP_ID = 5982451
# Максимальные права - https://vk.com/dev/permissions
SCOPE = 140489887
# Задержка между исполнением команд для одного пользователя. Антифлуд
# Рекомендуемое значение - 1 секунда
FLOOD_INTERVAL = 0

# Данные для базы данных PostgreSQL или MySQL
# DATABASE_SETTINGS = ("DATABASE NAME", "HOST", PORT, "USER", "PASSWORD")
DATABASE_SETTINGS = ("sql8189314","sql8.freesqldatabase.com",3306,"sql8189314","V4ji5Aiumd")
DATABASE_DRIVER = "mysql"  #  Может принимать значения: mysql, postgresql
DATABASE_CHARSET = 'utf8mb4'  # utf8mb4, latin1 и т.д.

# Является ли бот группой
IS_GROUP = True

# Нужно ли, чтобы бот болтал с пользователями, если они написали не команду
DO_CHAT = False
# Если True, бот будет только общаться с пользователем, без команд
ONLY_CHAT = False
# Если True - бот будет использовать https://github.com/gunthercox/ChatterBot для общения
# с пользователем и плагин chatter.py будет отключён!
USE_CHATTER = False
# Должен ли бот отвечать на сообщения без префикса?
IGNORE_PREFIX = True

# На текущий момент может принимать значение -  rucaptcha или antigate
CAPTCHA_SERVER = "rucaptcha"  # Сервис для решения капч.
CAPTCHA_KEY = ""  # API ключ для сервиса решения капч

# Нужно ли писать получаемые сообщения в лог
LOG_MESSAGES = False
# Нужно ли писать выполняемые команды в лог
LOG_COMMANDS = True

# Принимать ли все заявки в друзья автоматически
ACCEPT_FRIENDS = False

# Черный список пользователей
BLACKLIST = ()
BLACKLIST_MESSAGE = "Вы не можете писать боту! Вы находитесь в чёрном списке!"
# Белый список пользователей (если не пуст - только пользователи в этом списке
# могут писать боту и получать от него ответы, иначе - боту могу писать все)
WHITELIST = ()
WHITELIST_MESSAGE = "Вы не можете писать боту! Для этого надо быть в белом списке!"

# Список администраторов
ADMINS = (314648435,)

# Загружаются только указанные плагины или все, при отсутствии значения
# ENABLED_PLUGINS = [
#     'available_cmds',
#     'exchange_rate',
#     'memes',
#     'loaded_plugins',
#     'say_joke',
#     'tts',
#     ]
ENABLED_PLUGINS = []
