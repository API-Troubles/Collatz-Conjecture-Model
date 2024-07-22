import matplotlib.pyplot as plt

starting_num = input("Enter starting number: ")

# Checks
try:
    starting_num = int(starting_num)
except ValueError:
    raise TypeError("You must input a valid number!") from None

if starting_num == 1:
    raise TypeError("The number cannot be 1.")


def even(num: int) -> bool:
    return num % 2 == 0
    

next_num: int = 0
results: list[int] = [starting_num]


next_num = starting_num

while next_num != 1:
    if even(next_num):
        results.append(int(next_num / 2))  # type: ignore
        next_num = next_num / 2       # type: ignore
    else:
        results.append(int(next_num * 3 + 1))
        next_num = next_num * 3 + 1

print("Results below:")
print(", ".join(str(i) for i in results))


x = range(len(results))
y = results

plt.plot(x, y)

# naming the x axis
plt.xlabel('Iteration Count')
# naming the y axis
plt.ylabel('Result')


plt.title(f'Collatz Conjecture - {starting_num}')

plt.savefig(f'graphs/{starting_num}.png')