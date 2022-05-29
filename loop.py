rows = 5
column = 4

[["." for c in range(column)] for r in range(rows)]

test = [["." for c in range(column)] for r in range(rows)]

# test = []
# for r in range(rows):
#     baris = []
#     for c in range(column):
#         baris.append(".")
#     test.append(baris)

for i in test:
    print(i)