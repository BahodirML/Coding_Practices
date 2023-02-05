
# question ='Enter the book you like to read'
# question += '(enter detective)'

# flag = True
# while flag:
#     value = input(question)
#     if value == 'exit':
#         flag=False
#         print('You stopped the program')
#     else:
#         print(f"{value} is a good book")
 
 

#  Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
#  18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
#  chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
#  Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)


# while True:
#     yosh = input('Yoshingiz nechchida')

#     if yosh=='exit' or yosh =='quit':
#         break;
#     if int(yosh) <= 7:
#         print('Siz uchun', 2000, 'ming so\'m ')
#     elif  7 < int(yosh) <=  18 :
#         print('Siz uchun', 3000, 'ming so\'m ')
#     elif  18 < int(yosh) <=  65 :
#         print('Siz uchun', 10000, 'ming so\'m ')
#     elif  int(yosh) > 65 :
#         print('Siz uchun bepul')

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat =='exit':
#         break;
#     elif float(qiymat) <= 0:
#         continue;
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")




# buyurtmalar = []
# n = 1
# flag = True

# while flag==True:
#     mahsulot = input((f"{n}-taomingizni tanlang:"))
    
#     buyurtmalar.append(mahsulot)
#     javob = input('Yana taom tanlaysizmi? ha yoki yo\'q')
#     if javob == 'ha':
#         n+=1
#         continue
#     elif javob == 'yo\'q':
#         flag = False
#         print(buyurtmalar)

