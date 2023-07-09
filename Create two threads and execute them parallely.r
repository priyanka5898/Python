#Q.1 Write a program to create two threads and execute them parallelly. 
import threading 
# define a funcƟon to be executed by the threads
def thread_funcƟon(name):
 print("Thread {} is starƟng...".format(name))
 # do some work here... 
 print("Thread {} is finishing...".format(name)) 
# create two threads and start them 
t1 = threading.Thread(target=thread_funcƟon, args=("1",))
t2 = threading.Thread(target=thread_funcƟon, args=("2",))
t1.start() 
t2.start() 
# wait for the threads to finish 
t1.join() 
t2.join() 
print("All threads have finished.") 