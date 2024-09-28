```markdown
# Artificial Neural Networks and Distribution Fit Tests

Welcome to the **Artificial Neural Networks and Distribution Fit Tests** project! This repository contains a collection of scripts, utilities, and visualizations aimed at analyzing the performance of various activation functions in artificial neural networks, along with statistical distribution tests.

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Visualizations](#visualizations)
- [Statistical Tests](#statistical-tests)
- [License](#license)

## Project Overview

This project provides tools and methodologies for analyzing the effectiveness of different activation functions in neural networks. It includes scripts for generating data, visualizing distributions, and performing statistical tests to validate model performance.

## Folder Structure

```plaintext
Artificial Neural Networks and Distribution Fit Tests/
├── Data_Generation_Scripts/
│   ├── 9595_example_last_update_control_95_.xls
│   ├── generator_95_percent.py
├── Visualization_Scripts/
│   ├── comprehensive_graphing.py
│   ├── data_table_utilities.py
│   ├── fitness_plotting.py
│   ├── matrix_operations.py
│   ├── matrix_plotting.py
│   ├── plotting_utilities.py
│   ├── rename_graph_files_script.ps1
│   ├── linear_quota_table.xlsx
│   ├── relu_quota_table.xlsx
│   ├── sigmoid_quota_table.xlsx
│   ├── tanh_quota_table.xlsx
│   ├── distribution_of_error_data_by_activation_functions.png
│   ├── distribution_of_non_error_data_by_activation_functions.png
│   ├── heatmap_of_all_error_data.png
│   ├── correct_prediction_data.png
│   ├── linear_distribution_goodness_of_fit.png
│   ├── relu_distribution_goodness_of_fit.png
│   ├── sigmoid_distribution_goodness_of_fit.png
│   ├── tanh_distribution_goodness_of_fit.png
├── Keras_Model_Development/
│   ├── rename_keras_files.ps1
│   ├── rename_keras_files_script.ps1
│   ├── error_analysis_report_95.xlsx
│   ├── finalize_keras_model_training.py
│   ├── generate_non_compliant_data.py
│   ├── k95_prediction_report_update_control.xlsx
├── Statistical_Analysis_Tests/
│   ├── distribution_control.py
│   ├── 95_Confidence_Distribution_Test_Results_All_Sheets.xlsx
```

## Usage

### Data Generation

To generate sample data, navigate to the `Data_Generation_Scripts` directory and run the `generator_95_percent.py` script. This script will create an Excel file containing the generated data.

```bash
python generator_95_percent.py
```

### Visualizations

The `Visualization_Scripts` folder contains several scripts that generate various visualizations to analyze the generated data. For example, to plot fitness data, run the `fitness_plotting.py` script:

```bash
python fitness_plotting.py
```

### Keras Model Training

The `Keras_Model_Development` directory includes scripts for training Keras models and analyzing their performance. You can finalize model training using:

```bash
python finalize_keras_model_training.py
```

### Statistical Tests

In the `Statistical_Analysis_Tests` folder, you can perform distribution tests using the `distribution_control.py` script. This will help in validating the assumptions regarding the data distributions.

```bash
python distribution_control.py
```

## Scripts Overview

- **Data_Generation_Scripts**
  - `generator_95_percent.py`: Generates synthetic data based on predefined parameters.
  - `9595_example_last_update_control_95_.xls`: Example dataset for testing.

- **Visualization_Scripts**
  - `fitness_plotting.py`: Plots fitness data of the models.
  - `comprehensive_graphing.py`: Generates comprehensive graphs for data analysis.
  - Other utility scripts for plotting and data manipulation.

- **Keras_Model_Development**
  - `finalize_keras_model_training.py`: Script to finalize the training of Keras models.
  - `generate_non_compliant_data.py`: Generates data that do not comply with the standard distributions.

- **Statistical_Analysis_Tests**
  - `distribution_control.py`: Conducts distribution tests and generates results in an Excel file.

## Visualizations

The project includes several visualizations that illustrate the distribution of data related to different activation functions. Below are some examples:

![Heatmap of All Error Data](graphs/heatmap_of_all_error_data.png)

![Distribution of Non-Error Data by Activation Functions](graphs/distribution_of_non_error_data_by_activation_functions.png)

![Linear Distribution Goodness of Fit](graphs/linear_distribution_goodness_of_fit.png)

## Statistical Tests

The project incorporates the Kolmogorov-Smirnov test for validating the assumptions of normality in data distributions. The results are stored in the `95_Confidence_Distribution_Test_Results_All_Sheets.xlsx` file for further analysis.

```