#Uma pessoa vai ter dois trabalhos, na quinta e sexta
#Se os dois derem certo ela irá no shopping comprar uma tv 50 e a familia tomará sorvere
#Se apenas um dois derem ela irá no shopping comprar uma tv 50 e a familia tomará sorvere
#Se os dois trabalhos não derem certo, terá saúde.

trabalho_quinta = False
trabalho_sexta = False
tv_50 = trabalho_quinta and trabalho_sexta
tv_30 = trabalho_quinta or trabalho_sexta
saude = not trabalho_quinta and not trabalho_sexta

print(f"TV 50 e tomar sorvete {tv_50}") 
print(f"TV 30 e tomar sorvete {tv_30}") 
print(f"Saude {saude}") 



