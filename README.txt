README - Experimental Repository for Paper Replication
=======================================================

Overview
--------
This repository contains the experimental materials, datasets, and MATLAB scripts associated with the replication and validation of the results presented in the paper. The objective is to provide transparency, reproducibility, and accessibility for researchers interested in the physiological analysis of Skin Conductance Responses (SCR) under different immersive conditions.

Contents
--------
- **Data in Github/**  
  Compressed datasets and raw measurements in `.zip` and `.txt` formats. These include SCR recordings across different experimental conditions and genres.

- **Scripts/**  
  MATLAB scripts used to preprocess, visualize, and statistically analyze SCR data. The scripts generate boxplots, bar plots, regression comparisons, histograms, and learning curves for model performance.

- **Figures/**  
  Automatically generated figures from the scripts, illustrating SCR distributions, real vs. predicted performance, loss curves, and temporal dynamics of SCR across game genres.

Usage
-----
1. Download or clone the repository.  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Extract the `Data.zip` file inside the `Data/` folder.

3. Open MATLAB (or Octave-compatible environment).

4. Run the analysis scripts located in `Scripts/`. Example:
   ```matlab
   run('grpahs.txt');
   run('mov.txt');
   ```

5. Figures and statistical outputs will be generated in the current working directory.

Requirements
------------
- MATLAB R2020a or later (tested), or GNU Octave 6.0+ (partially supported).  
- Basic knowledge of MATLAB scripting and data visualization.

Citation
--------
If you use or adapt this repository, please cite the corresponding paper and provide credit to the original authors.

License
-------
This repository is distributed for academic and research purposes only. Please check the LICENSE file for details.
