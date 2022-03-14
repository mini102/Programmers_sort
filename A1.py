def solution(array, commands):
    answer = []
    for entry in commands:
        # print(sorted(array[entry[0]-1:entry[1]]))
        a = sorted(array[entry[0]-1:entry[1]])
        answer.append(a[entry[2]-1])
        
    return answer
