# Detección de SMS spam con CNN

**Iris Giselle Balderas Arreola · A01752895**  
Implementación individual de deep learning con Keras y TensorFlow.

Se implementó una red convolucional para clasificar mensajes SMS en inglés como `ham` (legítimo) o `spam`. Se eligió un dataset real de Kaggle y una arquitectura pequeña para evitar descargas y entrenamientos largos.

## Archivos principales

| Archivo | Contenido |
| --- | --- |
| `reporte_spam.ipynb` | Reporte completo con todas las celdas ejecutadas, gráficas y conclusiones |
| `modelos/modelo_final.keras` | Modelo completo entrenado: preprocesamiento, arquitectura y pesos |
| `modelos/inicial.keras` | CNN inicial entrenada, entrada de tokens |
| `modelos/ajustado.keras` | CNN ajustada entrenada, entrada de tokens |
| `predecir.py` | Predicción por consola o desde una función |
| `datos/spam.csv` | CSV original descargado de Kaggle |
| `datos/FUENTE.md` | Fuente, atribución y licencia del dataset |
| `resultados/` | Métricas, curvas, particiones y predicciones de prueba |
| `requirements.txt` | Dependencias para ejecutar el proyecto |

## Datos y separación

Se utilizó [SMS Spam Collection Dataset, de UCI ML en Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). El CSV descargado contiene 5,572 mensajes. Se retiraron vacíos y duplicados normalizados, incluyendo grupos con etiquetas contradictorias si existían; quedaron 5,129 mensajes.

Se separaron 3,590 para entrenamiento, 769 para validación y 770 para prueba, usando estratificación y semilla 42. El vocabulario se aprendió únicamente con entrenamiento. El dataset no apareció entre los ejemplos de las diapositivas compartidas; se debe confirmar que tampoco se utilizó en prácticas no incluidas en ese material.

## Arquitectura y ajuste

Se empleó `TextVectorization` (máximo 6,000 tokens, longitud 80), `Embedding(32)`, `Conv1D(32, 3, ReLU)`, `GlobalMaxPooling1D` y una salida sigmoid. Se entrenó con Adam (0.001), entropía cruzada binaria y lotes de 64.

La CNN inicial se entrenó por 8 épocas. Se añadió `SpatialDropout1D(0.2)` y `Dropout(0.4)` en la segunda configuración, con un máximo de 12 épocas y early stopping (paciencia 3). Se conservaron pesos por pérdida de validación y se eligió la configuración final por F1 de validación, con umbral fijo 0.5. Early stopping no detuvo anticipadamente esta ejecución: se completaron las 12 épocas. El ajuste cambia regularización y duración, por lo que no permite aislar sus efectos individuales.

## Resultados medidos

| Conjunto y modelo | Accuracy | F1 de spam |
| --- | ---: | ---: |
| Validación, inicial | 97.01% | 0.8715 |
| Validación, ajustado | 97.53% | 0.8950 |
| Prueba, modelo seleccionado (ajustado) | 98.18% | 0.9239 |

En prueba se obtuvo precisión de spam de 95.51%, recall de 89.47% y average precision de 0.9557. El notebook muestra la matriz de confusión, las curvas y ejemplos de errores. Prueba se utilizó después de seleccionar el modelo con validación.

La mejora es compatible con el efecto conjunto de regularización y mayor entrenamiento. Se redujo la pérdida de validación, aunque se mantuvo una brecha frente a entrenamiento. Una sola ejecución no prueba que esa mejora ocurra con cualquier partición.

## Ejecutar predicciones sin entrenar

Se recomienda Python 3.11 o 3.12. La entrega se verificó con Python 3.12 y TensorFlow 2.20 en CPU.

Desde la carpeta del proyecto, crear un entorno:

```bash
python -m venv .venv
```

Activación en Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activación en macOS o Linux:

```bash
source .venv/bin/activate
```

Instalar y probar:

```bash
python -m pip install -r requirements.txt
python predecir.py "Congratulations! You won a free prize. Call now to claim your cash reward!"
python predecir.py "Hey, are we still meeting for lunch tomorrow?"
```

Se devuelve un diccionario con `clase` y `puntuacion_spam`. No se necesita volver a entrenar. La primera instalación de TensorFlow descarga sus dependencias y tarda más que abrir el reporte o entrenar esta red pequeña.

También se puede llamar la función:

```python
from predecir import predecir_mensaje
print(predecir_mensaje("Please send me the notes after class."))
```

## Consultar o reproducir el notebook

Se puede leer directamente en GitHub con sus resultados guardados. Para volver a ejecutar, abrir `reporte_spam.ipynb` en VS Code con la extensión Jupyter, elegir el entorno `.venv` y ejecutar todas las celdas en orden. Se debe usar la carpeta del proyecto como directorio de trabajo. El CSV ya está incluido; si se elimina, el notebook intenta descargarlo de Kaggle y explica la fuente. Si Kaggle exige autenticación o cambia su API, descargar `spam.csv` manualmente desde su página y colocarlo en `datos/`.

El modelo completo ocupa aproximadamente 2.4 MB. No usa GPU ni embeddings preentrenados. Los tiempos medidos del entrenamiento están en `resultados/comparacion_validacion.csv`; dependen del equipo. Volver a entrenar reemplaza los archivos de modelos y resultados.

## Limitaciones y mejoras

Se evaluaron SMS históricos en inglés; no se comprobó el desempeño en español, con fraude reciente o con otros tipos de mensajes. La puntuación no es una probabilidad calibrada de fraude. Pueden quedar plantillas similares entre particiones. Sería útil evaluar varias semillas, separar por plantillas, recopilar mensajes actuales y comparar con TF-IDF más un modelo lineal.

## Referencias

- Almeida, T. y Hidalgo, J. (2011). *SMS Spam Collection*. [UCI](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). [DOI](https://doi.org/10.24432/C5CC84). Licencia CC BY 4.0 según la fuente original.
- [Kaggle: uciml/sms-spam-collection-dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).
- [Keras: clasificación de texto desde cero con Conv1D](https://keras.io/examples/nlp/text_classification_from_scratch/).
- Diapositivas compartidas: *Diagnosing Deep Neural Networks*, *Convolutional Neural Networks* y *Fully Connected Neural Networks*.
