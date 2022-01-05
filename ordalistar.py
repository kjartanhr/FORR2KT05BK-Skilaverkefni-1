def pretty_print(l, d = ","):
    r = ""
    for x, y in enumerate(l):
        if (x + 1) == len(l):
            r = f"{r}{y}"
        else:
            r = f"{r}{y}{d} "
    return r

def main():
    a = []
    b = []
    c = []
    for i in range(5):
        a.append(input(f"Sláðu inn orð nr. {i + 1} í lista A > "))
    for i in range(5):
        b.append(input(f"Sláðu inn orð nr. {i + 1} í lista B > "))
    for i in a:
        if i in b:
            c.append(i)
    print(f"Eins orð í báðum listum: {pretty_print(c)}")

if __name__ == '__main__':
    main()