def lu_decomposition(X):
    A = X.copy()
    n = A.shape[0]
    P = np.identity(n)
    L = np.identity(n)
    
    for i in range(n):
        maxEl = abs(A[i, i])
        maxRow = i
        
        for k in range(i+1, n):
            if abs(A[k, i]) > maxEl:
                maxEl = abs(A[k, i])
                maxRow = k
                
        if i != maxRow:
            P[i, i], P[i, maxRow], P[maxRow, i], P[maxRow, maxRow] = 0, 1, 1, 0
            tmp = A[i, :].copy()
            A[i, :] = A[maxRow, :]
            A[maxRow, :] = tmp
    for i in range(n):
        for k in range(i + 1, n):
            m = A[k, i]/A[i, i]
            A[k, :] = A[k, :] - A[i, :] * m
            L[k, i] = m
            print(A)
        
    
    return P, L, A
        