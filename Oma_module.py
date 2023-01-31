def loe_failist(file:str)->list:
    fail=open(file,"r",encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def list_failisse(mas:list,file:str):
    """ Salvetame loetelu failisse
    :param str file: Faili nimetus
    :param list mas: loetelu
    """
    f=open(file,"w",encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def elem_listisse(p:list,i:list):
    n=int(input("mitu inimesi lisame?"))
    for j in range(n):
        nimi=input("Nimi: ")
        i.append(nimi)
        palk=input("Palk: ")
        p.append(palk)
    return p,i

def kustutamine(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i

#def str_to_int(mas: list)->list:
#    for m in mas:
#        mas.pop(mas.index(m))
#        m=int(m)
#    return mas

def maksimaalne_palk(p:list,i:list):
    p=list(map(int,p))
    max_palk=max(p)
    n=p.count(max_palk)
    pos=0
    print(f"maksimalne palk on {max_palk}\nInimeste nimed:")
    for j in range(n):
        ind=p.index(max_palk,pos)
        nimi=i[ind]
        print(f"{nimi}")
        pos=ind+1
