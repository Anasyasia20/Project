import time
f = open('task2_data.dat', 'r')  # открываем таблицу
stars = f.read().split('\n')  # считываем её, разделяя по переходам строк
entries = []  # временный массив
for entry in stars:  # перебираем все ряды
    entries.append(entry.split())  # разделяем ряды по пробелам
entries = entries[1:]  # 1: удаляем первое значение (названия столбцов)
stars = entries  # заменяем изначальный массив временным
entries = []  # обнуляем временный массив
# objects = []  # имена объектов
# filters = []  # фильтры
objects = set()
filters = set()

# entry === [имя объекта, дата, фильтр, звездная величина]
for entry in stars:
    name = ''  # формируем одинаковое имя
    if len(entry) > 4:  # в имени есть пробел
        name = entry[0] + ' ' + entry[1]  # первая часть имени, пробел, вторая часть имени
        entry = [name] + entry[2:]  # обновляем ряд в соответствии с новым именем
    elif len(entry) < 4:  # ряд не рассматриваем
        continue
    else:
        name = entry[0]

    # suhor в одно имя
    name = name.replace('_', '')
    name = name.replace(' ', '')
    name = name.lower()
    name = name[:2].upper() + ' ' + name[2:].title()  # снова преобразовываем, suhor => SU Hor
    entry[0] = name  # обновляем ряд

    entry[1] = float('24' + entry[1])  # преобразуем дату и звездную величину в числа из строк
    entry[3] = float(entry[3])
    # проверяем на новое имя объекта
    objects.add(entry[0])
    # проверяем на новый фильтр
    filters.add(entry[2].title())
    entries.append(entry)  # обновляем временный массив
stars = entries  # замена
entries = []  # обнуление

print('Объекты:', objects)
print('Фильтры:', filters)

#  3 part

object_name = None
while object_name not in objects:
    object_name = input('Введите имя объекта: ')  # просим пользователя ввести имя объекта

filters_names = set()
while len(filters.intersection(filters_names)) == 0:
    inp = input('Введите фильтр: ')  # то же самое, но с фильтром
    filters_names = set(inp.split(','))

filters_names = filters.intersection(filters_names)

# перевод в дни и часы

unix_epoch = 2440587.5  # 1 января 1970 года в юлианских днях

def julian_to_unix(date):
    days = date - unix_epoch
    seconds = days * 24 * 60 * 60
    return seconds

def unix_to_grigorian(seconds):
    tm = time.gmtime(seconds)
    # код time.gmtime(seconds) возвращает структуру с информацией о дне, месяце и т.д.
    # из секунд с начала эпохи юникс (1 января 1970)
    day = str(tm.tm_mday)
    if len(day) == 1:  # если день - это одна цифра, то добавляем 0 в начало
        day = '0' + day
    mon = str(tm.tm_mon)
    if len(mon) == 1:
        mon = '0' + mon
    year = tm.tm_year
    hour = str(tm.tm_hour)
    if len(hour) == 1:
        hour = '0' + hour
    min = str(tm.tm_min)
    if len(min) == 1:
        min = '0' + min
    sec = str(tm.tm_sec)
    if len(sec) == 1:
        sec = '0' + sec
    return f'{day}.{mon}.{year} {hour}:{min}:{sec}'

processed = {}  # словарь с обработанной информацией из stars
for entry in stars:
    if entry[0] != object_name:  # объект не введенный пользователем - пропускаем
        continue

    if entry[2] not in filters_names:  # фильтр не введенный пользователем - пропускаем
        continue

    if entry[1] not in processed:  # если даты нет в processed, то
        processed[entry[1]] = {'date': unix_to_grigorian(julian_to_unix(entry[1]))}
        # создаем в словаре processed и сразу вычисляем дату в нужном формате
        for filter_name in filters_names:
            processed[entry[1]][filter_name] = '-'  # назначаем всем столбцам-фильтрам значение '-'
        processed[entry[1]][entry[2]] = entry[3]  # назначаем нужному столбцу-фильтру значение звездной величины

#создание файла

f = open(f'_{object_name}_.dat', 'w', encoding='utf-8')  # создаем файл с нужным именем
headers = 'Date\tHJD\t'  # создаем ряд-заголовок
for filter in filters_names:
    headers += filter + '\t'  # добавляем столбцы-фильтры
headers = headers[:-1] + '\n'  # удаляем лишнюю табуляцию и добавляем переход строки
f.write(headers)  # записываем

dates = list(processed.keys())  # переводим ключи в словаре processed в список, чтобы можно было его отсортировать
dates.sort()  # сортировка
for date in dates:  # проходимся по списку dates в порядке возрастания
    value = processed[date]  # получаем соответствующую информацию из словаря processed
    s = value['date'] + '\t' + str(date) + '\t'  # первый столбец - григорианская дата, второй - JD
    for filter in filters_names:
        s += str(value[filter]) + '\t'  # добавляем столбцы-фильтры в порядке, в котором они были в filters_names
    s = s[:-1] + '\n'  # удаляем лишнюю табуляцию, переход строки
    f.write(s)  # запись
