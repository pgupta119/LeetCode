class State:
    def __init__(self):
        print("In the state class")
        self.state1 = "Main State"
        # state1 = "Main State"


##derived class
class HappyState(State):
    def __init__(self):
        print("In the happy state class")
        self.state2 = "Derived State"
        super().__init__()


state = HappyState()

# print(state.state1)
print(state.state2)
