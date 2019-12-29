def solution(heights):
    answer = []
    for i in range (len(heights)):
        j=i-1
        while True:
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
            elif j == -1:
                answer.append(0)
                break
            j -= 1
    return answer