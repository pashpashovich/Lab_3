# создадим пустой словарь для хранения информации о предметах и количестве занятий
subject_dict = {}

# открываем файл "subjects.txt" для чтения
with open("subjects.txt", "r", encoding="utf-8") as file:
    # читаем каждую строку файла
    for line in file:
        parts = line.strip().split(": ")  # разделяем строку по ": "
        if len(parts) == 2:
            subject_name, details = parts  # название предмета и все остальные детали
            lessons = details.split()  # разделяем детали по пробелу
            total_lessons = 0

            for lesson in lessons:
                if lesson.endswith("(л)"):
                    total_lessons += int(lesson[:-3])  # извлекаем количество лекций
                elif lesson.endswith("(пр)"):
                    total_lessons += int(lesson[:-4])  # извлекаем количество практических занятий
                elif lesson.endswith("(лаб)"):
                    total_lessons += int(lesson[:-5])  # извлекаем количество лабораторных занятий

            subject_dict[subject_name] = total_lessons  # записываем инфу о предмете в словарь

print("Название предметов и общее количество занятий по ним в виде словаря:")
# выводим словарь на экран
print(subject_dict)
