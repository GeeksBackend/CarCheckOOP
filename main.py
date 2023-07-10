import sqlite3

connection = sqlite3.connect('carcheck.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cars (
    license_plate VARCHAR(10),
    brand VARCHAR(200),
    model VARCHAR(200),
    year INTEGER,
    color VARCHAR(100),
    rudder_location VARCHAR(50),
    volume VARCHAR(100)
);
""")

class Check:
    def __init__(self):
        self.login = None

    def add_car(self, license_plate, brand, model, year, color, rudder_location, volume):
        cursor.execute(f"""INSERT INTO cars VALUES ('{license_plate}', '{brand}', '{model}', {year}, 
                       '{color}', '{rudder_location}', '{volume}');""")
        cursor.connection.commit()
        print("Успешно добавлено!")

    def find_car(self, license_plate):
        cursor.execute(f"SELECT * FROM cars WHERE license_plate='{license_plate}';")
        result = cursor.fetchall()
        print("------------------------------")
        if result != []:
            print(f"Результат {result[0][0]}\nМарка: {result[0][1]}\nМодель {result[0][2]}\nГод: {result[0][3]}\nЦвет: {result[0][4]}\nРасположение руля: {result[0][5]}\nОбъем: {result[0][6]}")
        else:
            print("Данные отсутвуют")

    def main(self):
        while True:
            command = input("1 - проверить машину, 2 - добавить, 3 - обновить, 4 - удалить: ")
            if command == "1":
                license_plate = input("Номер машины которую нужно найти: ")
                self.find_car(license_plate)
                print("------------------------------")
            elif command == "2":
                print("Вы добавляете в базу машину")
                license_plate = input("Номер машины: ")
                brand = input("Марка машины: ")
                model = input("Модель машины: ")
                year = int(input("Год машины: "))
                color = input("Цвет машины: ")
                rudder_location = input("Расположение руля машины: ")
                volume = input("Объем машины: ")
                self.add_car(license_plate, brand, model, year, color, rudder_location, volume)

check = Check()
check.main()