nom = "Clavier"
prix_unitaire = 25.50
quantite_stock = 10

print("===== INFORMATIONS DU PRODUIT =====")
print(f"Nom              : {nom}")
print(f"Prix unitaire    : {prix_unitaire:.2f} €")
print(f"Quantité en stock: {quantite_stock}")
print()

quantite_ajoutee = 15
quantite_stock = quantite_stock + quantite_ajoutee
print(f"{quantite_ajoutee} produits ajoutés en stock.")
print(f"Nouveau stock : {quantite_stock}")
print()

quantite_achat = int(input("Combien de produits voulez-vous acheter ? "))

if quantite_achat <= 0:
    print("Quantité invalide : elle doit être supérieure à 0.")
elif quantite_achat > quantite_stock:
    print(f"Stock insuffisant ! Il ne reste que {quantite_stock} produit(s).")
else:
    quantite_stock = quantite_stock - quantite_achat
    total = quantite_achat * prix_unitaire
    print(f"Achat de {quantite_achat} produit(s) validé.")
    print(f"Total à payer : {total:.2f} €")

print()

prix_unitaire = prix_unitaire * 1.10
print("Le prix a augmenté de 10 % à cause de l'inflation.")
print()

print("===== INFORMATIONS MISES À JOUR =====")
print(f"Nom              : {nom}")
print(f"Prix unitaire    : {prix_unitaire:.2f} €")
print(f"Quantité en stock: {quantite_stock}")
