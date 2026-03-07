def main():
    x, y, z = input("What's your arithmetic expression? ").strip().split(" ")

    match y:
        case "+":
            addition(x, z)
        case "-":
            substraction(x, z)
        case "*":
            multiplication(x, z)
        case "/":
            division(x, z)
        case _:
            print("Invalid input")

def addition(p, q):
    pfloat = float(p)
    qfloat = float(q)
    r = pfloat + qfloat
    print(f"{r:.1f}")

def substraction(p, q):
    pfloat = float(p)
    qfloat = float(q)
    r = pfloat - qfloat
    print(f"{r:.1f}")

def multiplication(p, q):
    pfloat = float(p)
    qfloat = float(q)
    r = pfloat * qfloat
    print(f"{r:.1f}")

def division(p, q):
    pfloat = float(p)
    qfloat = float(q)
    r = pfloat / qfloat
    print(f"{r:.1f}")

main()