from random import randint 

def gen_proc_1():
    
    all_proces_1=[] #создаем список процессов 

    for item in range(50): #с помощью этого цикла мы будем создовать элементы(процессы) нашего списка (их число можно изменить, я поставил 5)
#рандомно выставляем числа прибытия процесса и время его работы 
        BurstTime = randint(0, 20) 
        ArrivalTime = randint(1, 20) 

#создаем внутри списка картеж куда вписываем все данные процессов 
        all_proces_1.append({
            'ProcessName': f'P{item+1}',
            'BurstTime': BurstTime,
            'ArrivalTime': ArrivalTime,
        })

    return all_proces_1

def save_txt_1():
    answer = gen_proc_1() #помещаем список в переменную для удобства работы 
    print(gen_proc_1())
    file = open('test_data_1.txt', 'w') #открываем файл 
#поочередно записываем каждый элемент картежа ореинтрируясь на ключи     
    for i in range(len(answer)): 
        file.write(answer[i]['ProcessName'])
        file.write(" ")
        file.write(str(answer[i]['ArrivalTime']))
        file.write(" ")
        file.write(str(answer[i]['BurstTime']))
        file.write("\n")


def gen_proc_2():

    all_proces_2=[] #utwórz listę stron
    
    #wygeneruj losowe liczby i zapełnij naszą listę
    for number in range(1, 51):
        all_proces_2.append(randint(0, 20)) 

    return all_proces_2

def save_txt_2():
#zapisujemy wszystkie nasze numery do pliku tekstowego
    answer = gen_proc_2()
    
    print(gen_proc_2())
    
    file = open('test_data_2.txt', 'w')

    for j in range(len(answer)):
        file.write(str(answer[j]))
        file.write("\n")


save_txt_1()
save_txt_2()
