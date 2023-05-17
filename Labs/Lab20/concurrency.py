from time import sleep
from threading import Thread
from queue import Queue

#Producer function uses ranger to enter the data
def producer(queue):
    for i in range(6):
        sleep(1)
        queue.put(i)
        print("Producer:", i)      

#Consuper is using the get function and task_done function 
#to process the data
def consumer(queue):
    for i in range(6):
        item = queue.get()
        queue.task_done()
        sleep(2)
        print("Consumer:", item)

#Initializing the queue that will be used for both functions
queue = Queue()


t1 = Thread(target=lambda: producer(queue))
t2 = Thread(target=lambda: consumer(queue))

#Starting the threads with the queue
t1.start()
t2.start()

#Joining both threads
t1.join()
t2.join()
