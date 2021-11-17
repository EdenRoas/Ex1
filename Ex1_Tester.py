from My_algo import my_algo


if __name__ == "__main__":
    # fileBuilding = open("C:\\Users\hadar\PycharmProjects\Ex1\B1.json", "r")
    # fileCall = open("C:\\Users\hadar\PycharmProjects\Ex1\Calls_a.csv", "r")
    algo = my_algo("C:\\Users\hadar\PycharmProjects\Ex1\B1.json", "C:\\Users\hadar\PycharmProjects\Ex1\Calls_a.csv")
    algo.updateFile("Ex1_calls_c_1")