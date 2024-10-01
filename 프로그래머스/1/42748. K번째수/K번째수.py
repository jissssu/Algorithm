def solution(array, commands):
    answer = []
    for a,b,c in commands: 
        sliced_array = array[a-1:b] 
        sliced_array.sort() 
        answer.append(sliced_array[c-1])
    return answer