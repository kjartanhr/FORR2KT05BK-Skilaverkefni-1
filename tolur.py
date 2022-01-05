from random import randint

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
    m = 1
    for i in range(50):
        r = randint(5, 70)
        m *= r
        a.append(r)
    b = sorted(a)
    print(f"Allar tölur margfaldaðar: {m}\nHæsta tala: {b[-1]}\nLægsta tala: {b[0]}\nÓraðaður listi: {pretty_print(a)}\nRaðaður listi: {pretty_print(b)}")
    
        
if __name__ == '__main__':
    main()
