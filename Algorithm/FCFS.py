def FCFS(filename):
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


    proces.sort(key=lambda x:x[1]) #sortujemy całą listę, zwiększając czas nadejścia procesu 

    for p in proces:
        if p[1] > general_time: #jeśli nie mamy procesu, który zaczyna się od 0 sekund, to po prostu czekamy
            general_time = p[1] #czekamy i przechodzimy od razu do początku kolejnego procesu, więc przesuwamy czas
        general_time += p[2] #dodaj czas procesu do całkowitego czasu
        processing_time = general_time - p[1] #czas oczekiwania na zakończenie bieżącego procesu
        waiting_time = general_time - p[1] - p[2] #czas oczekiwania bieżącego procesu przed rozpoczęciem następnego
        total_waiting_time += waiting_time # dodajemy czas, jaki bieżący proces musiał czekać przed rozpoczęciem, do całkowitego czasu oczekiwania, abyśmy mogli później obliczyć średni czas oczekiwania
        total_processing_time += processing_time #to samo robimy z czasem procesu 

    avarage_processing_time = total_processing_time / len(proces)
    avarage_waiting_time = total_waiting_time / len(proces)

    print("TotalProcesingTime:", total_processing_time)
    print("TotalWaitingTime:", total_waiting_time)
    print('TurnaroundTime',round(avarage_processing_time, 1))
    print('WaitingTime', round(avarage_waiting_time, 1))







