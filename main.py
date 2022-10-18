import psycopg2
import configparser
import os

os.system("clear")

configpath = "configuration.ini"
config = configparser.ConfigParser()
config.read(configpath)

def performance():
    namedb = config["DATABASE"]["NAME"]
    userdb = config["DATABASE"]["USER"]
    passdb = config["DATABASE"]["PASSWORD"]
    hostdb = config["DATABASE"]["HOST"]

    print(namedb, userdb,passdb,hostdb)

def start_programm():
    if os.path.exists(configpath) == True:
        performance()
    else:
        config.add_section("DATABASE")
        add_dbname = input("[!]Введите имя базы данных - ")
        add_dbuser = input("[!]Введите имя пользователя базы данных - ")
        add_dbpass = input("[!]Введите пароль базы данных - ")
        add_dbhost = input("[!]Введите адрес хоста базы данных - ")

        config.set("DATABASE","NAME", add_dbname)
        config.set("DATABASE","USER", add_dbuser)
        config.set("DATABASE","PASSWORD", add_dbpass)
        config.set("DATABASE","HOST", add_dbhost)


        with open(configpath, "w") as config_file:
            config.write(config_file)

if __name__ == "__main__":
    start_programm()