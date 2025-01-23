# entropy-screened-BO

## Contents
+ **[Overview](
https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/README.md#overview)**

+ **[Paper Abstract](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#paper-abstract)**
  

+ **[Implementing the code](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main#implementing-the-code)**


+ **[Dependencies](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#dependencies)**


+ **[Acknowledgements](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/README.md#acknowledgements)**


+ **[Contact/Bug report](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/README.md#contactbug-report)**
  
## Overview
This is a repository with open source code and the data for the paper "Artificial Intelligence-Driven Discovery of High-Entropy Alloys for Optimal Water Splitting Using Configuration Entropy and Design of Experiments". <br/>
+ Schematic illustration of the entire optimization procedure

![Bayesian Optimization](https://github.com/user-attachments/assets/2bbf421b-ab5e-47fa-9391-395da2577e90)

+ Operation of liquid handler (in 4x speed)
  
https://github.com/user-attachments/assets/f50458a2-79e6-4c31-89fb-8c291689cae2


## Paper Abstract
Water splitting for hydrogen production is essential in advancing the hydrogen economy. High-entropy alloys (HEAs) offer promising opportunities for optimizing this process, yet their vast compositional space and the presence of low-entropy local minima pose significant challenges for experimental and artificial intelligence (AI)-driven exploration. To overcome these challenges, a new AI method is developed by integrating Gaussian Process Regression with a thermodynamic configuration entropy-based acquisition function for high-precision screening and a design of experiments (DoE) for data-efficient overpotential mapping. Through Bayesian optimization across 16.2 million HEA candidates, this entropy-screened and DoE dataset-trained AI discovers Fe12Co28Ni33Mo17Pd5Pt5 as the HEA for optimal water splitting. This HEA exhibits ultra-low overpotentials of 24 mV for hydrogen evolution and 204 mV for oxygen evolution at 10 mA·cm-2 with remarkable stability to yield an overall watersplitting overpotential of 228 mV, outperforming state-of-the-art metal-based electrocatalysts including Pt/C+IrO2, Pt35Ru65, and Ru-VO2 — showcasing groundbreaking capabilities unattainable by current methodologies.


## Implementing the ML model & DFT calculation

+ To run the [**entropy-screened BO.ipynb**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Model/Entropy-screened%20BO.ipynb) in **Model** folder, use [**Entropy-screened BO dataset.csv**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Data/Experimental/Entropy-screened%20BO%20dataset.csv) in **Data/Experimental**.
<br/><br/>

+ To run the [**Bare BO.ipynb**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Model/Bare%20BO.ipynb) with upper confidence bound in **Model** folder, use [**Bare BO dataset.csv**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Data/Experimental/Bare%20BO%20dataset.csv) in **Data/Experimental**.
<br/><br/>

+ Training the GPR model and plotting the overpotential with respect to element composition may take few minutes, depending on your hardware.
<br/><br/>

+ To find out the crystal structures governed by SQS computation, go to [**Data/Structures**](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main/Data/Structures).
<br/><br/>

+ To find out the outputs for DFT calculation using Quantum Espresso (e.g. structure, density of states, charge density), go to [**Data/DFT**](Data/DFT).
<br/><br/>

+ All the DFT calculations were conducted using **Quantum ESPRESSO 6.4**. 

## Dependencies
+ Python 3.x <br/>
+ numpy >1.25 <br/>
+ Scipy >1.11.2 <br/>
+ Scikit-learn >1.3.2 <br/>
+ SHAP (can be installed either from pip or conda-forge) 

## Acknowledgements
+ This research was supported by the National Research Foundation of Korea (2022M3H4A1A04096482, RS-2023-00229679) funded by the Ministry of Science and ICT.


## Contact/Bug report
+ For inquiries regarding the paper or bug report of the code given, please send an email to jihoonkim@kaist.ac.kr
