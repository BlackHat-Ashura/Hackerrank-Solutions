if __name__ == '__main__':
    input_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        input_list.append([name, str(score)])
        scores.append(score)
    
    lowest = min(scores)
    while lowest in scores:
        scores.remove(lowest)
    second_lowest = min(scores)
    output_names = [i[0] for i in input_list if i[1] == str(second_lowest)]
    output_names.sort()
    print("\n".join(output_names))
