import numpy as np

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return np.dot(a,b)
def matrix():
    print("\nEnter matrix dimensions: ")
    rows= int(input("Number of rows: "))
    col= int(input("Number of columns: "))
    
    print("Enter elements row-wise: ")
    matrix =[]
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

    
print("welcome to simple calculator!")
print("choose an operator:")
print("1.addition")
print("2.subtration")
print("3.multiplication")
print("4. transpose")
print("5.determinant")

choice = input("Enter choice(1/2/3/4/5):")
if choice in ['1','2','3']:
    
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
if choice =='1':
    print("\nenter matrix A: ")
    a = matrix()
    print("\nenter matrix B: ")
    b = matrix()
    
    if a.shape != b.shape:
        print("ERROR!!!!! MATRICES MUST HAVE THE SAME DIMENSIONS!!!!!")
    else:
        print(add(a,b))
elif choice =='2':
    print("\nEnter Matrix A:")
    a = matrix()

    print("\nEnter Matrix B:")
    b = matrix()

    if a.shape != b.shape:
        print("ERROR!!!!! MATRICES MUST HAVE THE SAME DIMENSIONS!!!!!")
    else:
        print(subtract(a,b))
elif choice =='3':
    print("\nEnter Matrix A:")
    a = matrix()

    print("\nEnter Matrix B:")
    b = matrix()

    if a.shape[1] != b.shape[0]:
        print("Error: Columns of A must equal rows of B!")
    else:
        print(multiply(a, b))
    
elif choice == '4':
    print("\n Matrix Transpose ")
    A =matrix()
    print("\nOriginal matrix: \n", A)
    print("\nTransposed matrix: \n",A.T)

elif choice == '5':
    print("\n Determinant ")
    A =matrix()
    
    if A.shape[0] != A.shape[1]:
        print("Error!!!! Determinant can only exist for square matrices!!!!")
    else:
        print("\nMatrix\n",A)
        print("\nDeterminant =", np.linalg.det(A))
            
else:
    print("invaild input.p1ease choose 1,2,3,4,5 or 6")