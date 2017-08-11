from database import *
from plugin_system import Plugin

plugin = Plugin('🔞Контроль бота - может использовать только владелец страницы или администратор',
                usage=['Выключить - выключает бота',
                       'Добавить в белый список [id] - добавить пользователя с id в белый список',
                       'Убрать из белого списка [id] - убрать пользователя с id из белого списка',
                       'Добавить в чёрный список [id] - добавить пользователя с id в чёрный список',
                       'Убрать из чёрного списка [id] - убрать пользователя с id из чёрного списка',
                       'Сделать админом [id] - добавить пользователя с id в белый список',
                       'Убрать из админов [id] - убрать пользователя с id из белого списка',
                       'Чёрный список - показать чёрный список'
                       'Белый список - показать белый список',
                       'Администраторы - показать администраторов'])


@plugin.on_command('Выключить')
async def shutdown(msg, args):
    if await get_or_none(Role, user_id=msg.user_id, role="admin"):
        await msg.answer('Выключаюсь, мой господин...')
        exit()
    else:
        await msg.answer('Я бы с радостью, но вы не мой господин \n Своего господина я знаю в лицо.  :)')


@plugin.on_command('Добавить в белый список')
async def add_to_whitelist(msg, args):
    return await add_to_list(msg, args, "whitelisted")


@plugin.on_command('Добавить в чёрный список')
async def add_to_admins(msg, args):
    return await add_to_list(msg, args, "blacklisted")


@plugin.on_command('Сделать администратором')
async def add_to_blacklist(msg, args):
    return await add_to_list(msg, args, "admin")


@plugin.on_command('Убрать из белого списка')
async def remove_from_whitelist(msg, args):
    return await remove_from_list(msg, args, "whitelisted")


@plugin.on_command('Убрать из чёрного списка')
async def remove_from_blacklist(msg, args):
    return await remove_from_list(msg, args, "blacklisted")


@plugin.on_command('Убрать из администраторов')
async def remove_from_admins(msg, args):
    return await remove_from_list(msg, args, "admin")


@plugin.on_command('Чёрный список')
async def show_blacklisted(msg, args):
    return await show_list(msg, args, "blacklisted")


@plugin.on_command('Белый список')
async def show_whitelisted(msg, args):
    return await show_list(msg, args, "whitelisted")


@plugin.on_command('Администраторы')
async def show_blacklisted(msg, args):
    return await show_list(msg, args, "admin")


async def show_list(msg, args, role):
    if not await get_or_none(Role, user_id=msg.user_id, role="admin"):
        return

    message = f"Список пользователей являющихся администорами. :\n"

    for u in await db.execute(Role.select(Role.user_id).where(Role.role == role)):
        message += f"{u.user_id}, "

    return await msg.answer(message)


async def add_to_list(msg, args, role):
    if not await get_or_none(Role, user_id=msg.user_id, role="admin"):
        return

    if not args or not args[0].isdigit():
        return await msg.answer("Вы не указали ID пользователя или указали его неверно!")

    await db.get_or_create(Role, user_id=int(args[0]), role=role)

    if role == "whitelisted":
        await check_white_list(msg.vk.bot)

    return await msg.answer("Готово!")


async def remove_from_list(msg, args, role):
    if not await get_or_none(Role, user_id=msg.user_id, role="admin"):
        return

    if not await get_or_none(Role, user_id=msg.user_id, role=role):
        return

    if not args or not args[0].isdigit():
        return await msg.answer("Вы не указали ID пользователя или указали его неверно!")

    await db.execute(Role.delete().where(Role.user_id == int(args[0])))

    if role == "whitelisted":
        await check_white_list(msg.vk.bot)

    return await msg.answer("Готово!")
