import os, random

def level_loading():   #загрузка уровней из тестого файлов рандомным образом
    with open(str(os.getcwd()) + '\data\levels' + '\\' +
              random.choice(os.listdir(str(os.getcwd()) + '\data\levels')), 'r', encoding='UTF-8') as file_level:
        data_level = list(map(lambda x: x.replace('\n', ''), file_level.readlines()))

    with open(str(os.getcwd()) + '\data\levels' + '\\' +
              random.choice(os.listdir(str(os.getcwd()) + '\data\levels')), 'r', encoding='UTF-8') as file_level_second:
        data_level_second = list(map(lambda x: x.replace('\n', ''), file_level_second.readlines()))
    data_level_final = []
    for index, string in enumerate(data_level):
        data_level_final.append(string + data_level_second[index][1:])

    for row in data_level_final:
        if 'p' in row[round(len(row) / 2):]:
            metka = row
            break

    data_level = []
    for row in data_level_final:
        if row == metka:
            data_level.append(row[::-1].replace('p', 's', 1)[::-1])
        else:
            data_level.append(row)

    return data_level

TILE_SIZE = 60
MAP = level_loading()
screen_width, screen_height = len(MAP[0]) * TILE_SIZE, len(MAP) * TILE_SIZE


