# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Проверка оплаты киви


def create_pay_qiwi_func(send_requests, receipt, message_id, way):
    check_qiwi_pay_inl = InlineKeyboardMarkup()
    check_qiwi_pay_inl.add(InlineKeyboardButton(
        text="🌀 Перейти к оплате", url=send_requests))
    check_qiwi_pay_inl.add(InlineKeyboardButton(text="🔄 Проверить оплату",
                                                callback_data=f"Pay:{way}:{receipt}:{message_id}"))
    return check_qiwi_pay_inl


# Кнопки при открытии самого товара
def open_item_func(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    return open_item


def open_item_func_menu_tickets(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    open_item.row(InlineKeyboardButton("Назад", callback_data="back_ticket"),
                  InlineKeyboardButton("Вперед", callback_data="next_ticket"))

    return open_item


def open_item_func_menu_burger(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    open_item.row(InlineKeyboardButton("Назад", callback_data="back_burger"),
                  InlineKeyboardButton("Вперед", callback_data="next_burger"))

    return open_item


def open_item_func_menu_pizza(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    open_item.row(InlineKeyboardButton("Назад", callback_data="back_pizza"),
                  InlineKeyboardButton("Вперед", callback_data="next_pizza"))

    return open_item


def open_item_func_menu_sushi(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    open_item.row(InlineKeyboardButton("Назад", callback_data="back_sushi"),
                  InlineKeyboardButton("Вперед", callback_data="next_sushi"))

    return open_item


def open_item_func_menu_napitki(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    open_item.row(InlineKeyboardButton("Назад", callback_data="back_napitki"),
                  InlineKeyboardButton("Вперед", callback_data="next_napitki"))

    return open_item


def menu_ticketov(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="Купить товар",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("Вернуться",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))

    open_item.row(InlineKeyboardButton("Назад", callback_data="bks"),
                  InlineKeyboardButton("Вперед", callback_data="nks"))

    return open_item


# Подтверждение покупки товара


def confirm_buy_items(position_id, get_count, message_id):
    confirm_buy_item_keyboard = InlineKeyboardMarkup()
    yes_buy_kb = InlineKeyboardButton(text="✅ Подтвердить",
                                      callback_data=f"xbuy_item:{position_id}:{get_count}:{message_id}")
    not_buy_kb = InlineKeyboardButton("❌ Отменить",
                                      callback_data=f"not_buy_items:{message_id}")
    confirm_buy_item_keyboard.add(yes_buy_kb, not_buy_kb)
    return confirm_buy_item_keyboard
#
