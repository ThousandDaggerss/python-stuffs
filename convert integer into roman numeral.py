class converter:
    def int_to_roman(self, num):
        valor = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_number = ''
        i = 0
        while num > 0:
            for _ in range(num // valor[i]):
                roman_number += symbol[i]
                num -= valor[i]
            i += 1
        return f'Number: {number} | Roman Number: {roman_number}'

number = int(input('Enter a number to convert to roman number: '))
print(converter().int_to_roman(number))
