import expect
def main():
    try:
        user = expect.Expect(fp = input("Введите путь к файлу: ").strip('"\',.:; '),
                             expc = ['Вид расчета', 'Cash-back', 'Время оплаты', 'Дата оплаты', 'Терминал оплаты', 'Результат операции', 'Сумма операции', 'Место оплаты', 'Сумма cash-back', 'Тип операции', 'Участники гражданского оборота'],
                             expt = {'Вид расчета': str, 'Cash-back' : float, 'Время оплаты' : str, 'Дата оплаты' : str, 'Терминал оплаты' : str, 'Результат операции' : str, 'Сумма операции' : float, 'Место оплаты' : str, 'Сумма cash-back' : float, 'Тип операции' : str, 'Участники гражданского оборота' : str})
        print(user.validate())    
    except ValueError as e:
        print("Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        
if __name__ == "__main__":
    main()