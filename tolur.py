def main():
    name = input("Sláðu inn nafn > ")
    i = len(name)
    for x in range(len(name)):
        name = name[-i:]
        print(name)
        i -= 1
        
if __name__ == '__main__':
    main()