def matrixRotation(matrix, r):
    R = len(matrix)
    C = len(matrix[0])
    layers = min(R, C)//2
    mat = []
    
    for layer in range(layers):
        temp = []
        row_last = R - (layer+1)
        column_last = C - (layer+1)
        
        for i in range(layer, column_last):
            temp.append(matrix[layer][i])
        for i in range(layer, row_last):
            temp.append(matrix[i][-(layer+1)])
        for i in range(layer, column_last):
            temp.append(matrix[-(layer+1)][-(i+1)])
        for i in range(layer, row_last):
            temp.append(matrix[-(i+1)][layer])
        mat.append(temp)
    
    for layer in range(layers):
        length = len(mat[layer])
        idx = r%length
        row_last = R - (layer+1)
        column_last = C - (layer+1)
        
        for i in range(layer, column_last):
            matrix[layer][i] = mat[layer][idx]
            idx += 1
            idx = idx%length
        for i in range(layer, row_last):
            matrix[i][-(layer+1)] = mat[layer][idx]
            idx += 1
            idx = idx%length
        for i in range(layer, column_last):
            matrix[-(layer+1)][-(i+1)] = mat[layer][idx]
            idx += 1
            idx = idx%length
        for i in range(layer, row_last):
            matrix[-(i+1)][layer] = mat[layer][idx]
            idx += 1
            idx = idx%length

    for rows in matrix:
        print(" ".join(str(j) for j in rows))
