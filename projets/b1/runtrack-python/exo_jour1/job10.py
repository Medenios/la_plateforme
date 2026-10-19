montant_init = 2000
taux = 1
montant = montant_init * (1 + taux / 100)
print(f"montant  : {montant:.2f} €")
montant1 = montant + 5000
taux = taux + 2
montant2 = montant1 * (1 + taux / 100)
print(f"montant 2 : {montant2:.2f} €")
taux = taux - 1
montant3 = montant2 * (1 + taux / 100)
print(f"montant 3 : {montant3:.2f} €")
