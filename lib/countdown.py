import time


def countdown(integer):
    int = 0
    while integer > int:
        print(f"{integer} SECOND(S)!")
        integer -= 1
    print("HAPPY NEW YEAR!")


print(countdown(5))


def countdown_with_sleep(integer):
    for i in range(integer, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)
    print("HAPPY NEW YEAR!")


# Example usage
countdown_with_sleep(5)
