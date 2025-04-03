# Given an integer n, and n space-separated integers as input, create a tuple t, of
# those integers. Then compute and print the result of.

if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    h = hash(t)

    print(h)
