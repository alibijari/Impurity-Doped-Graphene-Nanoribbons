"""
Band Structure Calculation for Zigzag Graphene Nanoribbon (GNR)
---------------------------------------------------------------

This script calculates and plots the electronic band structure of a zigzag graphene nanoribbon (width = 6 atoms).
It covers both the pristine (pure) case and the case with one Si impurity per unit cell using the tight-binding method.

Requirements:
- numpy
- matplotlib

Author: [Your Name]
Date: February 12, 2024
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------- PARAMETERS ----------

# Common Parameters
t_C = 2.7  # Hopping parameter for C-C (eV)
a0 = 1.42  # Lattice constant (Å)
num_atoms = 12  # Number of atomic sites in the unit cell (6 dimers)

# For Si impurity case
E_C = 0  # On-site energy for Carbon
E_Si = 0.118  # On-site energy for Si impurity (eV)
t_Si = 1.123  # Hopping parameter for C-Si or Si-C (eV)
si_index = 2  # Index of Si atom in the unit cell (0-based index)

# k-space sampling
kx_values = np.linspace(-2.11 * np.pi / 3, 2.11 * np.pi / 3, 2000)


# ---------- FUNCTION: Pure GNR ----------

def calc_eigenvalues_pure(kx):
    """
    Constructs the tight-binding Hamiltonian for pristine (pure) zigzag GNR.
    Returns the sorted eigenvalues at a given kx.
    """
    E_s = 0
    a = -t_C + (-t_C * np.exp(-1j * kx * a0))
    b = -t_C + (-t_C * np.exp(+1j * kx * a0))

    # Hamiltonian for pure GNR (12x12, only nearest-neighbor interactions)
    H = np.zeros((num_atoms, num_atoms), dtype=complex)
    for i in range(num_atoms):
        H[i, i] = E_s  # on-site energy
        # Set nearest neighbor hopping terms (alternating a and b for edge connections)
        if i < num_atoms - 1:
            if i % 2 == 0:
                H[i, i + 1] = a
            else:
                H[i, i + 1] = -t_C
        if i > 0:
            if (i - 1) % 2 == 0:
                H[i, i - 1] = b
            else:
                H[i, i - 1] = -t_C
    # Periodic boundary conditions (edge-to-edge)
    # (not strictly necessary for nanoribbons, but can be included if desired)
    return np.sort(np.linalg.eigvals(H))


# ---------- FUNCTION: Si-Doped GNR ----------

def calc_eigenvalues_si_doped(kx):
    """
    Constructs the tight-binding Hamiltonian for a zigzag GNR with one Si impurity.
    Returns the sorted eigenvalues at a given kx.
    """
    H = np.zeros((num_atoms, num_atoms), dtype=complex)
    # On-site energies
    for i in range(num_atoms):
        H[i, i] = E_Si if i == si_index else E_C

    # Hopping terms (C-Si, Si-C, and C-C)
    for i in range(num_atoms):
        # right neighbor
        if i < num_atoms - 1:
            if i == si_index - 1 or i == si_index:
                # Bond involving Si atom
                hop = t_Si
            else:
                hop = t_C
            # phase factors for ribbon edge hopping
            if i % 2 == 0:
                phase = np.exp(-1j * kx * a0)
                H[i, i + 1] = -hop + (-hop * phase)
            else:
                H[i, i + 1] = -hop
        # left neighbor
        if i > 0:
            if i == si_index or i == si_index + 1:
                hop = t_Si
            else:
                hop = t_C
            if (i - 1) % 2 == 0:
                phase = np.exp(+1j * kx * a0)
                H[i, i - 1] = -hop + (-hop * phase)
            else:
                H[i, i - 1] = -hop
    return np.sort(np.linalg.eigvals(H))


# ---------- BAND STRUCTURE PLOTTING ----------

def plot_band_structure(eigenvalues, title):
    """
    Plots the band structure for a given array of eigenvalues vs. kx_values.
    """
    plt.figure(figsize=(10, 8))
    for band in eigenvalues:
        plt.plot(kx_values, np.real(band), lw=1)
    plt.title(title, fontsize=18, pad=18)
    plt.xlabel(r"$k_x$", fontsize=16, color="black", labelpad=10)
    plt.ylabel("Energy (eV)", fontsize=16, color="black", labelpad=10)
    plt.xticks(
        [-2.11 * np.pi / 3, 0, 2.11 * np.pi / 3],
        [r"$X$", r"$\Gamma$", r"$X$"]
    )
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------- MAIN EXECUTION ----------

if __name__ == "__main__":
    # --- Pristine Zigzag GNR ---
    eig_pure = np.array([calc_eigenvalues_pure(kx) for kx in kx_values]).T
    plot_band_structure(eig_pure, "Band Structure of Pristine Zigzag GNR (Width = 6 atoms)")

    # --- Si-Doped Zigzag GNR ---
    eig_doped = np.array([calc_eigenvalues_si_doped(kx) for kx in kx_values]).T
    plot_band_structure(eig_doped, "Band Structure of Zigzag GNR (Width = 6 atoms) with One Si Impurity")
