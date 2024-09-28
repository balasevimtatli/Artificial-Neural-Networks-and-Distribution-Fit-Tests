# Set the folder path to your actual project directory
$folderPath = "C:\Users\yigit\Documents\GitHub\Artificial Neural Networks and Distribution Fit Tests\graphs"

# Define the specific changes you want to make
$renameMap = @{
    'doğru tahmin veriler.png' = 'correct_prediction_data.png';
    'hatasız verilerin grafiği-aktivasyonfonksiyonlarınagöredağılımlar.png' = 'distribution_of_non_error_data_by_activation_functions.png';
    'hatalı verilerin grafiği-aktivasyonfonksiyonlarınagöredağılımlar.png' = 'distribution_of_error_data_by_activation_functions.png';
    'tanh-dağılımlarınuygunlukdurum.png' = 'tanh_distribution_goodness_of_fit.png';
    'sigmoid-dağılımlarınuygunlukdurum.png' = 'sigmoid_distribution_goodness_of_fit.png';
    'relu-dağılımlarınuygunlukdurum.png' = 'relu_distribution_goodness_of_fit.png';
    'linear-dağılımlarınuygunlukdurum.png' = 'linear_distribution_goodness_of_fit.png';
}

# Function to rename files
function Rename-Items {
    param (
        [string]$path
    )

    # Get all files in the directory
    Get-ChildItem -Path $path -File | ForEach-Object {
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

# Call the function and provide the graphs folder path
Rename-Items -path $folderPath
