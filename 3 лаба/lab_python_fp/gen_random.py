import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        number = random.randrange(begin, end)
        yield number

def main():
    data = list()
    for i in gen_random(7, 0, 9):
        data.append(i)
    print(data)
if __name__ == "__main__":
    main()