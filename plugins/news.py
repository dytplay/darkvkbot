from random import choice

import aiohttp
import xmltodict

from plugin_system import Plugin
from settings import PREFIXES
from utils import unquote

# yandex news
news = {"Армия \n": "https://news.yandex.ru/army.rss",
        "Авто \n": "https://news.yandex.ru/auto.rss",
        "Мир \n": "https://news.yandex.ru/world.rss",
        "Главное \n": "https://news.yandex.ru/index.rss",
        "Игры \n": "https://news.yandex.ru/games.rss",
        "Интеренет \n": "https://news.yandex.ru/internet.rss",
        "Кино \n": "https://news.yandex.ru/movies.rss",
        "Музыка \n": "https://news.yandex.ru/music.rss",
        "Политика \n": "https://news.yandex.ru/politics.rss",
        "Наука \n": "https://news.yandex.ru/science.rss",
        "Экономика \n": "https://news.yandex.ru/business.rss",
        "Спорт \n": "https://news.yandex.ru/sport.rss",
        "Происшествия \n": "https://news.yandex.ru/incident.rss",
        "Космос \n": "https://news.yandex.ru/cosmos.rss"}

plugin = Plugin("Новости",
                usage=["новости - показать новость",
                       "новости [тема] - показать новость определённой тематики",
                       "новости помощь - показать доступные темы"])


@plugin.on_command('Новости')
async def show_news(msg, args):
    url = news["главное"]

    if args:
        category = args.pop()

        if category.lower() in ["помощь", "помощ", "помоги", "помог"]:
            return await msg.answer(f"{PREFIXES[0]}новости [тема], где тема - это одно из следующих слов:\n"
                                    f"{', '.join([k[0].upper() + k[1:] for k in news.keys()])}")

        if category.lower() in news:
            url = news[category]

    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            xml = xmltodict.parse(await resp.text())
            items = xml["rss"]["channel"]["item"]
            item = unquote(choice(items))

            return await msg.answer(f'👉 {item["title"]}\n'
                                    f'👉 {item["description"]}')
@plugin.on_command('Темы')
async def show_news(msg, args):

    if args:
        category = args.pop()

        if category.lower() in ["новостей"]:
            return await msg.answer(f"{PREFIXES[0]}Для отображения новостей по теме используйте команду <Новости [тема]>, где тема - это одно из следующих слов:\n"
                                    f"{''.join([k[0].upper() + k[1:] for k in news.keys()])}")

        if category.lower() in news:
            url = news[category]