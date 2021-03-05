import _thread
import threading
import logging
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(5)
#     logging.info("end loop0 at " + ctime())
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(3)
#     logging.info("end loop1 at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     # loop0()
#     # loop1()
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1,())
#     sleep(6)
#     logging.info("end all at " + ctime())
#
# if __name__=='__main__':
#     main()

'''
loops=[3,7]
def loop(nloop,nsec,lock):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())
    lock.release()

def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at " + ctime())

if __name__=='__main__':
    main()
'''

# loops=[3,7]
# def loop(nloop,nsec):
#     logging.info("start loop " + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop " + str(nloop) + " at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t = threading.Thread(target=loop,args=(i,loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     logging.info("end all at " + ctime())
#
# if __name__=='__main__':
#     main()

loops=[3,7]
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__=='__main__':
    main()