from math import log, pow

def insert(bucket, elem):
    bucket.append(elem)
    i = 0
    while i < len(bucket) and bucket[i] < elem:
        i += 1
    j = len(bucket) - 1
    while j > i:
        bucket[j], bucket[j-1] = bucket[j-1], bucket[j]
        j -= 1
    bucket[i] = elem

def bucket_sort(array, start, end):
    n = len(array)
    inter_len = (end - start) / n
    buckets = [[] for _ in range(n+1)]
    for i, x in enumerate(array):
        if x == 0:
            insert(buckets[0], x)
            continue
        bucket = int(x / inter_len)
        insert(buckets[bucket], x)
    index = 0
    for buck in buckets:
        for x in buck:
            array[index] = x
            index += 1

def fast_sort(array, a):
    for i, elem in enumerate(array):
        array[i] = log(elem) / log(a)
    bucket_sort(array, 0, 1)
    for i, elem in enumerate(array):
        array[i] = pow(a, elem)

