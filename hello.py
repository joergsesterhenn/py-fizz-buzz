#### TASK ####
# print numbers from 1 to 1000
# if number is multiple of 3 print fizz
# if number is multiple of 5 print buzz


def main():
    print("Hello from fizzbuzz!")
    for i in range(1000):
        print(i, ":", fizz(i))


def fizz(i: int) -> str:
    if i % 5 == 0:
        return "buzz"
    if i % 3 == 0:
        return "fizz"
    return str(i)


if __name__ == "__main__":
    main()
