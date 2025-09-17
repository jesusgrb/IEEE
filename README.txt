# Genre-Sensitive Prediction of Emotional Arousal in Virtual Reality: A Neural Modeling Approach Using Skin Conductance Peaks

**Manuscript ID:** [10067]

## Authors and Affiliations
- Demian Velasco Gómez Llanos, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México
- Santiago Arreola Munguía, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México
- Marco Antonio Manjarrez Fernández, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México
- Juan Pablo Villaseñor Navares, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México
- Violeta Corona, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México
- Jesús Gómez-Romero Borquez, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México
- José Varela-Aldás, Universidad Tecnológica Indoamérica, Facultad de Ingenierías, Ambato, Ecuador
- Carolina Del-Valle-Soto, Universidad Panamericana, Facultad de Ingeniería, Guadalajara, México

---

## Repository Content

This repository contains the experimental code and datasets used to replicate the results presented in the article.  
Each file is described in the following table.

| File name  | Description | Notes |
|------------|-------------|-------|
| `graphs.m` | MATLAB script to generate statistical visualizations of SCR data, including boxplots, mean/std barplots, regression scatterplots, histograms, and model training/validation curves. | Reproduces Figures 1–5 of the paper. |
| `moving.m` | MATLAB script to compute and visualize the temporal dynamics of SCR signals across VR game genres, applying smoothing techniques. | Reproduces Figure 6 of the paper. |
| `Data.zip` | Compressed archive containing all participant datasets (`.csv.gz` files). | Must be extracted into the `Data/` folder before running scripts. |
| `README.txt` | Documentation of the repository, including title, ID, authors, affiliations, and description of files. | – |

---
List of files:
- https://github.com/jesusgrb/IEEE/001_alondra.csv.gz – Raw SCR peaks for participant Alondra
- https://github.com/jesusgrb/IEEE/002_braulio.csv.gz – Raw SCR peaks for participant Braulio
- https://github.com/jesusgrb/IEEE/003_Ana.csv.gz – Raw SCR peaks for participant Ana
- https://github.com/jesusgrb/IEEE/004_carlos.csv.gz – Raw SCR peaks for participant Carlos
- https://github.com/jesusgrb/IEEE/005_daniela.csv.gz – Raw SCR peaks for participant Daniela
- https://github.com/jesusgrb/IEEE/006_eduardo.csv.gz – Raw SCR peaks for participant Eduardo
- https://github.com/jesusgrb/IEEE/007_fernanda.csv.gz – Raw SCR peaks for participant Fernanda
- https://github.com/jesusgrb/IEEE/008_gabriel.csv.gz – Raw SCR peaks for participant Gabriel
- https://github.com/jesusgrb/IEEE/009_isabel.csv.gz – Raw SCR peaks for participant Isabel
- https://github.com/jesusgrb/IEEE/010_jorge.csv.gz – Raw SCR peaks for participant Jorge
- https://github.com/jesusgrb/IEEE/011_karla.csv.gz – Raw SCR peaks for participant Karla
- https://github.com/jesusgrb/IEEE/012_luis.csv.gz – Raw SCR peaks for participant Luis
- https://github.com/jesusgrb/IEEE/013_maria.csv.gz – Raw SCR peaks for participant Maria
- https://github.com/jesusgrb/IEEE/014_nicolas.csv.gz – Raw SCR peaks for participant Nicolas
- https://github.com/jesusgrb/IEEE/015_olivia.csv.gz – Raw SCR peaks for participant Olivia
- https://github.com/jesusgrb/IEEE/016_pedro.csv.gz – Raw SCR peaks for participant Pedro
- https://github.com/jesusgrb/IEEE/017_queralt.csv.gz – Raw SCR peaks for participant Queralt
- https://github.com/jesusgrb/IEEE/018_ricardo.csv.gz – Raw SCR peaks for participant Ricardo
- https://github.com/jesusgrb/IEEE/019_silvia.csv.gz – Raw SCR peaks for participant Silvia
- https://github.com/jesusgrb/IEEE/020_tomas.csv.gz – Raw SCR peaks for participant Tomas
- https://github.com/jesusgrb/IEEE/021_ursula.csv.gz – Raw SCR peaks for participant Ursula
- https://github.com/jesusgrb/IEEE/022_valeria.csv.gz – Raw SCR peaks for participant Valeria
- https://github.com/jesusgrb/IEEE/023_walter.csv.gz – Raw SCR peaks for participant Walter
- https://github.com/jesusgrb/IEEE/024_ximena.csv.gz – Raw SCR peaks for participant Ximena
- https://github.com/jesusgrb/IEEE/025_yahir.csv.gz – Raw SCR peaks for participant Yahir
- https://github.com/jesusgrb/IEEE/026_zulema.csv.gz – Raw SCR peaks for participant Zulema
- https://github.com/jesusgrb/IEEE/027_paola.csv.gz – Raw SCR peaks for participant Paola

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/jesusgrb/IEEE.git
   cd IEEE
   ```

2. Extract `Data.zip` into the `Data/` folder.

3. Open MATLAB R2020a (or later).

4. Run scripts in MATLAB:
   ```matlab
   run('graphs.m');
   run('moving.m');
   ```

5. Figures will be generated in the current working directory.

---

## Requirements

- MATLAB R2020a or later (tested).  
- GNU Octave 6.0+ (partial compatibility).  

---

## Citation

If you use this repository, please cite the corresponding paper:

*D. Velasco Gómez Llanos, S. Arreola Munguía, M. A. Manjarrez Fernández, J. P. Villaseñor Navares, V. Corona, J. Gómez-Romero Borquez, J. Varela-Aldás, and C. Del-Valle-Soto. “Genre-Sensitive Prediction of Emotional Arousal in Virtual Reality: A Neural Modeling Approach Using Skin Conductance Peaks,” IEEE LATAM Transactions, 2025.*

---

## License

This repository is distributed for academic and research purposes only. See LICENSE for details.
