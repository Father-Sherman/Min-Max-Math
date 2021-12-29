import random
import time

def main():
    print("Welcome to D&D Math Practice")
    print("Ready GO!")
    while True:
        first = random.randint(0,20)
        second = random.randint(0,10)
        print("what is ", first, " + ", second, "?")
        while True:
            answer = input()
            if int(answer) is (first + second):
                print("CORRECT!!!")
                print()
                print()
                break
            else:
                print("Wrong!!!")
                time.sleep(2)
                print()
                print()

main()