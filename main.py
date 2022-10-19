import psycopg2
import configparser
import os

os.system("clear")

configpath = "configuration.ini"
config = configparser.ConfigParser()
config.read(configpath)

#ЦВЕТНОЙ ТЕКСТ

def cprint_upred(text):
    print("\033[1m\033[31m{}\033[0m".format(text))
def cprint_yellow(text):
    print("\033[33m{}\033[0m".format(text))


def performance():
    namedb = config["DATABASE"]["NAME"]
    userdb = config["DATABASE"]["USER"]
    passdb = config["DATABASE"]["PASSWORD"]
    hostdb = config["DATABASE"]["HOST"]
    portdb = config["DATABASE"]["PORT"]


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