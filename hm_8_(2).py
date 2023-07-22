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
    volume VARCHAR(100),
    UNIQUE(license_plate) ON CONFLICT IGNORE
);
""")

class Check:
    def __init__(self):
        self.login = None

    def add_car(self, license_plate, brand, model, year, color, rudder_location, volume):
        try:
            cursor.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?);", 
                           (license_plate, brand, model, year, color, rudder_location, volume))
            connection.commit()
            print("Успешно добавлено!")
        except sqlite3.IntegrityError:
            print("Машина с таким номером уже существует.")

    def find_car(self, license_plate):
        cursor.execute("SELECT * FROM cars WHERE license_plate=?;", (license_plate,))
        result = cursor.fetchall()
        print("------------------------------")
        if result:
            print(f"Результат {result[0][0]}\nМарка: {result[0][1]}\nМодель {result[0][2]}\nГод: {result[0][3]}\nЦвет: {result[0][4]}\nРасположение руля: {result[0][5]}\nОбъем: {result[0][6]}")
        else:
            print("Данные отсутвуют")

    def update_car(self, license_plate, brand, model, year, color, rudder_location, volume):
        query = "UPDATE cars SET brand=?, model=?, year=?, color=?, rudder_location=?, volume=? WHERE license_plate=?"
        values = (brand, model, year, color, rudder_location, volume, license_plate)
        cursor.execute(query, values)
        connection.commit()
        print("Данные успешно обновлены!")

    def delete_car(self, license_plate):
        cursor.execute("DELETE FROM cars WHERE license_plate=?;", (license_plate,))
        connection.commit()
        print("------------------------------")
        print("Данные успешно удалены!")

    def main(self):
        while True:
            command = input("1 - проверить машину, 2 - добавить, 3 - обновить, 4 - удалить: ")
            if command == "1":
                license_plate = input("Номер машины, которую нужно найти: ")
                self.find_car(license_plate)
                print("------------------------------")
            elif command == "2":
                print("Вы добавляете машину в базу")
                license_plate = input("Номер машины: ")
                brand = input("Марка машины: ")
                model = input("Модель машины: ")
                year = int(input("Год машины: "))
                color = input("Цвет машины: ")
                rudder_location = input("Расположение руля машины: ")
                volume = input("Объем машины: ")
                self.add_car(license_plate, brand, model, year, color, rudder_location, volume)
            elif command == "3":
                print("Вы обновляете данные машины в базе")
                license_plate = input("Номер машины: ")
                brand = input("Марка машины: ")
                model = input("Модель машины: ")
                year = int(input("Год машины: "))
                color = input("Цвет машины: ")
                rudder_location = input("Расположение руля машины: ")
                volume = input("Объем машины: ")
                self.update_car(license_plate, brand, model, year, color, rudder_location, volume)
            elif command == "4":
                print("Вы удаляете машину из базы")
                license_plate = input("Номер машины, которую нужно удалить: ")
                self.delete_car(license_plate)
            else:
                print("Неверная команда. Пожалуйста, выберите одну из доступных команд.")

check = Check()
check.main()