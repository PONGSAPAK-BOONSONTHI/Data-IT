def insertionSort(data: list):
    last = len(data) - 1
    comparison = 0
    for current in range(1, last):
        hold = data[current]
        walker = current - 1
        while walker >= 0:
            comparison += 1
            if not hold < data[walker]:
                break
            data[walker + 1] = data[walker]
            walker -= 1
        data[walker + 1] = hold
        print(data)
    print(f"Comparison times: {comparison}")

def selectionSort(data: list):
    last = len(data) - 1
    comparison = 0
    for current in range(last):
        smallest = current
        walker = current + 1
        while walker <= last:
            comparison += 1
            if data[walker] < data[smallest]:
                smallest = walker
            walker += 1
        data[current], data[smallest] = data[smallest], data[current]
        print(data)
    print(f"Comparison times: {comparison}")

def bubbleSort(data: list):
    last = len(data) - 1
    comparison = 0
    current = 0
    sort = False
    while current <= last and sort is False:
        walker = last
        sort = True
        while walker > current:
            comparison += 1
            if data[walker] < data[walker - 1]:
                sort = False
                data[walker], data[walker - 1] = data[walker - 1], data[walker]
            walker -= 1
        current += 1
        print(data)
    print(f"Comparison times: {comparison}")

def main():
    import json
    data_list = json.loads(input())
    print("insertionSort :")
    insertionSort(data_list)
    print("selectionSort :")
    selectionSort(data_list)
    print("bubbleSort :")
    bubbleSort(data_list)
main()
