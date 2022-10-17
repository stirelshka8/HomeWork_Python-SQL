import psycopg2, configparser, os.path

if os.path.exists("configuration.ini"):
    pass
else:
    file_path = open("configuration.ini", "w+")
    file_path.write("""#Файл конфигурации подключения к базе данных PostgreSQL!

[DATABASE]
NAME=None
USER=None
PASSWORD=None
HOST=None""")
print("Был создан конфигурационный файл базы данных. Откройте его и настройте параметры подключения!")


#config = configparser.ConfigParser()
#config.read("configuration.ini")
#namedb = config["DATABASE"]["NAME"]
#userdb = config["DATABASE"]["USER"]
#passdb = config["DATABASE"]["PASSWORD"]
#hostdb = config["DATABASE"]["HOST"]



#print(namedb, userdb,passdb,hostdb)