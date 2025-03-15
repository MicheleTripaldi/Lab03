import datetime
import queue

import spellchecker
import multiDictionary

sc = spellchecker.SpellChecker()
md = multiDictionary.MultiDictionary()

while(True):
    sc.printMenu()

    txtIn = input("Indicare la lingua:")
    # Add input control here!


    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")

        txtIn = input()
        c1 = queue.PriorityQueue()

        #creo una lista di elementi che contiene le parole digitate e creo una lista di elementi del dizionario
        lista_parole_input = sc.handleSentence(txtIn)
        tic = datetime.datetime.now()
        lista_parole_sbagliate = md.searchWord(lista_parole_input,"resources/Italian.txt")
        toc = datetime.datetime.now()
        print("-------------------------------")
        print("Using contains")
        for p in lista_parole_sbagliate:
            print(p)
        print(f"Per fare l'operazione ci sono voluti {toc-tic} secondi")
        # metodo linear

        c2= queue.PriorityQueue()
        tic = datetime.datetime.now()
        lista_parole_sbagliate = md.searchWordLinear(lista_parole_input,"resources/Italian.txt")
        toc = datetime.datetime.now()
        print("-------------------------")
        print("Using linear search")
        for p in lista_parole_sbagliate:
            print(p)
        print(f" Per fare la ricerca lineare ci vogliono{toc-tic} secondi")

        # metodo dichotomic
        tic = datetime.datetime.now()
        lista_parole_sbagliate = md.searchWordDichotomic(lista_parole_input,"resources/Italian.txt")
        toc = datetime.datetime.now()
        print("---------------------------")
        print("Using dichotomic search")
        for p in lista_parole_sbagliate:
            print(p)
        print(f" Per fare la ricerca Dichotomic ci vogliono{toc-tic} secondi")
        continue



    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        c1 = queue.PriorityQueue()

        # creo una lista di elementi che contiene le parole digitate e creo una lista di elementi del dizionario
        lista_parole_input = sc.handleSentence(txtIn)
        tic = datetime.datetime.now()
        lista_parole_sbagliate = md.searchWord(lista_parole_input, "resources/English.txt")
        toc = datetime.datetime.now()
        print("-------------------------------")
        print("Using contains")
        for p in lista_parole_sbagliate:
            print(p)
        print(f"Per fare l'operazione ci sono voluti {toc - tic} secondi")

        # metodo linear

        c2 = queue.PriorityQueue()
        tic = datetime.datetime.now()
        lista_parole_sbagliate = md.searchWordLinear(lista_parole_input, "resources/English.txt")
        toc = datetime.datetime.now()
        print("-------------------------")
        print("Using linear search")
        for p in lista_parole_sbagliate:
            print(p)
        print(f" Per fare la ricerca lineare ci vogliono{toc - tic} secondi")

        # metodo dichotomic
        tic = datetime.datetime.now()
        lista_parole_sbagliate = md.searchWordDichotomic(lista_parole_input, "resources/English.txt")
        toc = datetime.datetime.now()
        print("---------------------------")
        print("Using dichotomic search")
        for p in lista_parole_sbagliate:
            print(p)
        print(f" Per fare la ricerca Dichotomic ci vogliono{toc - tic} secondi")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(txtIn) == 4:
        break


