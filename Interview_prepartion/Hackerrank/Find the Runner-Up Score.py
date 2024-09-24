# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # first sort the list:
    arr.sort(reverse=True)
    
    # removed the duplicate values
    arr_unique = []
    for num in arr:
        if num not in arr_unique:
            arr_unique.append(num)
    
    # print the second maximum which is the runner up score
    print(arr_unique[1])
    
    