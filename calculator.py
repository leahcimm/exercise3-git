def add(a, b):
    return a + b


def greet(name):
    return "Hi, " + name + "! (from feature branch)"


if __name__ == "__main__":
    print(greet("Software Engineering"))
    print("1 + 2 =", add(1, 2))
