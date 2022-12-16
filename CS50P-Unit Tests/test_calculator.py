from calculator import square
import pytest
def user_str():
    with pytest.raises(TypeError):
r

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_zero():
    assert square(0) == 0
# def test_square():
#     # if square(2) != 4 :
#     #     print("2 squared was not 4")
#     # if square(3) != 9:
#     #     print("3 squared was not 9")
#         assert square(2) == 4
#         assert square(3) == 9


# if __name__ == "__main__":
#     main()