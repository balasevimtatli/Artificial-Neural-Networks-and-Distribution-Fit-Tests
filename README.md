# Artificial Neural Networks and Distribution Fit Tests

## Project Overview

This repository contains a comprehensive study on Artificial Neural Networks (ANNs) and Distribution Fit Tests, focusing on various activation functions and their impacts on prediction accuracy and error distribution.

## Project Structure

```
Artificial Neural Networks and Distribution Fit Tests/
├── generator/
│   ├── generator_95_percent.py
│   └── 9595_example_last_update_control_95_.xls
├── graphs/
│   ├── Images/
│   │   ├── distribution_of_error_data_by_activation_functions.png
│   │   ├── distribution_of_non_error_data_by_activation_functions.png
│   │   ├── heatmap_of_all_error_data.png
│   │   ├── linear_distribution_goodness_of_fit.png
│   │   ├── relu_distribution_goodness_of_fit.png
│   │   ├── sigmoid_distribution_goodness_of_fit.png
│   │   ├── tanh_distribution_goodness_of_fit.png
│   │   └── correct_prediction_data.png
│   ├── Data/
│   │   ├── linear_quota_table.xlsx
│   │   ├── relu_quota_table.xlsx
│   │   ├── sigmoid_quota_table.xlsx
│   │   └── tanh_quota_table.xlsx
│   ├── comprehensive_graphing.py
│   ├── data_table_utilities.py
│   ├── fitness_plotting.py
│   ├── matrix_operations.py
│   ├── matrix_plotting.py
│   ├── plotting_utilities.py
│   └── rename_graph_files_script.ps1
├── keras/
│   ├── finalize_keras_model_training.py
│   ├── generate_non_compliant_data.py
│   ├── k95_prediction_report_update_control.xlsx
│   └── error_analysis_report_95.xlsx
└── kolmogorov-smirnov/
    ├── distribution_control.py
    └── 95_Confidence_Distribution_Test_Results_All_Sheets.xlsx
```

## Component Details

### 1. Generator

- **Location**: `generator/` folder
- **Files**:
  - `generator_95_percent.py`: Script for generating data sets
  - `9595_example_last_update_control_95_.xls`: Example output from the generator

### 2. Graphs

- **Location**: `graphs/` folder
- **Subfolders**:
  - `Images/`: Contains all generated visualization PNG files
  - `Data/`: Contains quota tables for different activation functions
- **Python Scripts**:
  - `comprehensive_graphing.py`: Main script for creating all graphs
  - `data_table_utilities.py`: Utilities for handling data tables
  - `fitness_plotting.py`: Functions for plotting fitness-related graphs
  - `matrix_operations.py`: Matrix manipulation utilities
  - `matrix_plotting.py`: Functions for plotting matrix-based visualizations
  - `plotting_utilities.py`: General plotting utility functions
- **Other Files**:
  - `rename_graph_files_script.ps1`: PowerShell script for renaming graph files

### 3. Keras

- **Location**: `keras/` folder
- **Files**:
  - `finalize_keras_model_training.py`: Script for finalizing and training Keras models
  - `generate_non_compliant_data.py`: Script for generating non-compliant data for testing
  - `k95_prediction_report_update_control.xlsx`: Prediction report
  - `error_analysis_report_95.xlsx`: Detailed error analysis report

### 4. Kolmogorov-Smirnov

- **Location**: `kolmogorov-smirnov/` folder
- **Files**:
  - `distribution_control.py`: Script for performing Kolmogorov-Smirnov distribution tests
  - `95_Confidence_Distribution_Test_Results_All_Sheets.xlsx`: Comprehensive test results

## Key Visualizations

1. **Error Distribution by Activation Functions**
   - File: `graphs/Images/distribution_of_error_data_by_activation_functions.png`
   - Description: Visualizes how errors are distributed across different activation functions.

2. **Non-Error Data Distribution by Activation Functions**
   - File: `graphs/Images/distribution_of_non_error_data_by_activation_functions.png`
   - Description: Shows the distribution of correctly predicted data for each activation function.

3. **Heatmap of All Error Data**
   - File: `graphs/Images/heatmap_of_all_error_data.png`
   - Description: Provides a comprehensive view of error patterns across all scenarios.

4. **Goodness of Fit for Activation Functions**
   - Files:
     - `graphs/Images/linear_distribution_goodness_of_fit.png`
     - `graphs/Images/relu_distribution_goodness_of_fit.png`
     - `graphs/Images/sigmoid_distribution_goodness_of_fit.png`
     - `graphs/Images/tanh_distribution_goodness_of_fit.png`
   - Description: These graphs show how well the error distributions for each activation function fit to theoretical probability distributions.

5. **Correct Prediction Data**
   - File: `graphs/Images/correct_prediction_data.png`
   - Description: Visualizes the patterns in correctly predicted data.

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