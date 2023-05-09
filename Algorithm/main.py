import FCFS
import SJF
import FIFO
import LRU

def main():
    filename1 = 'test_data_1.txt'
    filename2 = 'test_data_2.txt'

#  =========== FCFS ===============
    print('=========== FCFS ===============')
    FCFS.FCFS(filename1)

#  =========== SJF ===============
    print('=========== SJF ===============')
    SJF.SJF(filename1)

#  =========== FIFO ===============
    print('=========== FIFO ===============')
    FIFO.FIFO(filename2)

#  =========== LRU ===============
    print('=========== LRU ===============')
    LRU.LRU(filename2)


if __name__ == '__main__':

    main()