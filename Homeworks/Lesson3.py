months = {1: 'Январь' , 2: 'Февраль' , 3: 'Март' , 4: 'Апрель' , 5: 'Май' , 6: 'Июнь' ,7: 'Июль' ,8: 'Август' , 9: 'Сентябрь' ,
          10: 'Октябрь' , 11: 'Ноябрь' , 12: 'Декабрь'}
def pecat_mesyaca(n):
    print(months[n])
    while True:
        try:
            pecat_mesyaca(int(input('Введите номер месяца: \n')))
        except:
            break
