# Calcul energie d'adsorption F sur diamant C(111)
E_slab   = -147.32903677  # Ry
E_slab_F = -206.68029516  # Ry
E_F      =  -59.07782699  # Ry
Ry_to_eV = 13.6057

E_ads_Ry = E_slab_F - E_slab - E_F
E_ads_eV = E_ads_Ry * Ry_to_eV

print(f"E(slab)      = {E_slab:.5f} Ry")
print(f"E(slab+F)    = {E_slab_F:.5f} Ry")
print(f"E(F atom)    = {E_F:.5f} Ry")
print(f"E_ads        = {E_ads_Ry:.5f} Ry")
print(f"E_ads        = {E_ads_eV:.3f} eV")
if E_ads_eV < 0:
    print("=> Adsorption spontanee et favorable")
