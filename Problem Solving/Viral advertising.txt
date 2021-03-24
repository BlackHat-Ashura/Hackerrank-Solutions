def viralAdvertising(n):
    shared = 5
    liked = 2
    cumulative = 2
    
    if n == 1:
        return cumulative
    
    for i in range(1, n):
        shared = liked * 3
        liked = shared//2
        cumulative += liked
        
    return cumulative
