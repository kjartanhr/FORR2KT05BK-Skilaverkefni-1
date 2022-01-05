def main():
    weight = float(input("Sláðu inn þyng þína í kg > "))
    height = float(input("Sláðu inn hæð þína í m > "))
    bmi = weight / pow(height, 2)
    print(f"BMI stuðullinn þinn er: {round(bmi, 2)}")

if __name__ == '__main__':
    main()