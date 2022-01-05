from datetime import date

def main():
    kt = input("Sláðu inn kennitölu > ")
    if len(kt) == 10:
        dd = kt[0:2] # fæðingardagur
        mm = kt[2:4] # fæðingarmánuður
        yy = kt[4:6] # fæðingarár
        c = kt[-1::] # fæðingaröld
        # er dagur réttur
        if 0 < int(dd) < 32:
            # er mánuður réttur
            if 0 < int(mm) < 13:
                cy = date.today().year
                cc = int(str(cy)[1:2])
                # er kennitalan skráð á sömu öld og er núna
                if int(c) == cc:
                    # er fæðingarár í framtíð
                    if int(yy) > int(str(cy)[2:4]):
                        print("Ógilt kennitala (fæðingarár í framtíð)")
                    else:
                        print("Gild kennitala")
                else:
                    print("Gild kennitala")
            else:
                print(f"Ógildur fæðingarmánuður ({mm})")
        else:
            print(f"Ógildur fæðingardagur ({dd})")
    else:
        print("Kennitalan er ekki nægilega löng")
    
if __name__ == '__main__':
    main()