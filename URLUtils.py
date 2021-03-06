"""
Версия приложения обновлена.
Приложенние позволяет спарсить n-ное количество изображений по url.
Модификации файла ускоряют обработку данных на 80 процентов в среднем.
Данный эффект экономии времени обусловлен разделением потоков исполнения.
Пакет исполняемый
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import *
import os
import logging

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

url = 'https://pg.brandquad.ru/png/ede7c57abbb3991f1ad84e5c3e5bd38a/'


def get_Inputs(file):
    """
    Очередь запросов.
Данная функция не принимает входных данных.
Работает функция с файлом данных в главной директории программы,
наименование которого было указано при запуске.
    :return: список данных проставленных в очередь
    """
    log.debug("Запущена функция get_Inputs")
    with open(file) as f:
        log.debug('открыт файл для чтения')
        lst_poz_in_file = []
        for i in f:
            log.debug(f'{i}')
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


def main_Func(file):
    """
Данная функция обрабатывает первый поток данных разделяя очередь с 0-го индекса,
до половины очереди
    :return: не возвращает значений. Производит загрузку файлов формата JPG в главную директорию
    """
    lst = get_Inputs(file)
    while True:
        for link in lst:
            log.debug(f'{link}')
            html = get_html("{}{}/".format(url, link))
            soup = BeautifulSoup(html, 'html.parser')
            try:
                image = soup.find(id='js-cover-preview')['src']
                urlretrieve(image, link + '.jpeg')
                print("Файл с кодом {} обработан и загружен".format(link))
            except:
                print("Файл {} не обработан\n".format(link))
                with open("{}\\fallen.txt".format(os.getcwd()), 'a') as fallen:
                    fallen.write("Файл {} не обработан\n".format(link))
                continue
            else:
                continue
        print("Loading complete")
        break



if __name__ == "__main__":
    pass
