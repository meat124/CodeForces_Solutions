import sys
input = sys.stdin.readline


def ask(x, y):
    print(f"? {x} {y}")
    sys.stdout.flush()
    return int(input())


def answer(x, y):
    print(f"! {x} {y}")
    sys.stdout.flush()


for t in range(int(input())):
    n, m = map(int, input().split())
    a1 = ask(1, 1)
    if a1 >= n:
        a2 = ask(1, a1 + 1)
        answer(a2 + 1, a1 + 1)
    elif a1 >= m:
        a2 = ask(a1 + 1, 1)
        answer(a1 + 1, a2 + 1)
    else:
        a2, a3 = ask(a1 + 1, 1), ask(1, a1 + 1)
        if a1 == a2 and a1 == a3:
            answer(a1 + 1, a1 + 1)
        elif a1 == a3:
            answer(a1 + 1, a2 + 1)
        else:
            answer(a3 + 1, a1 + 1)
