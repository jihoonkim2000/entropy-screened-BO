# AI-driven design of multiprincipal element alloys for optimal water splitting 

## Contents
+ **[Overview](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#overview)**

+ **[Paper Abstract](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#paper-abstract)**
  

+ **[Implementing the code](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#implementing-the-ml-model--dft-calculation)**


+ **[Dependencies](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#dependencies)**


+ **[Acknowledgements](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#acknowledgements)**


+ **[Contact/Bug report](https://github.com/jihoonkim2000/entropy-screened-BO/tree/main?tab=readme-ov-file#contactbug-report)**
  
## Overview
This is a repository with open source code and the data for the paper "AI-driven design of multiprincipal element allioys for optimal water splititng". <br/>
+ Schematic illustration of the entire optimization procedure

![Fig1A](https://github.com/user-attachments/assets/b9d083d8-cc81-4420-b006-def786dfd39f)



+ 3D reconstruction of final MPEA


https://github.com/user-attachments/assets/dc943b0f-649c-4176-b000-090a2e8510e8


+ Operation of liquid handler (in 4x speed)
  
https://github.com/user-attachments/assets/f50458a2-79e6-4c31-89fb-8c291689cae2

## Paper Abstract
Water splitting for hydrogen production is essential in advancing the hydrogen economy. Multi-principal element alloys (MPEAs) offer promising opportunities for optimizing this process, yet their vast compositional space and the presence of local minima pose significant challenges for experimental and artificial intelligence (AI)-driven exploration. To overcome these challenges, a new AI framework is developed by integrating Gaussian Process Regression with a configuration entropy-based acquisition function for screening and a design of experiments (DoE) for data-efficient overpotential mapping. Through Bayesian optimization across 16.2 million chemical compositions, this entropy-screened and DoE dataset-trained AI discovers Fe₁₂Co₂₈Ni₃₃Mo₁₇Pd₅Pt₅ as the best composition for water splitting within its search space. The alloy exhibits ultra-low overpotentials of 24 mV for hydrogen evolution and 204 mV for oxygen evolution at 10 mA·cm⁻² with robust stability, surpassing state-of-the-art non-noble and noble metal electrocatalysts including Pt/C+IrO₂, Pt₃₅Ru₆₅, and Ru-VO₂-demonstrating unprecedented performance beyond reach by contemporary experimental and AI frameworks.


## Implementing the ML model & DFT calculation

+ To run the [**entropy-screened BO.ipynb**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Model/Entropy-screened%20BO.ipynb) in **Model** folder, use [**Entropy-screened BO dataset.csv**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Data/Experimental/Entropy-screened%20BO%20dataset.csv) in **Data/Experimental**.
<br/><br/>

+ To run the [**Bare BO.ipynb**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Model/Bare%20BO.ipynb) with upper confidence bound in **Model** folder, use [**Bare BO dataset.csv**](https://github.com/jihoonkim2000/entropy-screened-BO/blob/main/Data/Experimental/Bare%20BO%20dataset.csv) in **Data/Experimental**.
<br/><br/>

+ Training the GPR model and plotting the overpotential with respect to element composition may take few minutes, depending on your hardware.
<br/><br/>

+ To reproduce the figures in the paper, go to [**Figures**](Figures)

+ To fetch raw DOS data, go to [**Data/DFT/DOS**](Data/DFT/DOS)

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
+ For inquiries regarding the paper or bug report of the code given, please send an email to jihoonkim2000@snu.ac.kr
