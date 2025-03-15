import dictionary as d



dict = d.Dictionary()

class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        pass

    def searchWord(self, words, nome_file):
        diz = dict.loadDictionary(nome_file)
        parole_sbagliate= []
        for word in words:
            if word not in diz:
                parole_sbagliate.append(word)
        return parole_sbagliate


    def searchWordLinear(self,words, nome_file):
        diz = dict.loadDictionary(nome_file)
        lista_sbagliate = []
        for word in words:
            flag = False
            for i in range(0,len(diz)):
                if word == diz[i]:
                    flag = True
            if not flag:
                lista_sbagliate.append(word)
            return lista_sbagliate


    def searchWordDichotomic(self,words, nome_file):
        diz = dict.loadDictionary(nome_file)
        lista_sbagliate = []
        for word in words:
            flag = False
            estremo_inf =0
            estremo_sup = len(diz)-1
            posizine_centrale = estremo_inf+(estremo_sup-estremo_inf)//2
            while estremo_inf <= estremo_sup:
                posizine_centrale = estremo_inf + (estremo_sup - estremo_inf) // 2
                if word == diz[int(posizine_centrale)]:
                    flag = True
                    break
                elif word < diz[int(posizine_centrale)]:
                    estremo_sup = posizine_centrale-1
                elif word > diz[int(posizine_centrale)]:
                    estremo_inf = posizine_centrale+1
            if not flag:
                lista_sbagliate.append(word)
        return lista_sbagliate












