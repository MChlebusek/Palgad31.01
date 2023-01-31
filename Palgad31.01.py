from Oma_module import *
palgad=[]
nimeta=[]
#palgad=loe_failist("palgade_file.txt")
#print(palgad)
#nimeta=loe_failist("nimeta_file.txt")
#print(nimeta)

while True:
    print("-------------------------------")
    print("0-loe failist\n1-andmete lisamine\n2-salvestame failisse\n3-kuistutama nimi\n4-max palk")
    v=int(input())
    if v==0:
        palgad=[]
        nimeta=[]
        palgad=loe_failist("palgade_file.txt")
        nimeta=loe_failist("nimeta_file.txt")
        print(palgad)
        print(nimeta)

    elif v==1:
        palgad, nimeta=elem_listisse(palgad,nimeta)
        print(palgad)
        print(nimeta)
    elif v==2:
        list_failisse(palgad,"palgade_file.txt")
        list_failisse(nimeta, "nimeta_file.txt")
        print(palgad)
        print(nimeta)
    elif v==3:
        palgad,nimeta=kustutamine(input("sisesta nimi "),palgad,nimeta)
    elif v==4:
        maksimaalne_palk(palgad,nimeta)
