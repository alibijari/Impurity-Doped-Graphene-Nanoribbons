# Impurity-Doped Graphene Nanoribbons

This repository contains Python code and theoretical resources for calculating the electronic band structure of **zigzag graphene nanoribbons (ZGNRs)** with and without single-site (Si) impurities, using the tight-binding model. The project tracks the emergence of impurity-induced mid-gap states and provides a framework for studying the impact of atomic substitutions on the electronic properties of graphene-based nanostructures.

---

## Overview

Graphene nanoribbons (GNRs) exhibit unique quantum properties due to their reduced dimensionality and edge structure. Impurity doping, such as the substitution of a carbon atom by silicon, can introduce localized states and modify the bandgap—making GNRs candidates for tunable nanoelectronic devices.

This project implements and visualizes:
- **Band structure of pristine (pure) zigzag GNRs**
- **Band structure of zigzag GNRs with a single Si impurity per unit cell**

The tight-binding Hamiltonian is explicitly constructed for a ribbon of width 6 atoms. Both the code and accompanying theory document are designed to be extensible for other widths or impurity types.

---

## Files

- **GNRS.py**: Python script for building the tight-binding Hamiltonian, computing energy eigenvalues across the Brillouin zone, and plotting the band structures for pure and Si-doped cases.
- **GNRS.pdf**: Detailed theoretical background, including matrix forms of the Hamiltonian for both cases, physical assumptions, and mathematical derivation.
- **text.pdf**: (Optional) Supplementary notes and explanation of the methods.
- **Other reference PDFs**: Key literature supporting the methodology and parameter choices.

---

## Physical and Computational Approach

- **Tight-binding model:** Nearest-neighbor hopping between p_z orbitals of carbon, extended to include Si–C and Si–Si hopping for the impurity case.
- **Hamiltonian construction:** Explicit 12×12 matrix for a nanoribbon with 6 zigzag chains.
- **Impurity modeling:** Si substitution modifies on-site energies and hopping terms as per ab-initio and semi-empirical references.
- **Eigenvalue analysis:** Band energies are calculated for each k-point, with special focus on mid-gap states arising due to impurities.

---

## How to Use

1. Install required Python modules:  
   ```bash
   pip install numpy matplotlib
python GNRS.py
