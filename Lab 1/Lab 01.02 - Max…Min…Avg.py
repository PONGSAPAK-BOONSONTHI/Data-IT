import json
"""Lab 01.02 - Max…Min…Avg"""
def main():
    """Lab 01.02 - Max…Min…Avg"""
    num_list = json.loads(input())
    mx_ = float('-inf')
    mn_ = float('inf')

    for i in num_list:
        if mx_ < i:
            mx_ = i
        if mn_ > i:
            mn_ = i
    avg = sum(num_list) / len(num_list)

    avg = f"{avg:.2f}".rstrip("0")
    print(f"({mx_}, {mn_}, {avg})")
main()
