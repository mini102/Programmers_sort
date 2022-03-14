def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)  #666, 101010, 222  6>2>1
    return str(int(''.join(numbers)))
