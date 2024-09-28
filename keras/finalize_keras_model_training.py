import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Excel dosyasını oku
df = pd.read_excel("C:/Tez/9595_example_last_update_control_95_.xls", header=None)

# Giriş ve çıkış değerlerini belirle
X = df.iloc[:, :10].values
y = pd.concat([df.iloc[:, 15:32]], axis=1).values

# Aktivasyon fonksiyonları
activation_functions = ['relu', 'sigmoid', 'tanh', 'linear']

# Sonuçları yazmak için Excel dosyası oluştur
writer = pd.ExcelWriter("995k95_prediction_last_update_control_95.xls", engine='xlsxwriter')

# Her aktivasyon fonksiyonu için model oluştur
for activation_func in activation_functions:
    model = Sequential()
    model.add(Dense(64, input_dim=X.shape[1], activation=activation_func))
    model.add(Dense(32, activation=activation_func))
    model.add(Dense(16, activation='softmax'))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, y, epochs=200, batch_size=32, verbose=False)

    # Tahminleri al
    y_pred = model.predict(X)
    df_pred = pd.DataFrame(y_pred, columns=[f'Prediction_{i+1}' for i in range(16)])

    # Tahminleri df'ye ekle
    df[df_pred.columns] = df_pred

    # En yüksek tahmini bul ve 1, diğerlerini 0 yap
    max_columns = df_pred.apply(pd.to_numeric, errors='coerce').idxmax(axis=1)  # Tüm değerleri sayıya çevir

    for i in range(1, 17):
        column_name = f'New_Prediction_{i-1}'
        # Maksimum tahminin olduğu sütuna 1, diğerlerine 0 atama
        df[column_name] = np.where(max_columns == f'Prediction_{i}', 1, 0)

    # Tahminleri her aktivasyon fonksiyonu için ayrı sayfaya yazdır
    df.to_excel(writer, sheet_name=activation_func, index=False)

writer.close()
