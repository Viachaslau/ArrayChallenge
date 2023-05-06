def ArrayChallenge(arr):
    s_list = []
    s_list.append(arr[-1])
    k = 0
    for i in range(0, len(arr)-1):
        if arr[i] == 0:
            k = -1
        s_list.append(arr[i])
        if arr[i+1] <= arr[i]:
            s_list.append((2+k)*arr[i+1])
        else:
            s_list.append((2+k)*arr[i]) 
        k += 1
            
    return max(s_list)


print(ArrayChallenge(input()))