import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def read_bands(filename):
    with open(filename) as f:
        content = f.read()
    bands = []
    for block in content.strip().split('\n\n'):
        if block.strip():
            arr = np.array([line.split() for line in block.strip().split('\n')], dtype=float)
            bands.append(arr)
    return bands

bands_clean = read_bands('diamond.bands.gnu')
bands_F     = read_bands('diamond_F.bands.gnu')

E_fermi_clean = -2.0
E_fermi_F     = -2.0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8), sharey=True)

for band in bands_clean:
    ax1.plot(band[:,0], band[:,1] - E_fermi_clean, 'b-', linewidth=0.8)
ax1.axhline(y=0, color='red', linestyle='--', linewidth=1)
ax1.set_title('C(111) — bare slab', fontsize=13)
ax1.set_ylabel('Energy (eV)', fontsize=12)
ax1.set_ylim(-20, 20)
k = bands_clean[0][:,0]
n = len(k)
pos = [k[0], k[n//3], k[2*n//3], k[-1]]
ax1.set_xticks(pos)
ax1.set_xticklabels(['Γ', 'K', 'M', 'Γ'], fontsize=12)
for p in pos:
    ax1.axvline(x=p, color='k', linewidth=0.5)
ax1.grid(axis='y', alpha=0.3)
ax1.text(0.05, 0.97, 'Surface states\nat E_Fermi', transform=ax1.transAxes,
         fontsize=10, color='red', va='top')

for band in bands_F:
    ax2.plot(band[:,0], band[:,1] - E_fermi_F, 'g-', linewidth=0.8)
ax2.axhline(y=0, color='red', linestyle='--', linewidth=1)
ax2.set_title('C(111) + F — E_ads = -3.720 eV', fontsize=13)
ax2.set_ylim(-20, 20)
k2 = bands_F[0][:,0]
n2 = len(k2)
pos2 = [k2[0], k2[n2//3], k2[2*n2//3], k2[-1]]
ax2.set_xticks(pos2)
ax2.set_xticklabels(['Γ', 'K', 'M', 'Γ'], fontsize=12)
for p in pos2:
    ax2.axvline(x=p, color='k', linewidth=0.5)
ax2.grid(axis='y', alpha=0.3)
ax2.text(0.05, 0.97, 'Gap opens\nafter F adsorption', transform=ax2.transAxes,
         fontsize=10, color='green', va='top')

plt.suptitle('Effect of F termination on Diamond C(111) band structure', fontsize=14)
plt.tight_layout()
plt.savefig('bands_comparison.png', dpi=150)
print("Figure sauvegardee : bands_comparison.png")
