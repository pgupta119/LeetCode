def main():
    height = int(input("Height: "))
    # print(height)
    pyramid(height)


def pyramid(n):
    print(n)
    for i in range(n, 0, -1):
        # print(i)
        print("#"*(i))


if __name__ == "__main__":
    main()
