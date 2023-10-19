# Функция для перевода английских числительных в русские
def translate_number(number):
    translation_dict = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре"
    }
    return translation_dict.get(number, number)  # возвращаем значение с ключом number,
    # если он есть, и если нет, то возвращаем значение само number

# Открываем исходный файл для чтения и создаем новый файл для записи
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        parts = line.strip().split(" - ")  # убираем лишние пробелы и запихиваем в список
        if len(parts) == 2:
            english_number, value = parts
            russian_number = translate_number(english_number)
            output_line = f"{russian_number} — {value}\n"
            output_file.write(output_line)

print("Перевод завершен. Результат записан в output.txt")
print("Содержимое файла output.txt:")
with open("output.txt", "r") as output_file:
    result = output_file.read()
    print(result)
