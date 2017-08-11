import random

from plugin_system import Plugin
usage = ['двач - случайная фотка с двача',
       'мемы - случайная фотка из агрегатора мемасов мдк']

plugin = Plugin("🔎 Случайные фотографии из пабликов",
                usage=usage)

# Стоп лист для текста в посте
stop_list = ['http', '[club', '[public', '[id']

# Функция проверки вхождения элементов списка a в строку "b"
any_in = lambda word_list, string: any(i in string for i in word_list)

async def give_memes(msg, group_id):
    """Получает фотографию из случайного поста выбранной группы"""
    answer = ''
    photo = None

    values = {
        # owner_id = ид группы
        'owner_id': group_id,
        'offset': random.randint(1, 1985),
        'count': 10
    }

    # Пока мы не нашли фотографию
    while not photo:
        values['offset'] = random.randint(1, 1985)

        # Получаем 10 постов и перемешиваем их
        data = await msg.vk.method('wall.get', values)
        items = random.sample(data.get('items'), len(data.get('items')))
        for item in items:
            content = item['text']
            attaches = item.get('attachments')
            # TODO добавить фильтр репостов из других пабликов
            # Если в тексте поста есть запрещенные слова или нет документов
            if any_in(stop_list, content) or not attaches:
                continue
            # Если одна картинка
            if len(attaches) == 1:
                answer = content if content else ''
                photo = attaches[0].get('photo')

    oid = photo['owner_id']
    att_id = photo['id']
    access_key = photo['access_key']

    attachment = f'photo{oid}_{att_id}_{access_key}'
    await msg.answer(answer, attachment=attachment)


@plugin.on_command('2ch')
async def twoch_memes(msg, args):
    group_id = -22751485
    await give_memes(msg, group_id)


@plugin.on_command('MDK')
async def just_memes(msg, args):
    group_id = -57846937
    await give_memes(msg, group_id)

@plugin.on_command('4ch')
async def just_memes(msg, args):
    group_id = -45745333
    await give_memes(msg, group_id)
