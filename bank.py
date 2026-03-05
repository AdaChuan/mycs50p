def main():
    x = input("What's your greeting? ").lower().strip()

    if leadinghello(x):
        print("$0")
    elif leadingh(x):
        print("$20")
    else:
        print("$100")

def leadinghello(n):
    return n.startswith('hello')

def leadingh(n):
    return n.startswith('h')

main()