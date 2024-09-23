# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Using list comprehension to generate the list of valid coordinates
        
    ans = [[i, j, k] for i in range(x + 1) 
                         for j in range(y + 1) 
                         for k in range(z + 1) 
                         if (i + j + k) != n]
    
    print(ans)
    
    # above code is equivalent to below for loop  code
    # resutl_for = []
    # for k in range(z+1): #1
    #     for j in range(y+1): #1,
    #         for i in range(x+1):
    #         resutl_for.append([i, j, k]) # 0,0, 1,0, 0,1, 1,1
            
    # print(resutl_for)