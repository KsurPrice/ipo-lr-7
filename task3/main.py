#Карась Илья
import json  # импортируем модуль для работы с JSON
import os    # импортируем модуль для проверки существования файла

filename = "fish.json"  # имя файла для хранения данных

# если файла нет — создаём его с 5 готовыми записями
if not os.path.exists(filename):  # проверяем, существует ли файл
    fishes = [  # список словарей с начальными данными
        {"id": 1, "name": "Щука", "latin_name": "Esox lucius", "is_salt_water_fish": False, "sub_type_count": 3},  # запись 1
        {"id": 2, "name": "Сельдь", "latin_name": "Clupea harengus", "is_salt_water_fish": True, "sub_type_count": 5},  # запись 2
        {"id": 3, "name": "Карп", "latin_name": "Cyprinus carpio", "is_salt_water_fish": False, "sub_type_count": 4},  # запись 3
        {"id": 4, "name": "Тунец", "latin_name": "Thunnus", "is_salt_water_fish": True, "sub_type_count": 6},  # запись 4
        {"id": 5, "name": "Сом", "latin_name": "Silurus glanis", "is_salt_water_fish": False, "sub_type_count": 2}   # запись 5
    ]
    with open(filename, "w", encoding="utf-8") as f:  # открываем файл для записи
        json.dump(fishes, f, ensure_ascii=False, indent=4)  # сохраняем список в JSON

# загружаем данные из файла
with open(filename, "r", encoding="utf-8") as f:  # открываем файл для чтения
    fishes = json.load(f)  # читаем JSON в список словарей

operations_count = 0  # счётчик операций с записями

# основной цикл программы
while True:  # бесконечный цикл, пока пользователь не выберет выход
    print("\nМеню:")  # выводим меню
    print("1 - Вывести все записи")  # пункт 1
    print("2 - Вывести запись по полю (id)")  # пункт 2
    print("3 - Добавить запись")  # пункт 3
    print("4 - Удалить запись по полю (id)")  # пункт 4
    print("5 - Выйти из программы")  # пункт 5

    choice = input("Введите номер пункта: ")  # ввод выбора пользователя

    if choice == "1":  # если выбрали пункт 1
        print("\nВсе записи:")  # заголовок
        for i, fish in enumerate(fishes, start=1):  # перебираем все записи
            print(f"Позиция {i}: {fish}")  # выводим позицию и саму запись
        operations_count += 1  # увеличиваем счётчик операций

    elif choice == "2":  # если выбрали пункт 2
        search_id = input("Введите id записи: ")  # ввод id для поиска
        found = False  # флаг найденной записи
        for i, fish in enumerate(fishes, start=1):  # перебираем записи
            if str(fish["id"]) == search_id:  # сравниваем id
                print(f"Запись найдена (позиция {i}): {fish}")  # выводим найденную запись
                found = True  # отмечаем, что нашли
                break  # прерываем цикл
        if not found:  # если не нашли
            print("Запись с таким id не найдена.")  # предупреждение
        operations_count += 1  # увеличиваем счётчик операций

    elif choice == "3":  # если выбрали пункт 3
        new_id = int(input("Введите id: "))  # ввод id
        new_name = input("Введите название рыбы: ")  # ввод названия
        new_latin = input("Введите латинское название: ")  # ввод латинского названия
        new_salt = input("Является ли рыба морской? (True/False): ")  # ввод булевого значения
        new_salt = True if new_salt.lower() == "true" else False  # преобразуем строку в bool
        new_subtypes = int(input("Введите количество подвидов: "))  # ввод числа подвидов

        new_fish = {  # создаём словарь новой записи
            "id": new_id,
            "name": new_name,
            "latin_name": new_latin,
            "is_salt_water_fish": new_salt,
            "sub_type_count": new_subtypes
        }
        fishes.append(new_fish)  # добавляем запись в список

        with open(filename, "w", encoding="utf-8") as f:  # открываем файл для записи
            json.dump(fishes, f, ensure_ascii=False, indent=4)  # сохраняем обновлённый список

        print("Запись добавлена.")  # подтверждение
        operations_count += 1  # увеличиваем счётчик операций

    elif choice == "4":  # если выбрали пункт 4
        del_id = input("Введите id записи для удаления: ")  # ввод id для удаления
        found = False  # флаг найденной записи
        for fish in fishes:  # перебираем список
            if str(fish["id"]) == del_id:  # сравниваем id
                fishes.remove(fish)  # удаляем запись
                with open(filename, "w", encoding="utf-8") as f:  # открываем файл для записи
                    json.dump(fishes, f, ensure_ascii=False, indent=4)  # сохраняем обновлённый список
                print("Запись удалена.")  # подтверждение
                found = True  # отмечаем, что нашли
                break  # прерываем цикл
        if not found:  # если не нашли
            print("Запись с таким id не найдена.")  # предупреждение
        operations_count += 1  # увеличиваем счётчик операций

    elif choice == "5":  # если выбрали пункт 5
        print(f"Количество выполненных операций с записями: {operations_count}")  # выводим количество операций
        break  # завершаем цикл (выход из программы)

    else:  # если ввели неверный пункт
        print("Неверный ввод. Попробуйте снова.")  # предупреждение
