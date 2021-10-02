if __name__ == '__main__':
    N = int(input())
    
    list_ = []
    for _ in range(N):
        command = input().split(" ")
        if command[0] == "print":
            print(list_)
        elif command[0] == "sort":
            list_.sort()
        elif command[0] == "reverse":
            list_.reverse()
        elif command[0] == "pop":
            list_.pop()
        elif command[0] == "insert":
            list_.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            if int(command[1]) in list_:
                list_.remove(int(command[1]))
        elif command[0] == "append":
            list_.append(int(command[1]))


############################################################################3

if __name__ == '__main__':
    N = int(input())
    
    list_ = []
    for _ in range(N):
        input_ = input().split()
        command = input_[0]
        args = input_[1:]
        if command != "print":
            command += "(" + ",".join(args) + ")"
            eval("list_." + command)
        else:
            print(list_)
