import datetime
from datetime import timedelta
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items: dict, title: str, amount: Decimal, expiration_date: str=None):
    if not title in items:
        items[title] = []
    if expiration_date == None:
        date = None
    else:
        date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title].append({'amount': amount, 'expiration_date': date})

def add_by_note(items, note):
    words = str.split(note, ' ')
    last_words = words[-1]

    if len(str.split(last_words,'-'))== 3:
        date = last_words
        amount = Decimal(words[-2])
        title = str.join(' ', words[0:-2])
    else:
        amount = Decimal(last_words)
        date = None
        title = str.join(' ', words[0:-1])
    add(items, title, amount, date)

def find(items, needle):
    needle_list = []
    for title in items.keys():
        if str.lower(needle) in str.lower(title):
            needle_list.append(title)
    return  needle_list

def amount(items, needle):
    goods_keys = find(items, needle)
    total_amount = Decimal('0')
    for title in goods_keys:
        items_list = items[title]
        for item in items_list:
            total_amount += item['amount']
    return total_amount

def expire(items, in_advance_days=0):
    expired_goods = []
    compared_date = datetime.date.today() + timedelta(days= in_advance_days)
    for title, good_list in items.items():
        amount = Decimal('0')
        for good in good_list:
            expired_date = good['expiration_date']
            if expired_date is not None:
                if compared_date >= expired_date:
                    amount += good["amount"]
        if amount > 0:
            expired_goods.append((title, amount))

    return expired_goods

