# def yoshniTop (ism, tugulganYil) :
#     print(f"{ism.title()}ning yoshi {2023-tugulganYil} da ekan")

# yoshniTop('Ali',2001 )
# yoshniTop('Rais',2007 )

# def sonKirit(raqam):
#     print(f"{raqam} ning kvadrati {raqam**2} ga teng va kubi {raqam**3} ga teng ")

# sonKirit(2)


# def sonKirit(raqam):
#     if raqam %2 :
#         print(f"{raqam} toq son ekan")
#     else:
#         print(f"{raqam} juft son ekan va natijasi {raqam/2} ga teng")

# sonKirit(100)

# def sonKirit(raqam, son):
#     if son > raqam :
#         print(f"{son} {raqam} dan katta ekan")
#     elif raqam > son:
#         print(f"{raqam} {son} dan katta ekan")
#     else:
#         print('Ikalla raqamlar teng')

# sonKirit(55, 65)

# def daraja(x,y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng"
# daraja(5)
# daraja(2,3)
# daraja(3,3)

# def sonKirit(son):
#     for n in range(2,11):
#         if not son%n :
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")

# sonKirit(5)

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni 
# kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)



# def malumotlar(ism, familiya, tugilganYil, tugilganJoy, yosh, email = '', telefon=''):
#     malumot = {'ism':ism,
#                'familiya': familiya,
#                'tugilganYil': tugilganYil,
#                'tugilganJoy' : tugilganJoy,
#                'email': email,
#                'telefon' : telefon,
#                'yosh': yosh}
    
#     return malumot


# malumot1 = malumotlar('Ali', 'Rasulov', 2001, 'Toshkent', 24)
# malumot2 = malumotlar('Rustam', 'Olimov', 2005, 'Namangan', 22)
# malumotlarr = [malumot1, malumot2]
# print(f"Do'stlar haqida ma'lumotlar")
# for malumot in malumotlarr:
#     if malumot['telefon']:
#         telefon = malumot['telefon']
#     else:
#      print(f"{malumot['ism']}, {malumot['familiya']},, {malumot['tugilganYil']},, {malumot['tugilganJoy']}, {malumot['yosh']}, {malumot['email']}, {malumot['telefon']}")
 



# print('Enter information about the client:')
# malumotlarr = []
# while True:
#     print('Enter the information required below:')
#     ism = input('What is your name?')
#     familiya = input('What is your surname?')
#     tyil = input('When were you born?')
#     tjoy = input('Where were you born?')
#     ilm = input('What is your faculty?')

#     malumotlarr.append(malumotlar(ism, familiya, tyil, tjoy, ilm))
#     javob = input('Any informations? (Yes/ no')
#     if javob == 'no':
#         break

# def big(son1,son2,son3):
#     if son1 >son2 and son1 > son3:
#         return son1
#     elif son2>son2 or son2> son3:
#         return son2
#     # elif son3>son1 and son3 >son2:
#     #     return son3
#     else:
#         return son3



# print(big(99,122,88))


# def aylana (radius):
#     qiymatlar = {
#         'yuzi' : 3.14*radius **2,
#         'diametr': radius *2,}
#     return qiymatlar
    
# print(aylana(20))


# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# print(tub_sonlar_top(1,50))

# def fibonacci(n):
#     fib_list = [0,1]
#     while len(fib_list) < n:
#         next_fib = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_fib)
#     return fib_list

# print(fibonacci(10)) 



















# def royhatQil(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title() 

# nomlar = [(input('Ism kiriting')), (input('Ism kiriting')), (input('Ism kiriting'))]
# royhatQil(nomlar)
# print(nomlar)

# def royhatQil(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title() 
#     return matnlar

# nomlar = [(input('Ism kiriting')), (input('Ism kiriting')), (input('Ism kiriting'))]
# yangi_nomlar = royhatQil(nomlar)

# print(nomlar)
# print(yangi_nomlar)


# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


# def bahola(ismlar):
#     baholar={}
#     for ism in ismlar:
#         baho = input(f" Talanba {ism.title()} ning bahosini kiritng:")
#         baholar[ism] = baho
#     return baholar

# talabalar = ['rustam', 'ali', 'olim', 'mahmud', 'bobue']
# print(bahola(talabalar[:]))
# print(talabalar)

# def kopaytir(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma = kopaytma*son
#     return kopaytma

# daraja = kopaytir(4,4,2,2,2)
# print(daraja)


# def malumotlat(ismi, familiyasi, **boshqalar):
#     boshqalar['ismi']= ismi
#     boshqalar['familiyasi']= familiyasi
#     return boshqalar

# talaba1 = malumotlat('Ali','Aliyev', yosh = 24, uy = 'Namangan', telefoni = 75110797)
# talaba2 = malumotlat('Olim','OLimov', yosh = 34, uy = 'Toshkent', telefoni = 3875753, addresi = 'qayerdadur')

# print(talaba1)
# print(talaba2)

