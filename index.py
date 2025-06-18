import openpyxl
wb = openpyxl.load_workbook('liste.xlsx')
sheet = wb['main'] 
print("appel")
print("réponder par abs ou pre")
lilo = input("lilo ? ")
sheet['A2'] = lilo
lila = input("lila ? ")
sheet['B2'] = lila
wb.save('liste.xlsx')
#valeur_cellule = sheet['C3'].value
#print("Valeur de la cellule C3 :", valeur_cellule)

