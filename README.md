# Artificial Neural Networks and Distribution Fit Tests

This repository contains a comprehensive study on Artificial Neural Networks (ANNs) and Distribution Fit Tests, focusing on various activation functions and their impacts on prediction accuracy and error distribution.

## Project Structure

```
Artificial Neural Networks and Distribution Fit Tests/
├── generator/
│   ├── 9595_example_last_update_control_95_.xls
│   └── generator_95_percent.py
├── graphs/
│   ├── images/
│   │   ├── distribution_of_non_error_data_by_activation_functions.png
│   │   ├── heatmap_of_all_error_data.png
│   │   ├── linear_distribution_goodness_of_fit.png
│   │   ├── relu_distribution_goodness_of_fit.png
│   │   ├── sigmoid_distribution_goodness_of_fit.png
│   │   ├── tanh_distribution_goodness_of_fit.png
│   │   ├── correct_prediction_data.png
│   │   └── distribution_of_error_data_by_activation_functions.png
│   ├── data/
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

## Project Overview

This project explores the behavior of Artificial Neural Networks (ANNs) with different activation functions and analyzes the distribution of prediction errors using various statistical tests.

### Key Components

1. **Data Generation**: 
   - Located in the `generator/` folder
   - Uses `generator_95_percent.py` to create datasets
   - Example output: `9595_example_last_update_control_95_.xls`

2. **Neural Network Models**: 
   - Implemented using Keras (see `keras/` folder)
   - `finalize_keras_model_training.py`: Main script for training models
   - `generate_non_compliant_data.py`: Creates data for testing model robustness

3. **Error Analysis and Visualization**: 
   - Found in the `graphs/` folder
   - Various Python scripts for data processing and visualization
   - Outputs include distribution plots, heatmaps, and goodness-of-fit visualizations

4. **Distribution Fit Tests**: 
   - Kolmogorov-Smirnov tests implemented in `kolmogorov-smirnov/distribution_control.py`
   - Results compiled in `95_Confidence_Distribution_Test_Results_All_Sheets.xlsx`

## Key Findings

### Activation Function Performance

![Distribution of Non-Error Data by Activation Functions](graphs/distribution_of_non_error_data_by_activation_functions.png)

This graph shows the distribution of correctly predicted data across different activation functions. It provides insights into which activation functions perform better for our specific problem.

### Error Distribution Analysis

![Heatmap of All Error Data](graphs/heatmap_of_all_error_data.png)

The heatmap visualizes the distribution of errors across different scenarios, helping identify patterns or clusters of errors.

### Goodness of Fit for Different Activation Functions

1. ![Linear Distribution Goodness of Fit](graphs/linear_distribution_goodness_of_fit.png)
2. ![ReLU Distribution Goodness of Fit](graphs/relu_distribution_goodness_of_fit.png)
3. ![Sigmoid Distribution Goodness of Fit](graphs/sigmoid_distribution_goodness_of_fit.png)
4. ![Tanh Distribution Goodness of Fit](graphs/tanh_distribution_goodness_of_fit.png)

These graphs demonstrate how well the error distributions for each activation function fit to theoretical probability distributions.

## Usage

1. **Data Generation**: 
   Run `generator_95_percent.py` in the `generator/` folder to create datasets.

2. **Model Training**: 
   Execute `finalize_keras_model_training.py` in the `keras/` folder to train the neural network models.

3. **Visualization and Analysis**: 
   Use scripts in the `graphs/` folder to generate visualizations and perform data analysis.

4. **Distribution Tests**: 
   Run `distribution_control.py` in the `kolmogorov-smirnov/` folder to perform distribution fit tests.

## Requirements

- Python 3.x
- TensorFlow/Keras
- Numpy
- Pandas
- Matplotlib
- SciPy

## Contributing

Contributions to this project are welcome. Please ensure to update tests as appropriate and adhere to the existing coding style.

## License

[Specify your license here]

## Contact

[Your contact information or link to issues page]