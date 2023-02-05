# otam = {"tugilgan yili" : '1978', 'ismi': 'Murodjon alayorov', 'shahri' : 'Namangan'}
# print(f"Mening dadam {otam['tugilgan yili']} da tallud topganlar. ismlari {otam['ismi'].title()}. {otam['shahri']}da yashaydilar ")


# taom = {'ali':'manti', 'mahmud' : 'osh', 'botir' :'somsa', 'olim' : 'shashlik', 'ahmad' : 'qatiq'}
# print(f" Ali {taom['ali']}ni yoqtiradi")
# print(f" Ahmad {taom['ahmad']}ni yoqtiradi")
# print(f" Botir {taom['botir']}ni yoqtiradi")

# python = {'integer' : 'raqam', 'string':'matn', 'float':'raqam', 'if':'agar', 'else' :'yana', 'for':'uchun', 'loop':'aylana'}

# word = input('Enter the word you want:').lower()
# print(python.get(word, 'There is no such word'))



# python = {'integer' : 'raqam', 'string':'matn', 'float':'raqam', 'if':'agar', 'else' :'yana', 'for':'uchun', 'loop':'aylana'}
# word = input('Enter the word you want:')
# tarjima = python.get(word)
# if tarjima == None:
#     print('Bunday so\'z mavjud emas')


# else:
#     print(f"{word.title()} so'zi {tarjima}")



# python = {'integer' : 'raqam', 'string':'matn', 'float':'raqam', 'if':'agar', 'else' :'yana', 'for':'uchun', 'loop':'aylana'}

# for key, value in sorted(python.items()) :
#     print( f"{key.title()} - {value}") 


#countries = {'Uzbekistan' : 'tashkent', 'korea':'seoul', 'amerika':'washington', 'china':'tokio'}
# for key in sorted(countries.keys()):
#     print(key.title())
# for capital in sorted(countries.values()):
#     print(capital.title())
#   # print(f"{key.title()} davlatining poytaxti {capital.title()}dir!")

# davlat = input('Davlat nomini kiriting:')
# capital = countries.get(davlat)
# if capital == None :
#     print('Bizda bunday ma\'lumot yo\'q')
# else:
#     print(f"{davlat.upper()} ning poytaxti {capital.title()}")


# restoran = {'manti':'12500','osh':'11000','somsa':'3500',
#            'chuchvara':'7000','norin':'12000','mastava':'8000',
#            'chihanbili':'14000','qozonKabob':'16000','shirguruch':'5000',
#            'lavash':'7900','burger':'8900','shorva':'8500',
#            }

# print('Ovqatlanish uchun 3 xil taom tanlang')

# zakazlar = []

# for taom in range(3):
#     zakazlar.append(input(f"{taom+1}chi taomni kiritng").lower())
  
# for buyurtma in zakazlar :
#     if buyurtma in restoran:
#         print(f"{buyurtma.title()} narxi {restoran[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz bizda {buyurtma} yo'q")

# supermarket = {'tufli':200000,'shkalad':8000,'olma':10000,
#               'cola':5000,'qoshiq':3500,'kartoshka':5000,
#               'sabzi':5000,'telefon':500000,'soat':150000,
#               'idish':3000,'makaron':3000,'tuxum':9000,
#               'mayonez':6000,'tuz':2000,'suv':3000,
#               }

# savatcha =[]

# for n in range(7):
#     savatcha.append(input(f"Harid qiladigan {n+1} maxsulotni tanlang").lower())

# for harid in savatcha :
#     if harid in supermarket:
#         print(f"{harid.title()} narxi {supermarket[harid]} so'm")
#     else:
#         print('Bizda bunday mahsulot yo\'q')

# imomiAzam = {
#     'ism':'Nomon ibn Sobit',
#     'tyil': 80,
#     'yonalishi':'fiqh',
#     'kitobi':'giqhul akbar'
# }

# imomiShofeiy = {
#     'ism':'Muhammad ibn Idris',
#     'tyil': 150,
#     'yonalishi':'fiqh',
#     'kitobi': 'nomalum'
# }

# imomiMolik = {
#     'ism':'Molik ibn Anas',
#     'tyil': 209,
#     'yonalishi':'fiqh',
#     'kitobi': 'bilmayman'
# }

# imomiAhmad = {
#     'ism':'Ahmad ibn Hanbal',
#     'tyil': 250,
#     'yonalishi':'fiqh',
#     'kitobi': 'Sunan'
# }

# shaxslar =[imomiAzam, imomiShofeiy, imomiMolik, imomiAhmad]

# for shaxs in shaxslar :
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     yonalishi = shaxs['yonalishi']
#     kitobi = shaxs['kitobi']
#     print(f"{ism} {tyil}-yildada tavallud topgan va {yonalishi} bo'yicha ilm bergan. Yozgan kitobi {kitobi}")


# imomiAzam = {
#     'ism':'Nomon ibn Sobit',
#     'tyil': 80,
#     'yonalishi':'fiqh',
#     'kitobi':['fiqhul akbar', 'diniy', 'aqidaviy']
# }

# imomiShofeiy = {
#     'ism':'Muhammad ibn Idris',
#     'tyil': 150,
#     'yonalishi':'fiqh',
#     'kitobi': ['arabiy', 'ilmiy', 'fiqhiy']
# }

# imomiMolik = {
#     'ism':'Molik ibn Anas',
#     'tyil': 209,
#     'yonalishi':'fiqh',
#     'kitobi': ['kitob', 'book', 'kniga']
# }

# imomiAhmad = {
#     'ism':'Ahmad ibn Hanbal',
#     'tyil': 250,
#     'yonalishi':'fiqh',
#     'kitobi': ['Sunan', 'mustadrok', 'ilm']
# }

# shaxslar =[imomiAzam, imomiShofeiy, imomiMolik, imomiAhmad]

# kinolar = {
#     'ali': ['krish','hayot','abdulhamidhon'],
#     'bobur': ['transformer','uch savdoi','toki hayot ekanman'],
#     'rustam': ['qopqon','qochqin','sotqin'],
#     'jony': ['supermen','batman','joker']
# }

# for ism, kinolar in kinolar.items() :
    
#     print(f" {ism.title()}ing yoqtirgan kinolari quyidagilar:")
#     for kino in kinolar:
#         print(kino)





# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar 
# haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

# davlatlar = {
#     'uzbekistan': {'mustaqil':'1991-yil',
#                    'konstitutsiya': '1992, 8-noyabr',
#                    'prezidenti': 'Shavkat Mirziyoyev',
#                    'poytaxti':'toshkent'
#                    },
#     'islom davlati' : {'mustaqil' : '632-yil',
#                        'konstitutsiya': 'nomalum',
#                        'prezidenti': 'Abdulhamidhon',
#                        'poytaxti':'Makka'
#                        },
#     'kazakhistan': {'mustaqil':'1993-yil',
#                    'konstitutsiya': '1995, 24-noyabr',
#                    'prezidenti': 'Nursultan Atanbayev',
#                    'poytaxti':'Astana'
#                    },
#     'kyirgizistan': {'mustaqil':'1992-yil',
#                    'konstitutsiya': '1993, 8-noyabr',
#                    'prezidenti': 'Nomalum',
#                    'poytaxti':'Osh'
#                    },
# }


# davlat = input('Istagan davlatingiz nomini kiritng:').lower()

# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"{davlat.title()}  {info['mustaqil']} da mustaqillikga erishgan.  Konstitutsiyasi {info['konstitutsiya']} \
#           da qabul qilingan. Prezidenti {info['prezidenti']} va poytaxti {info['poytaxti']} shaxridir")
# else:
#     print('Bizda', davlat, 'haqida ma\'lumot yo\'q')

# for davlat, info in davlatlar.items() :
#         print(f"{davlat.title()}  {info['mustaqil']} da mustaqillikga erishgan.  Konstitutsiyasi {info['konstitutsiya']} \
# da qabul qilingan. Prezidenti {info['prezidenti']} va poytaxti {info['poytaxti']} shaxridir")


