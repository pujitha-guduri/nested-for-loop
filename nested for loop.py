# Nested For Loop Assignment

rows = 5

print("Checkerboard Pattern:\n")

for i in range(rows):
    for j in range(rows):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()