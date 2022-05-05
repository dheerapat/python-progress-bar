import math

# some how this snippet only work on window command prompt


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent)
    print(f'\r{bar} {percent}', end='\r')


numbers = [x * 5 for x in range(2000, 3000)]
result = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
