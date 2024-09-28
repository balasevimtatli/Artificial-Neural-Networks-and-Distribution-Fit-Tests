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
│   ├── distribution_of_non_error_data_by_activation_functions.png
│   ├── heatmap_of_all_error_data.png
│   ├── linear_distribution_goodness_of_fit.png
│   ├── relu_distribution_goodness_of_fit.png
│   ├── sigmoid_distribution_goodness_of_fit.png
│   ├── tanh_distribution_goodness_of_fit.png
│   ├── correct_prediction_data.png
│   ├── distribution_of_error_data_by_activation_functions.png
│   ├── linear_quota_table.xlsx
│   ├── relu_quota_table.xlsx
│   ├── sigmoid_quota_table.xlsx
│   ├── tanh_quota_table.xlsx
│   ├── comprehensive_graphing.py
│   ├── data_table_utilities.py
│   ├── fitness_plotting.py
│   ├── matrix_operations.py
│   ├── matrix_plotting.py
│   ├── plotting_utilities.py
│   └── rename_graph_files_script.ps1
├── keras/
│   ├── error_analysis_report_95.xlsx
│   ├── finalize_keras_model_training.py
│   ├── generate_non_compliant_data.py
│   ├── k95_prediction_report_update_control.xlsx
│   ├── rename_keras_files.ps1
│   └── rename_keras_files_script.ps1
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