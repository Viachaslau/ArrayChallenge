def ArrayChallenge(arr): # arr - List of int. Each of the items >= 0
    s_list = [] 
    s_list.append(arr[-1])
    k = 0 
    for i in range(0, len(arr)-1):  #loop without last element of "arr"
        if arr[i] == 0:
            k = 0
            i += 1
        else:
            s_list.append(arr[i])
            if arr[i+1] <= arr[i]:
                s_list.append((2+k)*arr[i+1])
            else:
                s_list.append((2+k)*arr[i]) 
            k += 1
            
    return max(s_list)

print(ArrayChallenge(input()))
