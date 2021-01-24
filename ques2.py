import multiprocessing as mp
import time

with open("words.txt") as f:
    data = f.read()


def pali(words):
    pal = []
    for i in words:
        pal.append(i == i[::-1])
    return pal


def splitarr(arr):
    lists, length = [], len(arr)
    for i in range(8):
        lists.append(arr[((length//8)*(i)):((length//8)*(i+1))])
    return lists


if __name__ == '__main__':
    words = [s.lower() for s in data.split('\n')]
    words[:20]

    start = time.time()
    result = pali(words)

    print(result[:20])
    print(time.time()-start)

    lists = splitarr(words)
    len(lists), len(lists[0]), len(words)

    start = time.time()
    pool = mp.Pool(processes=8)
    result = pool.map(pali, lists)

    print(time.time()-start)
