def BubbleSort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]: # > : 작은 것부터, 오름차순 // < : 큰 것부터, 내림차순
                data[j], data[j+1] = data[j+1], data[j]

data = [55, 7, 78, 12, 42]
BubbleSort(data)
print(data)