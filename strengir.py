def main():
    while True:
        string = input("Sláðu inn amk. 4 stafa orð > ")
        if len(string) < 3:
            print("Þetta er ekki 4 stafa orð, reyndur aftur.")
        else:
            new_string = f"{string[0:2]}{string[-2:]}"
            print(f"Nýji strengurinn er: {new_string}\nNýji strengurinn í hástöfum: {new_string.upper()}\nNýji strengurinn í lágstöfum: {new_string.lower()}")
            break
        
if __name__ == '__main__':
    main()