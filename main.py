import threading,time
from src.word_program import check_count
from src.password_program import passvalidate
from src.Queue_program import CircularQueue

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
def wordprogram():
    input_file_path ='word_file.txt'
    line = read_input_from_file(input_file_path)
    sorted_cn = check_count(line)
    #print_word_frequency(sorted_cn)
    # print(sorted_cn)
    for i,j in sorted_cn:
        print((i,j))

def passprogram():
    input_file_path = 'password_file.txt'
    pass_list=read_input_from_file(input_file_path)
    print(passvalidate(pass_list))


def queue_program():
    queue = CircularQueue(5)
    for i in range(1, 8):
        queue.enqueue(i)
    queue.display()

if __name__=="__main__":

    threads=[]
    threads.append(threading.Thread(target=passprogram))
    threads.append(threading.Thread(target=wordprogram))
    threads.append(threading.Thread(target=queue_program))
    print(threads)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()