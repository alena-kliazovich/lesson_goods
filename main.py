import datetime
from decimal import Decimal
from goods import add, find, amount, expire
from pytest import

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ]
}

add(goods, 'молоко', Decimal('2'), '2023-6-22')

print(goods)

print(goods)

print(find(goods, 'Молоко'))

print(amount(goods, 'молоко'))


print(expire(goods))

