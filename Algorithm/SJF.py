
def sortingProces(List):
#sotujemy naszą listę według czasu pracy    
    for j in range(len(List)-1):
        for i in range(1 ,len(List)-1):# pominięcie 1 elementu listy
            if List[i][2]>List[i+1][2]:
                List[i],List[i+1]=List[i+1],List[i]
    return List    

def processesInQueue(List, Time):   # ta funkcja wykonuje zadanie kolejki, w której znajdują się procesy przed ich wykonaniem 
    ListToReturn=[] # utwórz listę, którą zamierzamy zwrócić
    counter=0 
    for line in List:  
        if line[1]<=Time:   # jeśli czas rozpoczęcia jest krótszy niż czas bieżący, proces już czeka w kolejce
            ListToReturn.append([])    # tworzenie listy wewnątrz innej listy, a następnie dodawanie procesów do naszej listy jeden po drugim
            ListToReturn[counter].append(List[counter][0])  
            ListToReturn[counter].append(List[counter][1]) 
            ListToReturn[counter].append(List[counter][2]) 
            counter+=1  #counter do iteracji linii
    ListToReturn.sort(key=lambda x:x[2])    # sortujemy listę według czasu wykonania, ponieważ w algorytmie SJF najkrótsze zadanie jest na pierwszym miejscu
    return(ListToReturn)



def SJF(filename):
    proces=[] #lista wszystkich procesów
    counter = 0 #oznacza numer wiersza pasujący do listy procesów
    general_time = 0 # czas całkowity 
    total_waiting_time = 0 #całkowity czas oczekiwania
    total_processing_time = 0 #łączny czas wykonania wszystkich procesów

    with  open(filename, 'r') as file: # otwórzamy plik do odczytu 
        for line in file: #iteruj przez wszystkie wiersze pliku, aby przekonwertować i zapisać je na liście procesów
            processName,processArrival,processDuration  = line.split() #uzyskanie nazwy, czasu przybycia i czasu trwania bieżącego procesu
            proces.append([])    #tworzenie listy wewnątrz innej listy
            proces[counter].append(processName)  #dodajemy nazwę jako pierwszy element podlisty procesów
            proces[counter].append(int(processArrival))  #dodajemy czas przybycia procesu do tej samej podlisty co element 2
            proces[counter].append(int(processDuration)) # dodaj czas procesu do tej samej podlisty co element 3
            counter += 1 # przechodzimy do następnej linii

    lenproces = len(proces)
    proces.sort(key=lambda x:x[1]) #sortujemy całą listę, zwiększając czas nadejścia procesu 

# tutaj zaczyna się nasz algorytm SJF
    for i in range(len(proces)):
        if general_time < proces[0][1]: #jeśli nie mamy procesu z krótkim czasem przybycia równym 0, to natychmiast przenosimy czas do następnego procesu
            general_time+=proces[0][1] 
        for j in range(len(proces)):
            if proces[j] == processesInQueue(proces,general_time)[0]: #szukamy procesu o najmniejszym czasie przetwarzania, który aktualnie znajduje się w kolejce. więc porównujemy listę wszystkich ze zwrotem funkcji, która podaje nam procesy w kolejce
        #zamień te dwa procesy. nie ma znaczenia, gdzie trafi pierwszy, nadal będzie posortowany według funkcji    
                temp = proces[0] 
                proces[0] = proces[j]
                proces[j] = temp
        general_time += proces[0][2] #dodajemy czas procesu do całkowitego czasu
        processing_time = general_time - proces[0][1] #czas oczekiwania na zakończenie bieżącego procesu
        waiting_time = general_time - proces[0][1] - proces[0][2] #czas oczekiwania bieżącego procesu przed rozpoczęciem następnego
        total_waiting_time += waiting_time # dodajemy czas, jaki bieżący proces musiał czekać przed rozpoczęciem, do całkowitego czasu oczekiwania, abyśmy mogli później obliczyć średni czas oczekiwania
        total_processing_time += processing_time #to samo robimy z czasem procesu 
        proces.pop(0)# usuwamy procesy z naszej listy żeby nie było powrtrzeń

    avarage_processing_time = total_processing_time / lenproces
    avarage_waiting_time = total_waiting_time / lenproces


    print("TotalProcesingTime:", total_processing_time)
    print("TotalWaitingTime:", total_waiting_time)
    print('TurnaroundTime',round(avarage_processing_time, 1))
    print('WaitingTime', round(avarage_waiting_time, 1))



