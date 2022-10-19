import psycopg2
import configparser
import os
import re

os.system("clear")

configpath = "configuration.ini"
config = configparser.ConfigParser()
config.read(configpath)
phonere = re.compile(r'/[+]\d[(]\d{3}[)]\d{3}[-]\d{2}[-]\d{2}/gm')
emailre = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

#ЦВЕТНОЙ ТЕКСТ

def cprint_upred(text):
    print("\033[1m\033[31m{}\033[0m".format(text))
def cprint_yellow(text):
    print("\033[33m{}\033[0m".format(text))
def cprint_blue(text):
    print("\033[34m{}\033[0m".format(text))


def performance():
    namedb = config["DATABASE"]["NAME"]
    userdb = config["DATABASE"]["USER"]
    passdb = config["DATABASE"]["PASSWORD"]
    hostdb = config["DATABASE"]["HOST"]
    portdb = config["DATABASE"]["PORT"]

    cprint_blue("""
Параметры работы

1 - Добавить нового клиента
2 - Добавить номер телефона для записи клиента
3 - Изменит данные клиента в базе
4 - Удалить телефон клиента в базе
5 - Удалить клиента из базы
6 - Поиск клиента в базе
EXT - Завершить работу программы\n""")

    selection = input("Введите параметр - ")


def start_programm():
    if os.path.exists(configpath) == True:
        cprint_yellow(f"[INFO] Программа запущена!\n\n")
        performance()
    else:
        config.add_section("DATABASE")
        add_dbname = input("[SET]Введите имя базы данных - ")
        add_dbuser = input("[SET]Введите имя пользователя базы данных - ")
        add_dbpass = input("[SET]Введите пароль базы данных - ")
        add_dbhost = input("[SET]Введите адрес хоста базы данных - ")
        add_dbport = input("[SET]Введите номер порта базы данных (по умолчанию - 5432) - ")

        config.set("DATABASE","NAME", add_dbname)
        config.set("DATABASE","USER", add_dbuser)
        config.set("DATABASE","PASSWORD", add_dbpass)
        config.set("DATABASE","HOST", add_dbhost)
        config.set("DATABASE","PORT", add_dbport)

        config.add_section("INSTALLATIONS")
        config.set("INSTALLATIONS","CHECK", "True")

        with open(configpath, "w") as config_file:
            config.write(config_file)

        os.system("clear")
        cprint_yellow(f"[INFO] Файл конфигурации {configpath} создан.")
        cprint_yellow(f"[INFO] Программа запущена!\n\n")
        performance()

if __name__ == "__main__":
    start_programm()