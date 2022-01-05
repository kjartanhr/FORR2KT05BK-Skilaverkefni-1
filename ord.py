def main():
    string = input("Sláðu inn setningu > ")
    wordlist = string.split(' ')
    print(f"Það eru {len(wordlist)} orð í setningunni.")
        
if __name__ == '__main__':
    main()