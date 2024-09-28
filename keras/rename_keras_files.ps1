# Set the folder path to your actual project directory
$folderPath = "C:\Users\yigit\Documents\GitHub\Artificial Neural Networks and Distribution Fit Tests\keras"

# Define the specific changes you want to make
$renameMap = @{
    'completeeras_last95.py' = 'finalize_keras_model_training.py';
    'rename_keras_files.ps1' = 'rename_keras_files_script.ps1'; # Optional: more descriptive name
    '95_error.xlsx' = 'error_analysis_report_95.xlsx'; # More descriptive
    'generate_non_compliant_data_95.py' = 'generate_non_compliant_data.py'; # If not needed
    'k95_prediction_report_last_update_control_95.xlsx' = 'k95_prediction_report_update_control.xlsx'; # Shorter
}

# Function to rename files
function Rename-Items {
    param (
        [string]$path
    )

    # Get all files in the directory
    Get-ChildItem -Path $path | ForEach-Object {
        $item = $_
        $newName = $item.Name
        
        # Check if the current file name matches any in the rename map
        if ($renameMap.ContainsKey($newName)) {
            $newName = $renameMap[$newName]
            $newFullPath = Join-Path $item.DirectoryName $newName
            
            # Rename the item only if the name has changed
            if ($newName -ne $item.Name) {
                try {
                    Rename-Item -Path $item.FullName -NewName $newFullPath -Force
                    Write-Host "Renamed: $($item.Name) -> $newName"
                } catch {
                    Write-Host "Failed to rename: $($item.Name)"
                }
            }
        }
    }
}

# Call the function and provide the keras folder path
Rename-Items -path $folderPath
