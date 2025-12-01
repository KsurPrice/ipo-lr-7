#Карась Илья
import json #Импортируем пакет для работы с json

with open("dump.json", encoding="utf-8") as f: #открываем файл
    data = json.load(f) # записываем его

query = input("Введите номер квалификации: ").strip().lower() #вводим код специальности

found = [] # пустой список для результата

for item in data: #перебираем нужные элементы
    if item.get("model") != "data.skill": # Берём только квалификации
        continue

    fields = item.get("fields", {}) # поле с информацией о квалификации
    code = fields.get("code", "") # поле с информацией о квалификации
    title = fields.get("title", "") # поле с информацией о квалификации
    type_ = fields.get("type", "") # поле с информацией о квалификации

    if query in code.lower(): # если query есть с таким кодом специальности
        if "специальность" in title.lower(): # если слово спец-ть в title
            found.append(f'{code} >> Специальность "{title}", {type_}' if type_ else f'{code} >> Специальность "{title}"') # добавляем информацию в список
        else:
            found.append(f'{code} >> Квалификация "{title}"') #Квалификацию

if found: #Если в списке есть элементы выводим информацию
    print("=============== Найдено ===============")
    for line in found:
        print(line)
else: #Если нет то не выводим
    print("=============== Не найдено ===============")
