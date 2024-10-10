# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    
    my_list = []
    
    for _ in range(n):
        input_list = input().split()
              
        if input_list[0] == 'print':
            print(my_list)
        elif input_list[0] == 'insert':
            my_list.insert(int(input_list[1]), int(input_list[2]))
        elif input_list[0] == 'append':
            my_list.append(int(input_list[1]))
        elif input_list[0] == 'remove':
            my_list.remove(int(input_list[1]))
        elif input_list[0] == 'pop':
            my_list.pop()
        elif input_list[0] == 'sort':
            my_list.sort()
        elif input_list[0] == 'reverse':
            my_list.reverse()