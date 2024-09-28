# Artificial Neural Networks and Distribution Fit Tests

## Overview

This repository contains a comprehensive study on Artificial Neural Networks (ANNs) and Distribution Fit Tests, focusing on various activation functions and their impacts on prediction accuracy and error distribution.

## Project Structure

```
Artificial Neural Networks and Distribution Fit Tests/
├── generator/
│   ├── 9595_example_last_update_control_95_.xls
│   └── generator_95_percent.py
├── graphs/
│   ├── images/
│   │   └── [various .png files]
│   ├── data/
│   │   └── [various .xlsx files]
│   └── [various Python scripts]
├── keras/
│   ├── [various .xlsx files]
│   ├── [Python scripts]
│   └── [PowerShell scripts]
└── kolmogorov-smirnov/
    ├── distribution_control.py
    └── 95_Confidence_Distribution_Test_Results_All_Sheets.xlsx
```

## Key Components

1. **Data Generation**
   - Location: `generator/` folder
   - Key file: `generator_95_percent.py`
   - Purpose: Creates datasets for analysis

2. **Neural Network Models**
   - Location: `keras/` folder
   - Key file: `finalize_keras_model_training.py`
   - Purpose: Trains and evaluates neural network models

3. **Error Analysis and Visualization**
   - Location: `graphs/` folder
   - Key files: Various Python scripts for data processing and visualization
   - Purpose: Generates insightful visualizations of model performance and error distributions

4. **Distribution Fit Tests**
   - Location: `kolmogorov-smirnov/` folder
   - Key file: `distribution_control.py`
   - Purpose: Performs statistical tests to analyze error distributions

## Key Findings

### 1. Activation Function Performance

![Activation Function Performance](graphs/distribution_of_non_error_data_by_activation_functions.png)

This graph illustrates the distribution of correctly predicted data across different activation functions (ReLU, Sigmoid, Tanh, Linear). Key observations:
- ReLU and Linear functions show similar patterns across most categories.
- Sigmoid and Tanh functions demonstrate distinct behaviors in certain categories.
- The 'uniform' category shows the most consistent performance across all activation functions.

### 2. Error Distribution Analysis

![Error Distribution Heatmap](graphs/heatmap_of_all_error_data.png)

This heatmap visualizes the distribution of errors across different scenarios:
- Darker colors indicate higher error concentrations.
- The pattern suggests certain combinations of factors lead to more frequent errors.
- Some rows (scenarios) show consistently low error rates across all conditions.

### 3. Goodness of Fit for Different Activation Functions

#### Linear Activation Function
![Linear Distribution Goodness of Fit](graphs/linear_distribution_goodness_of_fit.png)

#### ReLU Activation Function
![ReLU Distribution Goodness of Fit](graphs/relu_distribution_goodness_of_fit.png)

#### Sigmoid Activation Function
![Sigmoid Distribution Goodness of Fit](graphs/sigmoid_distribution_goodness_of_fit.png)

#### Tanh Activation Function
![Tanh Distribution Goodness of Fit](graphs/tanh_distribution_goodness_of_fit.png)

These graphs demonstrate how well the error distributions for each activation function fit to theoretical probability distributions:
- Green bars represent a good fit, while red bars indicate a poor fit.
- The x-axis shows different distribution types (e.g., Beta, Cauchy, Exponential).
- Linear and ReLU functions show similar fitting patterns, while Sigmoid and Tanh have distinct characteristics.

## Usage

1. **Data Generation**: 
   ```
   python generator/generator_95_percent.py
   ```

2. **Model Training**: 
   ```
   python keras/finalize_keras_model_training.py
   ```

3. **Visualization and Analysis**: 
   ```
   python graphs/comprehensive_graphing.py
   ```

4. **Distribution Tests**: 
   ```
   python kolmogorov-smirnov/distribution_control.py
   ```

## Requirements

- Python 3.x
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib
- SciPy


## License

[Specify your license here]

## Contact

[Your contact information or link to issues page]