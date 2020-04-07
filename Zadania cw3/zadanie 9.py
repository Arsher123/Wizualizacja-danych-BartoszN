import math
def ciag_iloczyn(* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1.0
    for i in liczby:
        iloczyn = iloczyn*i
    return iloczyn
print(ciag_iloczyn())
print(ciag_iloczyn(1,2,3,4,5,6,7,8))