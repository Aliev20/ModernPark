# - *- coding: utf- 8 - *-
from utils.db_api.sqlite import get_userx, get_purchasesx, logger


def get_user_qrcode_profile(user_id):
    get_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    time = str(get_user[6])
    year = time.split("-")[0]
    month = time.split("-")[1].split("-")[0]
    count = time.split("-")[2].split(" ")[0]

    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = (
        f"<b>📱 Профиль:</b>\n"
        f"\n"
        f"🔑 ID: <code>{get_user[1]}</code>\n"
        f"👤 Логин: <b>@{get_user[2]}</b>\n"
        f"🕜 Регистрация: <code>{count}.{month}.{year}</code>\n"
        f"\n"
        f"💳 Баланс: <code>{get_user[4]} руб.</code>\n"
        f"💳 Баланс бонусной карты: <code>{get_user[8]}руб</code>\n"
        f"💵 Всего пополнено: <code>{get_user[5]} руб.</code>\n"
        f"🎁 Куплено товаров: <code>{count_items} шт.</code>"
    )
    return msg


def get_user_profile(user_id):
    get_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    time = str(get_user[6])
    year = time.split("-")[0]
    month = time.split("-")[1].split("-")[0]
    count = time.split("-")[2].split(" ")[0]

    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = (
        f"<b>📱 Ваш профиль:</b>\n"
        f"\n"
        f"🔑 Мой ID: <code>{get_user[1]}</code>\n"
        f"👤 Логин: <b>@{get_user[2]}</b>\n"
        f"🕜 Регистрация: <code>{count}.{month}.{year}</code>\n"
        f"\n"
        f"💳 Баланс: <code>{get_user[4]} руб.</code>\n"
        f"💵 Всего пополнено: <code>{get_user[5]} руб.</code>\n"
        f"🎁 Куплено товаров: <code>{count_items} шт.</code>"
    )
    return msg


def search_user_profile(user_id):
    get_status_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    print(f"INFORMATION\n\n\n{get_status_user[8]}")
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = (
        f"<b>📱 Профиль пользователя:</b> <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n"
        f"\n"
        f"🔑 ID: <code>{get_status_user[1]}</code>\n"
        f"👤 Логин: <b>@{get_status_user[2]}</b>\n"
        f"Ⓜ Имя: <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n"
        f"🕜 Регистрация: <code>{get_status_user[6]}</code>\n"
        f"\n"
        f"💳 Баланс: <code>{get_status_user[4]}руб</code>\n"
        f"💵 Всего пополнено: <code>{get_status_user[5]}руб</code>\n"
        f"🎁 Куплено товаров: <code>{count_items}шт</code>\n"
        f"🎟 Баланс бонусной карты: <code>{get_status_user[8]}руб</code>\n"
    )
    return msg
