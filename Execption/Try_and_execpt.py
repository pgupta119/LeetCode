# def main():
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int():
#     while True:
#         try:
#             return int(input('What is x?'))
#         except ValueError:
#             pass
#




def main():
    x = get_int("what is x? ")
    print(f"x is {x}")


def get_int(name):
    while True:
        try:
            return int(input(name))
        except ValueError:
            pass


main()
# try:
#     x = int(input("what is X?"))
#     print(x)
# except ValueError:
#     print('X is not integer')
#
# else:
#     print(f" x is {x}")
