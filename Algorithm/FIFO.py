def FIFO(filename):
    ProcesList = [] #nasza lista z numerami (strony)
    hit = 0 #liczba hitów
    miss = 0 # liczba misów
    Queue = [] #naszą listę zadań, na której liczby będą pojawiać się i znikać
    IndexOfQueueValue = 0 # indeksuj każdy element listy roboczej(Queue)
    capasity = 4 # długość naszej listy roboczej
    m = 0 # służy temu, aby ten sam numer nie został użyty 2 razy (w obliczaniu hitow i missow)

    # otworzamy plik i stamtąd pobierzamy wartości 
    with open(filename, 'r') as file:
        for line in file:
            temp = line[:-1]
            ProcesList.append(temp)
    # zamieniamy te wartości na int        
    ProcesList = list(map(int, ProcesList))


    #w tym cyklu uzupełniamy naszą listę prac
    for i in range(capasity):
        if len(Queue) < capasity:
            Queue.append(ProcesList[i])
            miss+=1
    
    # w tej pętli wykonywany jest nasz algorytm 
    for j in range(capasity, len(ProcesList)):

        # tutaj sprawdzamy, czy numer przychodzący odpowiada numerom na liście roboczej
        for x in Queue:
            if x == ProcesList[j]:
                hit+=1
                m = 1 # jeśli nasze liczby zgadzają się z liczbami na liście prac, to ustawiamy m na 1, aby ta liczba nie wchodziła dalej w obliczanie misów
                break

        #tutaj zamieniamy numery na otrzymane, jeśli nie zgadzają się z numerami na liście prac
        if m != 1:
            for x in Queue:
                Queue[IndexOfQueueValue] = ProcesList[j]
                IndexOfQueueValue += 1 #zwiększamy w nieskończoność nasz indeks o 1
                miss+=1
                # jeśli indeks jest większy niż długość listy roboczej (capasity), to resetujemy go do zera, wracając tym samym do najstarszego elementu
                if IndexOfQueueValue > (capasity - 1):
                    IndexOfQueueValue = 0 
                break
        else:
            m = 0

    
    hitrate = (hit / len(ProcesList)) * 100
    missrate = (miss / len(ProcesList)) * 100


    print("hit:",hit)
    print("miss:",miss)
    print('hitrate:' ,round(hitrate, 1),"%")
    print("missrate:",round(missrate, 1),"%")



