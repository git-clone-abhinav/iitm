def is_magic(mat):
    _sum = sum(mat[0])
    
    for i in mat:
        if sum(i) != _sum:
            return 'NO'
        
    for i in range(len(mat[0])):
        x = 0
        for j in mat:
            x += j[i]
        if x != _sum:
            return 'NO'
        
    x = 0
    for i in range(len(mat)):
        x += mat[i][i]
    if x != _sum:
        return 'NO' 
    
    x = 0
    colId = len(mat[0])-1
    for i in range(len(mat)):
        x += mat[i][colId - i]
    if x != _sum:
        return 'NO' 

    return 'YES'
