import psycopg2, configparser, os

os.system("clear")

def performance():
    config = configparser.ConfigParser()
    config.read("configuration.ini")
    namedb = config["DATABASE"]["NAME"]
    userdb = config["DATABASE"]["USER"]
    passdb = config["DATABASE"]["PASSWORD"]
    hostdb = config["DATABASE"]["HOST"]

    print(namedb, userdb,passdb,hostdb)

def start_programm():
    if os.path.exists("configuration.ini") == True:
        performance()
    else:
        file_path = open("configuration.ini", "w+")
        file_path.write("""#Файл конфигурации подключения к базе данных PostgreSQL!

[DATABASE]
NAME=None
USER=None
PASSWORD=None
HOST=None""")

        print("Был создан конфигурационный файл базы данных (configuration.ini). Откройте его и настройте параметры подключения!")

if __name__ == "__main__":
    start_programm()