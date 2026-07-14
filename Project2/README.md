# Iris Flower Classification

A machine learning project that classifies Iris flowers into different species based on their physical measurements. The model is trained using the **K-Nearest Neighbors (KNN)** algorithm and demonstrates the complete classification workflow, including data preprocessing, model training, and performance evaluation.

---

## Badges

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Dataset](#dataset)
* [Technologies Used](#technologies-used)
* [Machine Learning Workflow](#machine-learning-workflow)
* [Installation](#installation)
* [Usage](#usage)
* [Screenshots](#screenshots)

---

## Project Overview
Classifying flowers based on their physical characteristics is a common machine learning classification problem. Measurements such as sepal length, sepal width, petal length, and petal width can be used to accurately identify different Iris species.

This project uses the **K-Nearest Neighbors (KNN)** algorithm to classify Iris flowers into their respective species. The workflow includes data preprocessing, feature scaling, model training, hyperparameter tuning, and performance evaluation.

---

## Features
* **Iris Flower Species Classification** using the KNN algorithm.
* **Data Preprocessing and Feature Scaling** utilizing Scikit-learn's `StandardScaler`.
* **Hyperparameter Tuning** to find the optimal K value based on error rates.
* **Confusion Matrix & Classification Report** for complete model evaluation.
* **Simple and Well-Structured Implementation** built using Scikit-learn and Jupyter Notebook.

---

## Dataset
The project uses the built-in Iris Dataset available in Scikit-learn. 

### Physical Features
* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

### Target Classes (Species)
* `setosa`
* `versicolor`
* `virginica`

### Sample Data
Here is a preview of how the dataset is structured:

| Sepal Length (cm) | Sepal Width (cm) | Petal Length (cm) | Petal Width (cm) | Species |
| :---: | :---: | :---: | :---: | :---: |
| 5.1 | 3.5 | 1.4 | 0.2 | setosa |
| 4.9 | 3.0 | 1.4 | 0.2 | setosa |
| 4.7 | 3.2 | 1.3 | 0.2 | setosa |
| 4.6 | 3.1 | 1.5 | 0.2 | setosa |
| 5.0 | 3.6 | 1.4 | 0.2 | setosa |

---

## Technologies Used
* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Scikit-learn**
* **Jupyter Notebook**

---

## Machine Learning Workflow
1. **Load the Iris dataset** using Scikit-learn.
2. **Split the dataset** into training (80%) and testing (20%) sets.
3. **Standardize the feature values** using `StandardScaler` to ensure features are scaled on a common range.
4. **Train multiple KNN models** with different K values (ranging from 1 to 24).
5. **Select the optimal K** based on the minimum error rate.
6. **Train the final KNN model** using the optimized K value.
7. **Predict the test data** and evaluate performance.
8. **Evaluate the model** using a Confusion Matrix and Performance Log.

---

## Installation

Clone the repository:
```bash
git clone https://github.com/MoazzamFarooqui/Iris-Flower-Classification.git
```

Navigate to the project directory:
```bash
cd Iris-Flower-Classification
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Open the notebook:
```bash
jupyter notebook
```

---

## Usage
1. Open the Jupyter Notebook environment.
2. Run all notebook cells sequentially.
3. Observe the preprocessing and feature scaling steps.
4. Train the KNN classifier and analyze the error rate plot.
5. View the optimal K value, the final diagnostic matrix, and the classification report.

---

## Screenshots

### Dataset Overview
*Initial look at the Iris features and species classification targets inside the Pandas DataFrame:*

```text
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) Species
0                5.1               3.5                1.4               0.2  setosa
1                4.9               3.0                1.4               0.2  setosa
2                4.7               3.2                1.3               0.2  setosa
3                4.6               3.1                1.5               0.2  setosa
4                5.0               3.6                1.4               0.2  setosa
```

### Error Rate vs. K Value
*Plot showing the classification error rate across different neighbor (K) settings to find the sweet spot:*

```text
[Matplotlib Generated Plot: Error Rate vs. K Value]
```

### Confusion Matrix
*Evaluation matrix displaying correct vs. incorrect classifications on the test partition:*

```text
--- DIAGNOSTIC MATRIX ---
            setosa  versicolor  virginica
setosa          10           0          0
versicolor       0           9          0
virginica        0           0         11
