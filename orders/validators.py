import re

from django.core.exceptions import ValidationError

cardNamePattern = r"^[A-Za-z ]{2,50}$"
NumberCardPattern = r"^[0-9]{13,19}$"
datePattern = r"^[0-9]{2}/[0-9]{2}$"
cvvPattern = r"^[0-9]{3}$"


def check_luna(field):

    numbers = list(map(int, field))
    numbers.reverse()
    for index in range(len(numbers)):
        if index % 2 != 0:
            numbers[index] = numbers[index] * 2
            if numbers[index] > 9:
                numbers[index] = int(str(numbers[index])[0]) + int(str(numbers[index])[1])
    return sum(numbers) % 10 == 0


def valid_name_card(field: str):
    if field:
        field = field.strip().title()
        if re.match(cardNamePattern, field):
            return field

        else:
            raise ValidationError('Неверная длина имени карты или недопустимые символы')
    else:
        raise ValidationError("Обязательное поле для Заполения")


def valid_number_card(field):
    field = field.replace(' ', '')
    if field:
        if re.match(NumberCardPattern, field) :
            if check_luna(field):
                return field
            else:
                raise ValidationError('Неверная длина номера карты или недопустимые символы Луна')
        else:
            raise ValidationError('Неверная длина номера карты или недопустимые символы')
    else:
        raise ValidationError("Обязательное поле для Заполения")


def valid_date(field):
    if field:
        if re.match(datePattern, field):
            return field
        else:
            raise ValidationError('Неверный формат даты')
    else:
        raise ValidationError("Обязательное поле для Заполения")


def valid_cvv(field):
    if field:
        if re.match(cvvPattern, field):
            return field
        else:
            raise ValidationError('Неверный формат CVV')
    else:
        raise ValidationError("Обязательное поле для Заполения")
