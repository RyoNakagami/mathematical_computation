def gauss_jordan(A, output_array = None):
    n, m = A.shape
    for i in range(n):
        if A[i, i] == 0:
            raise ValueError('{}-th pivot is zero'.format(i))
        
        A[i, :] = A[i, :]/A[i,i]
        
        for j in range(n):
            if i != j:
                A[j, :] = A[j, :] - A[j,i] * A[i, :]
    if output_array:
        return A
    return A[:, -1]