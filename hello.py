#### TASK ####
# print numbers from 1 to 1000
# if number is multiple of 3 print fizz
# if number is multiple of 5 print buzz


def main():
    print("Hello from fizzbuzz!")
    for i in range(1, 1001):
        print(i, ":", fizz(i))


def fizz(i: int) -> str:
    reply = ""
    if i % 3 == 0:
        reply = "fizz"
    if i % 5 == 0:
        reply += "buzz"
    if reply == "":
        reply = str(i)
    return reply


if __name__ == "__main__":
    main()
