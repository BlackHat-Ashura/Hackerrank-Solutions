if __name__ == '__main__':
    N = int(input())    
    
    result = []  # Solution
    
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if re.search(r"@gmail.com", emailID):  # Solution
            result.append(firstName)  # Solution
    
    result.sort()  # Solution
    print("\n".join(result))  # Solution