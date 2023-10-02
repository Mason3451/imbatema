def print_star_digits():
    star_digits = {
        '0': [
            '  ***  ',
            ' *   * ',
            '*     *',
            '*     *',
            '*     *',
            ' *   * ',
            '  ***  '
        ],
        '1': [
            '   *   ',
            '  **   ',
            ' * *   ',
            '   *   ',
            '   *   ',
            '   *   ',
            ' ***** '
        ],
        '2': [
            '  ***  ',
            ' *   * ',
            ' *  *  ',
            '   *   ',
            '  *    ',
            ' *     ',
            ' ***** '
        ],
        '3': [
            ' ***** ',
            '     * ',
            '     * ',
            '  **** ',
            '     * ',
            '     * ',
            ' ***** '
        ]
    }
    number = input("Введите число (0, 1, 2 или 3): ")
    if number in star_digits:
        for line in star_digits[number]:
            print(line)
    else:
        print("Некорректный ввод. Введите число 0, 1, 2 или 3.")

print_star_digits()