starting_num = input("Enter starting number: ")

# Checks
try:
    starting_num = int(starting_num)
except ValueError:
    raise TypeError("You must input a valid number!") from None


def even(num: int) -> bool:
    return num % 2 == 0
    

next_num: int = 0
results: list[int] = []


next_num = starting_num

while next_num != 1:
    if even(next_num):
        results.append(next_num / 2)  # type: ignore
        next_num = next_num / 2       # type: ignore
    else:
        results.append(next_num * 3 + 1)
        next_num = next_num * 3 + 1

print(results)