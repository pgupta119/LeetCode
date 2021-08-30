class Student:
    ...


def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()
    # if name == 'Padma':
    #     house = "Ravenclaw"
    student = get_student()
    print(f"{student.name} from {student.house}")

    # print(f"{student[0]} from {student[1]}")
    # print(f"{name} from {house}")



# def get_name():
#     return input("Name:  ")

# def get_house():
#     return input("House: ")

def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    return student
     #
     # return name, house

if __name__ == "__main__":
    main()




