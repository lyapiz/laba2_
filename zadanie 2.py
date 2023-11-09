def process_input(input_arg):
    if isinstance(input_arg, dict):
        if not input_arg:
            print("Словарь пуст")
        else:
            min_key = min(input_arg, key=input_arg.get)
            print(f"Ключ с минимальным значением: {min_key}")
    elif isinstance(input_arg, list):
        if len(input_arg) >= 2:
            zero_indices = [i for i, x in enumerate(input_arg) if x == 0]
            if len(zero_indices) >= 2:
                result = input_arg[zero_indices[0]] * input_arg[zero_indices[1]]
                print(f"Произведение между первым и вторым нулевыми элементами: {result}")
            else:
                print("Недостаточно нулевых элементов в списке")

        input_arg = list(set(input_arg))
        print(f"Список без повторяющихся элементов: {input_arg}")
    elif isinstance(input_arg, int):
        if input_arg < 1:
            print("Число должно быть положительным")
        else:
            print(f"Делители числа {input_arg}: {[i for i in range(1, input_arg + 1) if input_arg % i == 0]}")
    elif isinstance(input_arg, str):
        if input_arg == input_arg[::-1]:
            print("Строка является палиндромом")
        else:
            print("Строка не является палиндромом")

        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowel_count = sum(1 for char in input_arg if char in vowels)
        consonant_count = sum(1 for char in input_arg if char in consonants)

        print(f"Количество гласных: {vowel_count}")
        print(f"Количество согласных: {consonant_count}")
    else:
        print("Неизвестный тип аргумента")


input_dict = {'a': 3, 'b': 1, 'c': 2}
input_list = [1, 2, 0, 3, 0, 4, 5]
input_int = 12
input_str = "racecar"

process_input(input_dict)
process_input(input_list)
process_input(input_int)
process_input(input_str)