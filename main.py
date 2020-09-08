"""
Версия приложения обновлена.
Приложенние позволяет спарсить n-ное количество изображений по url.
Модификации файла ускоряют обработку данных на 80 процентов в среднем.
Данный эффект экономии времени обусловлен разделением потоков исполнения.
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import *
import os



def get_Inputs():
    """
    Очередь запросов.
Данная функция не принимает входных данных.
Работает функция с файлом данных в главной директории программы,
наименование которого было указано при запуске.
    :return: список данных проставленных в очередь
    """
    with open("{}\\{}.txt".format(directoryPath, file_Name)) as f:
        lst_poz_in_file = []
        for i in f:
            lst_poz_in_file.append(i.split("\n")[0])
        print("В очереди {} запросов".format(len(lst_poz_in_file)))
        return lst_poz_in_file

def get_html(url) -> str:
    """
Данная функция выполняет Get запрос по входящему url и возвращает тело сообщения,
полученного в ответе
    :param url: входящая ссылка для запроса
    :return: данные в формате html
    """
    reg = requests.get(url)
    return str(reg.text)

def main_Func():
    """
Данная функция обрабатывает первый поток данных разделяя очередь с 0-го индекса,
до половины очереди
    :return: не возвращает значений. Производит загрузку файлов формата JPG в главную директорию
    """
    while True:
        lst = get_Inputs()
        for link in lst:
            html = get_html("{}{}/".format(url, link))
            soup = BeautifulSoup(html, 'html.parser')
            try:
                image = soup.find(id='js-cover-preview')['src']
                urlretrieve(image, link + '.jpeg')
                print("Файл с кодом {} обработан и загружен".format(link))
            except:
                print("Файл {} не обработан\n".format(link))
                with open("{}fallen.txt".format(directoryPath), 'a') as falen:
                    falen.write("Файл {} не обработан\n".format(link))
                continue
            else:
                continue
        break

if __name__ == "__main__":
    url = 'https://pg.brandquad.ru/png/ede7c57abbb3991f1ad84e5c3e5bd38a/'
    directoryPath = input(":")  # тут был input()
    if directoryPath == "": directoryPath = "{}\\".format(os.getcwd())
    file_Name = input(":")  # тут был input()
    while True:
        if os.path.exists("{}\\{}.txt".format(directoryPath, file_Name)):
            break
        else:
            continue
    main_Func()
    print("Loading complete")