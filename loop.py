# rows = 5
# column = 4

# [["." for c in range(column)] for r in range(rows)]

# test = [["." for c in range(column)] for r in range(rows)]

# # test = []
# # for r in range(rows):
# #     baris = []
# #     for c in range(column):
# #         baris.append(".")
# #     test.append(baris)

# for i in test:
#     print(i)


from os import stat
from queue import Empty


class jarak:
    def __init__(self, jarak):
        self.jarak = jarak
    
    # def __lt__(self, other):
    #     # 100 < 150
    #     return self.jarak > other.jarak 
        

# jakarta_depok = jarak(100)
# jakarta_bekasi = jarak(150)
# print(jakarta_depok < jakarta_bekasi)

# hapus = [1, 2, 3, 4]
# hapus.pop()
# print(hapus)

class a():
    def b():
        return "test"

status = False


if status is not True:
    test = a()


if not test:
    print("test belum di deklarasikan")