#multiprocessing launches separate python processes that don't necessarily talk to each other
#this project is now on Python 3.6 64-bit
import multiprocessing
from multiprocessing import Pool

def spawn(num,num2):
    print('Spawned! {} {}'.format(num,num2))

def job(num):
    return num * 2


if __name__ == '__main__':
    # for i in range(50):
    #     p = multiprocessing.Process(target=spawn, args=(i,i+3))
    #     p.start()

        #wait for the process to be complete
        #prints stuff 1 at a time if joined
        #500 processes maxes the cpu when not joined, goes up to 40% when joined
        #p.join()

    p = Pool(processes=20)
    data = p.map(job, range(20))
    data2 = p.map(job, [1,2,3,4])
    p.close()
    print(data)
    print(data2)


