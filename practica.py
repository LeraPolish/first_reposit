# import datetime

# now = datetime.datetime.now()
# print(now)


# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)


# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())

# import datetime
# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"


# import datetime

# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)
# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

# print(specific_date)  # Виведе "2020-01-07 00:00:00"


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")  



# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2


# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)



# from datetime import datetime

# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу


# from datetime import datetime

# # Припустимо, є timestamp
# timestamp = 1617183600

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime


# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)



# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)


# from datetime import datetime

# iso_date_string = "2023-03-14T12:39:29.992996"

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)



# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")



# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC


# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  


# from datetime import datetime, timezone, timedelta

# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC


# from datetime import datetime, timezone, timedelta

# # Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)



# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")



# import time

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")


# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")


# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")




# import random

# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")


# # import random

# num = random.random()
# print(num)


# import random

# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")


# import random

# target = random.randrange(1, 11, 2)
# print(f"Ціль: {target}")


# import random

# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

# random.shuffle(cards)

# print(f"Перемішана колода: {cards}")


# import random

# fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))


# import random

# items = ['яблуко', 'банан', 'вишня', 'диня']
# chosen_item = random.choices(items, k=10)
# print(chosen_item)  


# import random

# colors = ['червоний', 'зелений', 'синій']
# weights = [10, 1, 1]
# chosen_color = random.choices(colors, weights, k=1)
# print(chosen_color)  


# import random

# participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
# team = random.sample(participants, 4)
# print(f"Команда: {team}")


# import random

# price = random.uniform(50, 100)
# print(f"Випадкова ціна: {price:.2f}")



# import math

# # Вихідне число
# x = 3.7

# # Використання різних методів округлення
# ceil_result = math.ceil(x)  # Округлення вгору
# floor_result = math.floor(x)  # Округлення вниз
# trunc_result = math.trunc(x)  # Відсікання дробової частини

# print(ceil_result, floor_result, trunc_result)


# import math

# # Використання констант
# print(math.pi)  # Виведе приблизне значення π

# # Тригонометрія
# angle = math.radians(60)  # Конвертація з градусів у радіани
# print(math.sin(angle))  # Синус кута

# # Корінь числа
# print(math.sqrt(9))  # Квадратний корінь з 9

# # Логарифми
# print(math.log(10, 2))  # Логарифм 10 за основою 2


# import math

# # r = math.isclose(0.1 + 0.2, 0.3)
# # print(r)  # Це поверне True

# r = math.isclose(0.1, 0.10000000009)
# print(r)  # Це поверне True


# my_string = "Hello, world!"

# # Проверка, начинается ли строка с определенной последовательности
# if my_string.startswith("Hello"):
#     print("Строка начинается c 'Hello'")

# # Проверка, заканчивается ли строка определенной последовательностью
# if my_string.endswith("world!"):
#     print("Строка заканчивается на 'world!'")


# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
# one_line_text = "Textual data in Python is handled with str objects," \
#                 " or strings. Strings are immutable sequences of Unicode" \
#                 " code points. String literals are written in a variety " \
#                 " of ways: single quotes, double quotes, triple quoted."


# x = ("spam " "eggs") == "spam eggs"  # True
# print(x)


# one_line_text = ("Textual data in Python is handled with str objects,"
#                 " or strings. Strings are immutable sequences of Unicode"
#                 " code points. String literals are written in a variety "
#                 " of ways: single quotes, double quotes, triple quoted.")



# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q")) # -1

# s = 'Some words'

# print(s.find("o"))
# print(s.rfind('o'))


# text = "hello world"
# result = text.split()
# print(result)  # Виведе: ['hello', 'world']

# my_string = "apple,banana,orange"
# fruits = my_string.split(',')
# print(fruits)

# my_string = "line1\nline2\nline3"
# lines = my_string.split('\n')
# print(lines) 


# list_of_strings = ['Hello', 'world']
# result = ' '.join(list_of_strings)
# print(result)  # Виведе: 'Hello world'

# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'


# text = "Hello world"
# new_text = text.replace("world", "Python")
# print(new_text) 

# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 2)
# print(new_text)  

# text = "Hello, world!"
# new_text = text.replace(" world", "")
# print(new_text)


# print('TestHook'.removeprefix('Test')) # Hook
# print('TestHook'.removeprefix('Hook')) # TestHook
# print('TestHook'.removesuffix('Test'))
# print('TestHook'.removesuffix('Hook'))


# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
#     # obj_query.update({key: value.replace('+', ' ').replace('-', ' ')})
# print(obj_query)


# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print("Це дійсно число!")
# else:
#     print("Це не число!")


# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")



# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# input_string = "34 DF 56 AC"
# result = ''.join([MAP.get(ord(char), char) for char in input_string])
# print(result)



# print(ord('A'))  # Вывод: 65
# print(chr(65))  # Вывод: 'A'


# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[s] = c
#     MAP[s.lower()] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)


# name = "Alice"
# formatted = f"{name:>10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)


# age = 10
# name = "Alice"
# formatted = f"{name:<10} = {age}"
# print(formatted) 



