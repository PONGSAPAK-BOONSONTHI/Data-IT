"""Lab 07.03 - Bubble Sort"""
def bubbleSort(data: list, last: int):
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
    last = int(input())
    bubbleSort(data_list, last)
main()
