# Метод кодирования строки
def encode(string):
    dictionary = list(letter_dictionary)  # Словарь, в который будут записываться все подстроки (в него уже занесены все символы строки)

    processed_char = ""  # Переменная, которая будет отвечать за символ/подстроку, который будет находиться в процессе обработки.
    encode_list = list()  # Финальный лист с закодированным словом

    for char in string:  # Проходимся по всем символам в строке
        substring = processed_char + char  # Соединяем рабочую подстроку с обрабатываемым символом
        if substring in dictionary:  # Если подстрока есть в словаре
            processed_char = substring  # Тогда переходим к следующему символу в строке
        else:
            encode_list.append(dictionary.index(processed_char) + 1)  # Записываем в наш финальный лист код подстроки, который достаем из словаря
            dictionary.append(substring)  # В общий словарь добавляем подстроку
            processed_char = char  # Обрабатываемой строкой становиться символ строки

    if processed_char != '':  # Проверяем, чтобы введённая строка была полностью закодирована, если это не так, то кодируем оставшуюся подстроку.
        encode_list.append(dictionary.index(processed_char) + 1)

    return encode_list


# Метод декодирования строки
def decode(encode_list: list):
    output = ""  # Декодированная срока

    dictionary = list(letter_dictionary)  # Словарь, в который будут записываться все подстроки (и уже в нём есть все буквы)

    char_code = encode_list.pop(0) - 1  # Берём первый элемент
    output += dictionary[char_code]  # Берём его из словаря, он точно там будет, потому что кодирование начинали мы именно с него
    dictionary.append(dictionary[char_code])  # Для дальнейшего формирования словаря мы добавляем его в общий словарь

    while len(encode_list) != 0:  # Пока словарь из кодов не будет пустым
        char_code = encode_list.pop(0) - 1  # Берём код (вычитаем единицу, чтобы взять правильный символ в словаре)
        dictionary[-1] = dictionary[-1] + dictionary[char_code][0]  # Добавляем к последнему добавленному символу новую часть подстроки
        output += dictionary[char_code]  # К выходной строке добавляем подстроку, ктороая уже есть в общем словаре
        dictionary.append(dictionary[char_code])  # # Для дальнейшего формирования словаря мы добавляем его в общий словарь

    return output


if __name__ == '__main__':
    file = open('text.txt', 'r').read()
    print("Введенная строка: " + file)

    letter_dictionary = list(sorted(set(list(file))))  # Делаем базовый словарь всех букв в введенной строке и сортируем их по алфавиту

    encoded_string = encode(file)
    print("Закодированная строка (массив): ")
    print(encoded_string)

    decoded_string = decode(encoded_string)
    print("Раскодированная строка: " + decoded_string)
