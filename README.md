 🧬 Protein–Protein Interaction Predictor (TUI Interface)

A **Terminal-based User Interface (TUI)** Python application for predicting protein–protein interactions using state-of-the-art deep learning models like **ProtBERT**. Designed for researchers, students, and bioinformaticians to interactively predict and explore recent advances in protein interaction prediction.

---
 🔍 Features

- 🧠 **Deep Learning**-based prediction using `Rostlab/prot_bert`
- ⌨️ **Rich TUI Interface** using the `rich` library
- 📚 View recent research papers on Deep Learning & PPI
- 📁 Supports input from FASTA files or direct sequence entry

 🏗️ Project Structure


---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ppi-tui-predictor.git
   cd ppi-tui-predictor
pip install -r requirements.txt
python main.py


─────────────────────────────────────────────────────── PPI TUI Menu ───────────────────────────────────────────────────────
[1] Predict PPI
[2] Show Recent Papers
[3] Exit
Choose an option [1/2/3]: 1

Enter first protein sequence: MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLF
Enter second protein sequence: MADQLTEEQIAEFKEAFSLFDKDGDGTITTKEA

Predicted Interaction Score: 0.8620


1. AlphaFold-Multimer: Complex protein prediction (Nature, 2021)
2. ESM2: Evolutionary-scale modeling of proteins (Nature, 2023)
3. GraphPPIs: Graph Attention for PPI (Bioinformatics, 2022)
4. ProtTrans: BERT-style models for protein sequences (EMBO J, 2021)


pip install -r requirements.txt

