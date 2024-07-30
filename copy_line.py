def copy_line(source_file, target_file, line_number):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()
            if line_number > len(lines) or line_number <= 0:
                print(f"Номер строки {line_number} вне диапазона. Файл содержит {len(lines)} строк.")
                return

        line_to_copy = lines[line_number - 1]

        with open(target_file, 'a') as tgt:
            tgt.write(line_to_copy)

        print(f"Строка {line_number} успешно скопирована из '{source_file}' в '{target_file}'.")

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    source_file = input("Введите имя файла-источника: ")
    target_file = input("Введите имя файла-назначения: ")
    line_number = int(input("Введите номер строки для копирования: "))

    copy_line(source_file, target_file, line_number)
