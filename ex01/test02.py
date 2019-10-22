def get_count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else :
        step = [1] + [2] + [0]*(n-2)
        for i in range(2,n):
            step[i] = step [i-1] + step [i-2]
            print(step[i])
        print(step)
        return step[n-1]

print(get_count(10))




