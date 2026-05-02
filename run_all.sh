#!/bin/bash
# DFT workflow: F adsorption on diamond C(111)
# Rania Zaier — 2026
# Usage: bash run_all.sh

set -e
QE=~/q-e/bin
DIR=~/diamond_project

echo "============================================"
echo " DFT workflow: F adsorption on diamond C(111)"
echo " Rania Zaier — 2026"
echo "============================================"

cd $DIR

echo ""
echo "[1/8] Geometry optimization — bare slab..."
$QE/pw.x < diamond_slab.in > diamond_slab.out 2>&1
echo "      Done. E(slab) = $(grep '!' diamond_slab.out | tail -1 | awk '{print $5}') Ry"

echo ""
echo "[2/8] Geometry optimization — slab + F..."
$QE/pw.x < adsorption_F.in > adsorption_F.out 2>&1
echo "      Done. E(slab+F) = $(grep '!' adsorption_F.out | tail -1 | awk '{print $5}') Ry"

echo ""
echo "[3/8] SCF — isolated F atom..."
$QE/pw.x < F_atom.in > F_atom.out 2>&1
echo "      Done. E(F) = $(grep '!' F_atom.out | tail -1 | awk '{print $5}') Ry"

echo ""
echo "[4/8] Adsorption energy..."
python3 analyse_adsorption.py

echo ""
echo "[5/8] Band structure SCF — bare slab..."
$QE/pw.x < bands_scf.in > bands_scf.out 2>&1
echo "      Done."

echo ""
echo "[6/8] Band structure calculation — bare slab..."
$QE/pw.x < bands_calc.in > bands_calc.out 2>&1
$QE/bands.x < bands_pp.in > bands_pp.out 2>&1
python3 plot_bands.py
echo "      Done. -> band_structure.png"

echo ""
echo "[7/8] Band structure SCF — slab + F..."
$QE/pw.x < bands_F_scf.in > bands_F_scf.out 2>&1
$QE/pw.x < bands_F_calc.in > bands_F_calc.out 2>&1
$QE/bands.x < bands_F_pp.in > bands_F_pp.out 2>&1
echo "      Done."

echo ""
echo "[8/8] Band structure comparison plot..."
python3 plot_bands_comparison.py
echo "      Done. -> bands_comparison.png"

echo ""
echo "============================================"
echo " All calculations complete!"
echo " Results:"
echo "   - diamond_slab.out"
echo "   - adsorption_F.out"
echo "   - band_structure.png"
echo "   - bands_comparison.png"
echo "============================================"
