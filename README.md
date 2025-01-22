# entropy-screened-BO
## Introduction
This is a repository with open source code and the data for the paper "Artificial Intelligence-Driven Discovery of High-Entropy Alloys for Optimal Water Splitting Using Configuration Entropy and Design of Experiments". To run the entropy-screened BO.ipynb, use Entropy-screened BO dataset.csv. To run the bare BO with upper confidence bound (UCB), use Bare BO dataset.csv. Training the GPR model and plotting the overpotential with respect to element composition may take few minutes, depending on your hardware.

## Abstract
Water splitting for hydrogen production is essential in advancing the hydrogen economy. High-entropy alloys (HEAs) offer promising opportunities for optimizing this process, yet their vast compositional space and the presence of low-entropy local minima pose significant challenges for experimental and artificial intelligence (AI)-driven exploration. To overcome these challenges, a new AI method is developed by integrating Gaussian Process Regression with a thermodynamic configuration entropybased acquisition function for high-precision screening and a design of experiments (DoE) for data-efficient overpotential mapping. Through Bayesian optimization across 16.2 million HEA candidates, this entropy-screened and DoE dataset-trained AI discovers Fe12Co28Ni33Mo17Pd5Pt5 as the HEA for optimal water splitting. This HEA exhibits ultra-low overpotentials of 24 mV for hydrogen evolution and 204 mV for oxygen evolution at 10 mA·cm-2 with remarkable stability to yield an overall watersplitting overpotential of 228 mV, outperforming state-of-the-art metal-based electrocatalysts including Pt/C+IrO2, Pt35Ru65, and Ru-VO2 — showcasing groundbreaking capabilities unattainable by current methodologies.

## Schematic image of the Bayesian Optimization procedure

![Bayesian Optimization](https://github.com/user-attachments/assets/2bbf421b-ab5e-47fa-9391-395da2577e90)

## Operation of liquid handler (in 4x speed)



https://github.com/user-attachments/assets/f50458a2-79e6-4c31-89fb-8c291689cae2



## Dependencies
Python 3.x
<br/>numpy
<br/>Scipy
<br/>Scikit-learn
