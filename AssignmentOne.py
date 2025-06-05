# Triangle Pattern Generator using '*'


# Lower triangular pattern
def lower_triangle(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()

# Upper triangular pattern 
def upper_triangle(n):
    print("Upper Triangular Pattern:")
    for i in range(n):
        print("  " * i + "* " * (n - i))
    print()

# Pyramid pattern
def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()


rows = int(input("Enter number of rows: "))

lower_triangle(rows)
upper_triangle(rows)
pyramid(rows)
