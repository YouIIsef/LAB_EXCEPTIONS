def Addition(value1, value2):
    try:
        value1 = 10
        value2 = 20
        print("Addition:", value1 + value2)

    except NameError:
        print("Error: variable is not defined")


Addition(10, 20)