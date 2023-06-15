def ritm(str):
    str = str.split(" ") #разбили строку на слова по пробелам
    list_slogi = [] #список слогов в словах строки
    for word in str: #проверяем каждое слово в строке
        slogi = 0
        for i in word:
            if i in 'аеёиоуыэюя': #если встречается гласная в слове, делаем +слог
                slogi += 1
        list_slogi.append(slogi) #добавляем количество слогов слова в список
    return len(list_slogi) == list_slogi.count(list_slogi[0]) #сравниваем количество элементов в списке слогов с количеством элементов в списке с одинаковыми слогами

str = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

if ritm(str):
     print('Парам пам-пам')
else:
     print('Пам парам')