from typing import List

def flippingMatrix(matrix: List[List[int]]) -> int:
    """
    a b c d d c b a
    e f g h h g f e 
    i j k l l k j i
    m n o p p o n m
    m n o p p o n m
    i j k l l k j i
    e f g h h g f e
    a b c d d c b a

    you can get the max a-p into the upper left matrix
    through column and row transformations, like a rubik's cube.
    """
    total = 0

    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            total += max(matrix[i][j], 
                         matrix[-i-1][j], 
                         matrix[i][-j-1], 
                         matrix[-i-1][-j-1])
    
    return total
            
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
