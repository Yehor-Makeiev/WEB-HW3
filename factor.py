import time
from multiprocessing import Pool, cpu_count

def factorize(number):
    results = []
    for i in range(1, number + 1):
        if number % i == 0:
            results.append(i)
    return results

def new_factorize(numbers):
    pool = Pool(cpu_count())
    result = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return result

def f_sync(numbers) -> None:
    result = []
    start_time = time.time()
    for num in numbers:
        res = factorize(num)
        result.append(res)
    end_time = time.time()
    return f'{numbers} work for {end_time - start_time}', print(res)

def f_async(numbers) -> None:
    start_time = time.time()
    res = new_factorize(numbers)
    end_time = time.time()
    return f'{numbers} work for {end_time - start_time}', print(res)



if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    print(f_sync(numbers))
    print(f_async(numbers))
