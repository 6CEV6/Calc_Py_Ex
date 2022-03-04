def main():
    end = False
    while not end:
        art_lay = str(input("Jakie działanie arytmetyczne mam wykonać? \n +,-,*,/,% \n"))
        x = int(input("Wprowadź pierwszą liczbę: \n"))
        y = int(input("Wprowadź drugą liczbę: \n"))
## Pętla: wykonuj art_lay po uzyskanym wyniku

        if art_lay == '+':
            print("Twój wynik to:", x + y)
        elif art_lay == '-':
            print("Twój wynik to:", x - y)
        elif art_lay == '*':
            print("Twój wynik to:", x * y)
        elif art_lay == '/':
            print("Twój wynik to: ", x / y)
        elif art_lay == '%':
            print("Twój wynik to: ", x % y)
        else:
            print("Niepoprawna operacja")
            break
        print("\n Chcesz wykonać kolejne działanie? \n Wpisz literę t lub n")
        
        kolejne = input()
        if kolejne == "t":
            end = False
        elif kolejne == "n":
            print ("Koniec operacji!")
            break
        #return main()
if __name__ == "__main__":
    main()
