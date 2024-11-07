import os
import requests
import time

import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


proxies = {
            'http': f'http://{os.getenv('PROXY')}',
           }


def get_category():
    url = os.getenv('URL')
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://www.wildberries.by',
        'priority': 'u=1, i',
        'referer': 'https://www.wildberries.by/catalog/elektronika/igry-'
                   'i-razvlecheniya/aksessuary/garnitury',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8",'
                     ' "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
    }

    response = requests.get(url=url, headers=headers, proxies=proxies)
    if response.status_code != 204:
        return response.json()


def format_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            print(product.get('name', None))
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'id': product.get('id', None),
                'reviewRating': product.get('reviewRating', None),
                'feedbacks': product.get('feedbacks', None),
            })

    return products


def main():
    response = get_category()
    products = format_items(response)
    print(products)


if __name__ == '__main__':
    main()


