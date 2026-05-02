import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = np.loadtxt('diamond.bands.gnu')
k = data[:, 0]
E = data[:, 1]

# Trouver les sauts (lignes vides separent les bandes)
with open('diamond.bands.gnu') as f:
    content = f.read()

bands = []
for block in content.strip().split('\n\n'):
    if block.strip():
        arr = np.array([line.split() for line in block.strip().split('\n')], dtype=float)
        bands.append(arr)

E_fermi = -2.0

fig, ax = plt.subplots(figsize=(6, 8))
for band in bands:
    ax.plot(band[:,0], band[:,1] - E_fermi, 'b-', linewidth=0.8)

ax.axhline(y=0, color='red', linestyle='--', linewidth=1, label='E_Fermi')
ax.set_ylabel('Energy (eV)', fontsize=12)
ax.set_title('Band structure — Diamond C(111) slab', fontsize=13)
ax.set_ylim(-20, 20)

k_all = bands[0][:,0]
n = len(k_all)
positions = [k_all[0], k_all[n//3], k_all[2*n//3], k_all[-1]]
ax.set_xticks(positions)
ax.set_xticklabels(['Γ', 'K', 'M', 'Γ'], fontsize=12)
for p in positions:
    ax.axvline(x=p, color='k', linewidth=0.5)

ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('band_structure.png', dpi=150)
print("Figure sauvegardee : band_structure.png")
