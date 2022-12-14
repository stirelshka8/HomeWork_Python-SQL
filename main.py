import configparser
import psycopg2
import os
import re

os.system("clear")

# ФАЙЛ КОНФИГУРЦИИ

configpath = "configuration.conf"
config = configparser.ConfigParser()
config.read(configpath)

# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
phonere = re.compile(r'[+]\d\d{10}')
emailre = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# ЦВЕТНОЙ ТЕКСТ

def cprint_upred(text):
    print("\033[1m\033[31m{}\033[0m".format(text))
def cprint_yellow(text):
    print("\033[33m{}\033[0m".format(text))
def cprint_blue(text):
    print("\033[34m{}\033[0m".format(text))

# ФУНКЦИЯ ЗАПУСКА ПРОГРАММЫ
def performance(cursor, conn):
    cprint_blue("""
Параметры работы

1 - Добавить нового клиента
2 - Добавить номер телефона для записи клиента
3 - Изменит данные клиента в базе
4 - Удалить телефон клиента в базе
5 - Удалить клиента из базы
6 - Поиск клиента в базе
0 - Завершить работу программы\n""")

    selection = int(input("[WORK]Введите параметр - "))
    
    if selection == 0:
        quit()
    elif selection == 1 and selection <= 6:
        Working_Database.add_client(cursor, conn)
    elif selection == 2 and selection <= 6:
        Working_Database.add_phone(cursor, conn)
    elif selection == 3 and selection <= 6:
        Working_Database.edit_client(cursor, conn)
    elif selection == 4 and selection <= 6:
        Working_Database.del_phone(cursor, conn)
    elif selection == 5 and selection <= 6:
        Working_Database.del_client(cursor, conn)
    elif selection == 6 and selection <= 6:
        Working_Database.search_client(cursor, conn)

def create_tab(cursor):
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS client(
                    id_client SERIAL PRIMARY KEY,
                    firstname_client TEXT NOT NULL,
                    lastname_client TEXT NOT NULL
                ); 
                """)
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS email(
                    id_email SERIAL PRIMARY KEY,
                    id_client INTEGER REFERENCES client (id_client),
                    name_email TEXT
               ); 
               """)
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS phone(
                    id_phone SERIAL PRIMARY KEY,
                    id_client INTEGER REFERENCES client (id_client),                    
                    number_phone TEXT
                ); 
                """)

def first_name():
    input_first_name = input ('Введите имя клиента: ').title()
    return input_first_name

def last_name():
    input_last_name = input ('Введите фамилию клиента: ').title()
    return input_last_name

def email():
     input_email = input ('Введите E-Mail клиента в формате email@example.com: ')
     while re.fullmatch(emailre, input_email) == None:
         cprint_upred("Введенный E-Mail не соответствует установленному формату!")
         input_email = input ('Введите E-Mail клиента в формате email@example.com: ')
     return input_email

def phone():
    input_phone = input ('Введите номер телефона клиента в формате +79992271102: ')
    while re.fullmatch(phonere, input_phone) == None:
        print("Введенный номер телефона не соответствует установленному формату!")
        input_phone = input ('Введите номер телефона клиента в формате +79992271102: ')
    return input_phone

class Working_Database():
    def __init__():
        pass

    def add_client(cursor, conn):
        os.system("clear")
        cprint_yellow("Выбран параметр добавления нового киента!\n")
        work_first_name = first_name()
        work_last_neme = last_name()
        work_email = email()
        work_phone = phone()
        cursor.execute ("""INSERT INTO client(firstname_client, lastname_client) VALUES (%s, %s)""", (work_first_name, work_last_neme))
        conn.commit()
        cursor.execute(""" SELECT id_client FROM client WHERE firstname_client = %s AND lastname_client = %s""",(work_first_name, work_last_neme))
        work_exec = cursor.fetchall()
        data_id_client = str(work_exec[0][0])
        cursor.execute ("""INSERT INTO email(id_client, name_email) VALUES (%s, %s)""", (data_id_client, work_email))
        conn.commit()
        cursor.execute ("""INSERT INTO phone(id_client, number_phone) VALUES (%s, %s)""", (data_id_client, work_phone))
        conn.commit()
        cprint_blue(f"Клиент {work_first_name} {work_last_neme} в базу успешно добавлен!")
    
    def add_phone(cursor, conn):
        os.system("clear")
        cprint_yellow("Выбран параметр добавления номера телфона клиенту!\n")
        work_first_name = first_name()
        work_last_neme = last_name()
        cursor.execute(""" SELECT id_client, firstname_client, lastname_client FROM client WHERE firstname_client = %s AND lastname_client = %s""",(work_first_name, work_last_neme))
        work_exec = cursor.fetchall()
        #print(work_exec)
        cprint_upred(f"В запись клиента {work_exec[0][1]} {work_exec[0][2]} добавим новый номер телефона?")
        work_switch = input("Введите ДА для продолжения").upper()
        if work_switch == "ДА":
            #print(work_exec)
            data_id_client = str(work_exec[0][0])
            work_phone = phone()
            cursor.execute ("""INSERT INTO phone(id_client, number_phone) VALUES (%s, %s)""", (data_id_client, work_phone))
            conn.commit()
            cprint_blue(f"Новый номер телефона клиента {work_exec[0][1]} {work_exec[0][2]} в базу успешно добавлен!")

    def edit_client(cursor, conn):
        cprint_yellow("Выбран параметр радактирования записа киента!\n")
        os.system("clear")
        cprint_yellow("Введите Имя и Фамилию клиента запись которого хотим отредактировать")
        work_first_name = first_name()
        work_last_neme = last_name()
        cursor.execute(""" SELECT id_client, firstname_client, lastname_client FROM client WHERE firstname_client = %s AND lastname_client = %s""",(work_first_name, work_last_neme))
        work_exec = cursor.fetchall()
        if work_exec == []:
            cprint_upred("Запись о клиенте отсутствует!")
        else:
            cprint_yellow(f"""
Выбирите режим редактирования над записью клиента {work_exec[0][1]} {work_exec[0][2]}
            
1 - Редактирование телефонов
2 - Редактирование E-Mail 
3 - Редактировать Имя и Фамилию
0 - выход из режима редактирования""")

            input_edit = int(input("[WORK]Введите параметр - "))

            if input_edit == 1:
                Working_Database.edit_client_phone(work_exec[0][0], work_exec[0][1], work_exec[0][2])
            elif input_edit == 2:
                Working_Database.edit_client_email(work_exec[0][0], work_exec[0][1], work_exec[0][2])
            elif input_edit == 3:
               Working_Database.edit_client_name(work_exec[0][0], work_exec[0][1], work_exec[0][2])
            elif input_edit == 0:
                pass

    def edit_client_name(data_id_client, edit_firstname, edit_lastname, cursor, conn):
        os.system("clear")
        cprint_yellow(f"У клиента в данный момент имя {edit_firstname}. ДА если будите редактировать.")
        edit_check = input("Введите ").upper()
        if edit_check == "ДА":
            work_first_name = first_name()
            cursor.execute ("""UPDATE client SET firstname_client = %s WHERE id_client = %s""", (work_first_name, data_id_client))
            conn.commit()
        cprint_yellow(f"У клиента в данный момент фамилия {edit_lastname}.")
        edit_check = input("Введите ДА для продолжения редактирования").upper()
        if edit_check == "ДА":
            work_last_neme = last_name()
            cursor.execute ("""UPDATE client SET lastname_client = %s WHERE id_client = %s""", (work_last_neme, data_id_client))
            conn.commit()
        cprint_blue(f"Данные клиента отредактированны")

    def edit_client_phone(data_id_client, edit_firstname, edit_lastname, cursor, conn):
        os.system("clear")
        print(f'В данный момент у клиента {edit_firstname} {edit_lastname} существуют записи о следующих номерах телефонов:\n')   
        cursor.execute(""" SELECT id_phone, number_phone FROM phone WHERE id_client = %s""",(str(data_id_client))) 
        work_exec = cursor.fetchall()
        cprint_yellow(work_exec)
        cprint_upred("Редактировать?")
        edit_check = input("Введите ДА для продолжения").upper()
        if edit_check == "ДА":
            cprint_yellow("Введите номер телефона который необходимо отредактировать: ")
            edit_phone_check = phone()
            cursor.execute(""" SELECT id_phone FROM phone WHERE number_phone = %s""",(edit_phone_check,)) 
            work_exec_phone = cursor.fetchall()
            cprint_yellow("Введите новый номер телефона: ")
            new_phone_check = phone()
            cursor.execute ("""UPDATE phone SET number_phone = %s WHERE id_phone = %s""", (new_phone_check, work_exec_phone[0][0]))
            conn.commit()
            cprint_blue(f"Данные клиента отредактированны")
    
    def edit_client_email(data_id_client, edit_firstname, edit_lastname, cursor, conn):
        os.system("clear")
        print(f'В данный момент у клиента {edit_firstname} {edit_lastname} существуют записи о следующих E-Mail адресах:\n')   
        cursor.execute("""SELECT id_email, name_email FROM email WHERE id_client = %s""",(str(data_id_client))) 
        work_exec = cursor.fetchall()
        cprint_yellow(work_exec)
        cprint_upred("Редактировать?")
        edit_check = input("Введите ДА для продолжения").upper()
        if edit_check == "ДА":
            cprint_yellow("Введите E-Mail адрес который необходимо отредактировать: ")
            edit_email_check = email()
            cursor.execute("""SELECT id_email FROM email WHERE name_email = %s""",(edit_email_check))
            work_exec_email = cursor.fetchall()
            cprint_yellow("Введите новый E-Mail адрес: ")
            new_email_check = email()
            cursor.execute ("""UPDATE email SET name_email = %s WHERE id_email = %s""", (new_email_check, work_exec_email[0][0]))
            conn.commit()
            cprint_blue(f"Данные клиента отредактированны")
    
    def del_phone(cursor, conn):
        cprint_yellow("Выбран параметр редактирования номера телефона киента!\n")
        os.system("clear")
        cprint_yellow("Введите Имя и Фамилию клиента запись которого хотте отредактировать")
        work_first_name = first_name()
        work_last_neme = last_name()
        cursor.execute(""" SELECT id_client FROM client WHERE firstname_client = %s AND lastname_client = %s""",(work_first_name, work_last_neme))
        work_exec = cursor.fetchall()
        if work_exec == []:
            cprint_upred("Запись о клиенте отсутствует!")
        else:
            dara_id_client = str(work_exec[0][0])
            cursor.execute(""" DELETE FROM phone WHERE id_client = %s""",(dara_id_client))
            cprint_blue(f"Данные клиента отредактированны")

    def del_client(cursor, conn):
        cprint_yellow("Выбран параметр удаления киента!\n")
        os.system("clear")
        cprint_yellow("Введите Имя и Фамилию клиента запись которого хотите удалить")
        work_first_name = first_name()
        work_last_neme = last_name()
        cursor.execute(""" SELECT id_client FROM client WHERE firstname_client = %s AND lastname_client = %s""",(work_first_name, work_last_neme))
        work_exec = cursor.fetchall()
        if work_exec == []:
            cprint_upred("Запись о клиенте отсутствует!")
        else:
            dara_id_client = str(work_exec[0][0])
            cursor.execute(""" DELETE FROM email WHERE id_client = %s""",(dara_id_client))
            cursor.execute(""" DELETE FROM phone WHERE id_client = %s""",(dara_id_client))
            cursor.execute(""" DELETE FROM client WHERE id_client = %s""",(dara_id_client))
            cprint_blue(f"Данные клиента удалены")

    def search_client(cursor, conn):
        cprint_yellow("Выбран параметр поиска киента!\n")
        os.system("clear")
        work_first_name = first_name()
        work_last_neme = last_name()
        cursor.execute(""" SELECT id_client, firstname_client, lastname_client FROM client WHERE firstname_client = %s AND lastname_client = %s""",(work_first_name, work_last_neme))
        work_exec = cursor.fetchall()
        if work_exec == []:
            cprint_upred("Запись о клиенте отсутствует!")
        else:
            dara_id_client = str(work_exec[0][0])
            cursor.execute(""" SELECT name_email FROM email WHERE id_client = %s""",(dara_id_client))
            work_exec_email = cursor.fetchall()
            cursor.execute(""" SELECT number_phone FROM phone WHERE id_client = %s""",(dara_id_client))
            work_exec_phone = cursor.fetchall()
            cprint_blue(f"Данные которые удалось найти : {work_exec} {work_exec_phone} {work_exec_email}")

def STARTUPDB():
    namedb = config["DATABASE"]["NAME"]
    userdb = config["DATABASE"]["USER"]
    passdb = config["DATABASE"]["PASSWORD"]
    hostdb = config["DATABASE"]["HOST"]
    portdb = config["DATABASE"]["PORT"]

    with psycopg2.connect(database=namedb, user=userdb, password=passdb, host=hostdb,port=portdb) as conn:
        with conn.cursor() as cursor:
            create_tab(cursor)
            performance(cursor, conn)


def start_programm():
    if os.path.exists(configpath) == True:
        cprint_yellow(f"[INFO] Программа запущена!\n\n")
        STARTUPDB()
    else:
        cprint_upred("""По всей вероятности это первый запуск программы. 
Для корректной работы необходимо настроить некоторые параметры, данное действие необходимо сделать однократно.

Приступим!
""")
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
        STARTUPDB()


if __name__ == "__main__":
    start_programm()
