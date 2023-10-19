import json

# открываем файл для чтения
with open("companies.txt", "r", encoding="utf-8") as file:
    companies_data = file.readlines()


profit_data = dict()
total_profit = 0
profit_count = 0

# обработка данных о компаниях и вычисление прибыли
for line in companies_data:
    parts = line.strip().split()  # записываем данные о фирме в виде списка
    if len(parts) == 4:
        firm_name, ownership, revenue, expenses = parts  # получчаем название фирмы, форма собственности,
        # выручка, издержки в виде строк
        revenue = int(revenue)  # выручка
        expenses = int(expenses)  # издержки
        profit = revenue - expenses  # прибыль
        profit_data[firm_name] = profit
        if profit >= 0:
            total_profit += profit
            profit_count += 1


# вычисление средней прибыли
if profit_count > 0:
    average_profit = total_profit / profit_count
else:
    average_profit = 0

# создание списка, содержащего словарь с прибылью каждой фирмы и средней прибылью
result_list = [profit_data, {"average_profit": average_profit}]

# сохранение списка в формате JSON в файл
with open("result.json", "w", encoding="utf-8") as json_file:
    json.dump(result_list, json_file)

print("Результат сохранен в result.json")
