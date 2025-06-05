# ⬛⬜⬛⬜⬛   Impurity-Doped Graphene Nanoribbons (ZGNRs)

> **Quantum engineering at the nanoscale:**  
> Explore the electronic band structure of *zigzag graphene nanoribbons* (ZGNRs) with and without single-site (Si) impurity, using a custom Python tight-binding model.

---

## 🧬 Project Scope

- **Pristine ZGNR:** Calculate and visualize the band structure of pure zigzag graphene nanoribbons.
- **Si-Doped ZGNR:** Analyze the effect of a single silicon impurity per unit cell—track the emergence of mid-gap states and bandgap modulation.
- **Extendable Framework:** The Hamiltonian and analysis are easily adaptable for different widths, impurity types, or other 1D nanostructures.

---

## 📂 Repository Structure

| File        | Purpose                                                                                       |
|-------------|----------------------------------------------------------------------------------------------|
| `GNRS.py`   | 🐍 Python code for building the Hamiltonian and plotting bands (pristine & Si-doped ZGNRs).  |
| `GNRS.pdf`  | 📖 Theory & derivations: Detailed construction of the Hamiltonian and physical discussion.    |
| `text.pdf`  | 📝 Supplementary notes and methods explanation.                                               |
| _References_| 📚 Key literature & PDFs supporting parameters and methodology.                               |

---

## 🛠️ Physical & Computational Approach

- **Model:** Nearest-neighbor tight-binding for $p_z$ orbitals.
- **Impurity Treatment:** On-site energy & hopping terms modified for Si impurity (ab initio & semi-empirical based).
- **Hamiltonian:** $12 \times 12$ matrix for width-6 ZGNR, explicitly constructed for both pure and doped cases.
- **Eigenproblem:** Compute band energies vs. $k$; identify impurity-induced localized states.

---

## 🚦 How to Run

1. **Install dependencies:**  
   ```bash
   pip install numpy matplotlib
