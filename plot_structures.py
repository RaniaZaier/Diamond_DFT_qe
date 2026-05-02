import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Positions atomiques en angstrom
C_positions = np.array([
    [0.000, 0.000],
    [1.261, 0.515],
    [0.000, 2.060],
    [1.261, 2.575],
    [0.000, 4.120],
    [1.261, 4.635],
    [0.000, 6.180],
    [1.261, 6.695],
])

F_position = np.array([0.000, 8.100])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8), sharey=True)

# --- Slab seul ---
ax1.scatter(C_positions[:,0], C_positions[:,1],
            s=400, c='#8B6914', zorder=5, label='C', edgecolors='black', linewidths=0.8)

# Liaisons C-C
bonds = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)]
for i,j in bonds:
    ax1.plot([C_positions[i,0], C_positions[j,0]],
             [C_positions[i,1], C_positions[j,1]],
             'k-', linewidth=1.5, zorder=3)

ax1.set_title('C(111) — bare slab', fontsize=13)
ax1.set_xlim(-1, 3)
ax1.set_ylim(-1, 10)
ax1.set_xlabel('x (Å)', fontsize=11)
ax1.set_ylabel('z (Å)', fontsize=11)
ax1.axhline(y=7.5, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='Surface')
ax1.legend(loc='upper right', fontsize=10)
ax1.set_facecolor('#f8f8f8')
ax1.text(0.5, 0.02, 'Dangling bonds\nat surface', transform=ax1.transAxes,
         ha='center', fontsize=10, color='red',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# --- Slab + F ---
ax2.scatter(C_positions[:,0], C_positions[:,1],
            s=400, c='#8B6914', zorder=5, label='C', edgecolors='black', linewidths=0.8)
ax2.scatter(F_position[0], F_position[1],
            s=500, c='#00CC44', zorder=5, label='F', edgecolors='black', linewidths=0.8)

for i,j in bonds:
    ax2.plot([C_positions[i,0], C_positions[j,0]],
             [C_positions[i,1], C_positions[j,1]],
             'k-', linewidth=1.5, zorder=3)

# Liaison C-F
ax2.plot([C_positions[-1,0], F_position[0]],
         [C_positions[-1,1], F_position[1]],
         'g-', linewidth=2.5, zorder=3)

ax2.set_title('C(111) + F — E_ads = -3.720 eV', fontsize=13)
ax2.set_xlim(-1, 3)
ax2.set_ylim(-1, 10)
ax2.set_xlabel('x (Å)', fontsize=11)
ax2.axhline(y=7.5, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax2.legend(loc='upper right', fontsize=10)
ax2.set_facecolor('#f8f8f8')
ax2.text(0.5, 0.02, 'C-F bond formed\nsurface passivated', transform=ax2.transAxes,
         ha='center', fontsize=10, color='green',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.suptitle('Diamond C(111) surface — effect of F adsorption', fontsize=14)
plt.tight_layout()
plt.savefig('structures_comparison.png', dpi=150)
print("Figure sauvegardee : structures_comparison.png")
