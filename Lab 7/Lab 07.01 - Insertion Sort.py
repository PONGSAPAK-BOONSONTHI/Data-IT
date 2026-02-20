"""Lab 07.01 - Insertion Sort"""
def insertionSort(data: list, last: int):
    comparison = 0
    for current in range(1, last + 1):
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

def main():
    import json
    data_list = json.loads(input())
    last = int(input())
    insertionSort(data_list, last)
main()
