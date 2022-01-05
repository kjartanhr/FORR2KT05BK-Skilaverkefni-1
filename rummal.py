def main():
    # önnur lausn en bara "lengd = float(input(..."
    a = ["lengd", "breidd", "hæð"]
    b = []
    for i in range(3):
        b.append(float(input(f"Sláðu inn {a[i]} > ")))
    print(f"Rúmmál: {round(b[0] * b[1] * b[2], 2)} rúmmetrar")

if __name__ == '__main__':
    main()