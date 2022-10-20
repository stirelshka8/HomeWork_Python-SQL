import psycopg2
import os
import re

os.system("clear")

phonere = re.compile(r'[+]\d\d{10}')
emailre = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

#ЦВЕТНОЙ ТЕКСТ

def cprint_upred(text):
    print("\033[1m\033[31m{}\033[0m".format(text))
def cprint_yellow(text):
    print("\033[33m{}\033[0m".format(text))
def cprint_blue(text):
    print("\033[34m{}\033[0m".format(text))


def performance():
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
        Working_Database.add_client()
    elif selection == 2 and selection <= 6:
        cprint_upred("Два")
    elif selection == 3 and selection <= 6:
        cprint_upred("Три")
    elif selection == 4 and selection <= 6:
        cprint_upred("Четыре")
    elif selection == 5 and selection <= 6:
        cprint_upred("Пять")
    elif selection == 6 and selection <= 6:
        cprint_upred("Шесть")

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
    def __init__(self) -> None:
        pass

    def add_client():
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


if __name__ == "__main__":
    with psycopg2.connect(database="client_db", user="postgres", password="7702293", host="192.168.1.111") as conn:
        with conn.cursor() as cursor:
            create_tab(cursor)
            performance()
