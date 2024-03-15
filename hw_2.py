"""
Задание №7.
� Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений.
"""
# Решение 2 - многопроцессорность

import random
import multiprocessing
import time

ARRAY_SIZE = 1_000_000
PARTS = 10
part_size = int(ARRAY_SIZE / PARTS)

arr = [random.randint(1, 100) for _ in range(ARRAY_SIZE)]

result = []
result = multiprocessing.Array('i', PARTS)

def calculate_sum(sub_arr, result, index):
    part_sum = sum(sub_arr)
    result[index] = part_sum

if __name__ == '__main__':
    processes = []
    start = time.time()
    for i in range(PARTS):
        start_index = i * part_size
        end_index = start_index + part_size
        sub_arr = arr[start_index:end_index]
        p = multiprocessing.Process(target=calculate_sum, args=(sub_arr, result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_sum = sum(result)
    print("Сумма элементов массива:", total_sum)
    stop = time.time()
    print(f' Время работы {PARTS} процессов {round((stop - start), 6)}')