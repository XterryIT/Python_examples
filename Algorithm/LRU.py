def LRU(filename):
    ProcesList = [] #nasza lista z numerami (strony)
    hit = 0 #liczba hitów
    miss = 0 # liczba misów
    Queue = [] #naszą listę zadań, na której liczby będą pojawiać się i znikać
    history = [] # to nasza koleja liczb na wejście na listę prac
    temp = [] # to zminna lista ktora służy do wyznaczenia, ktorą liczbe potrzebnie usunąć z listy prac
    capasity = 4  # długość naszej listy roboczej
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
            history.insert(0, ProcesList[i]) # również dodajemy wszystkie liczby do historii
            miss+=1
    
 # w tej pętli wykonywany jest nasz algorytm 
    for j in range(capasity, len(ProcesList)):
        temp = []
        history.insert(0, ProcesList[j])

   # tutaj sprawdzamy, czy numer przychodzący odpowiada numerom na liście roboczej
        for x in Queue:
            if x == ProcesList[j]:
                hit+=1
                m = 1 # jeśli nasze liczby zgadzają się z liczbami na liście prac, to ustawiamy m na 1, aby ta liczba nie wchodziła dalej w obliczanie misów 
                break

     #tutaj zamieniamy numery na otrzymane, jeśli nie zgadzają się z numerami na liście prac
        if m != 1:
            miss+=1   
            for x in Queue:
                for p in history:
                    if p in Queue:
                        if p not in temp:
                            temp.append(p) # dodajemy do zminnej temp liczby z Queue i ostatnia liczba będzie na zmianę
                # Zmieniamy liczbę na liczbę którą obecnie iterujemy czyli j
                DeleteElement = temp[len(temp)-1]

                Queue.remove(DeleteElement)

                Queue.append(ProcesList[j])
                break    
        else:
            m = 0

    
    hitrate = (hit / len(ProcesList)) * 100 
    missrate = (miss / len(ProcesList)) * 100

    print("hit:",hit)
    print("miss",miss)
    print("hitrate:",round(hitrate, 1),"%")
    print("missrate:",round(missrate, 1),"%")

