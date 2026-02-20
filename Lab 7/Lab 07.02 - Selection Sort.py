"""Lab 07.02 - Selection Sort"""
def selectionSort(data: list, last: int):
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

def main():
    import json
    data_list = json.loads(input())
    last = int(input())
    selectionSort(data_list, last)
main()
