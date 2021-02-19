from itertools import islice
from itertools import chain, combinations

# MAKE POWER SET


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


pset1 = powerset(list(range(1, 11)))
pset2 = powerset(list(range(1, 11)))

# DIVIDE POWERSET

splitlist = [list(islice(pset1, elem)) for elem in [8]*((2**10-1)//8)]

# print(splitlist)

# make function


def prime(t_list):
    find_prime = []
    for i in t_list:
        find_prime.append(isPrime(sum(i)))
    return find_prime


def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return num
    else:
        return False


# MULTI PROCESS
if __name__ == "__main__":
    import multiprocessing

    pool = multiprocessing.Pool(processes=4)

    import time

    now = time.time()
    prime(list(pset2))
    print("Linear %0.5f" % (time.time()-now))

    # took 0.0032045841217041016

    now = time.time()
    pool.map(prime, splitlist)
    print("Pooled %0.5f" % (time.time()-now))

    # took 0.002752065658569336
