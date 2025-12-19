"""Exercise 01.01- Prob Stat"""
def main():
    """Exercise 01.01- Prob Stat"""
    num = []
    for _ in range(4):
        x = int(input())
        num.append(x)
    mins = min(num)
    # print(mins)
    num.remove(mins)
    print(sum(num))
main()
