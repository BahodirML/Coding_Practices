# def katta_son_qaytar(son1,son2,son3):
#     return max(son1, son2, son3)

# print(katta_son_qaytar(4,5,3))

matnlar = ['Ism','famikiya', 'nimadier', 'olma', 'uzum','shaftoli']

def kattar_harf_qaytar():
    matnlar_modified = []
    for matn in matnlar:
        matn = f"{matn}".title()
        matnlar_modified.append(matn)
    return matnlar_modified

print(kattar_harf_qaytar())