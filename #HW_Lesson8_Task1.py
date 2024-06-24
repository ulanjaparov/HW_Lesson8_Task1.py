# HW_Lesson8_Task1

# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
# Формат сдачи: ссылка на свой репозиторий.

def copy_line(source_file, target_file, line_number):
    try:
        # Открываем исходный файл для чтения
        with open(source_file, 'r') as f_source:
            # Читаем все строки в список
            lines = f_source.readlines()

            # Проверяем, что введенный номер строки корректен
            if line_number < 1 or line_number > len(lines):
                print(f"Строка с номером {line_number} не существует в файле {source_file}.")
                return

            # Определяем индекс строки (с учетом индексации с 0)
            index_to_copy = line_number - 1
            line_to_copy = lines[index_to_copy]

            # Открываем целевой файл для записи (режим добавления 'a' для добавления в конец файла)
            with open(target_file, 'a') as f_target:
                # Записываем строку в целевой файл
                f_target.write(line_to_copy)
                print(f"Строка из файла {source_file} c номером {line_number} успешно скопирована в файл {target_file}.")

    except FileNotFoundError:
        print("Один из указанных файлов не найден.")
    except IOError as e:
        print(f"Произошла ошибка ввода-вывода: {e}")

# Пример использования функции
if __name__ == "__main__":
    source_file = "source.txt"
    target_file = "target.txt"
    
    # Предположим, что пользователь вводит номер строки
    line_number_to_copy = int(input("Введите номер строки для копирования из исходного файла: "))
    
    # Вызываем функцию копирования строки
    copy_line(source_file, target_file, line_number_to_copy)