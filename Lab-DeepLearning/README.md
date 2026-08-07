# Laboratorio 3 - Deep Learning: Reconocimiento de Lenguaje de Señas (ASL)

Proyecto desarrollado para el curso **CC3084 - Data Science** de la Universidad del Valle de Guatemala.

El objetivo del laboratorio es desarrollar y evaluar diferentes modelos de Machine Learning y Deep Learning capaces de clasificar imágenes correspondientes a letras del alfabeto del **Lenguaje de Señas Americano (ASL)**.

## Integrantes

- Milton Polanco
- Osman de León

## Dataset

Se utiliza el dataset **ASL Alphabet**, compuesto por aproximadamente **87,000 imágenes** distribuidas en **29 clases**:

- 26 letras del alfabeto (A-Z).
- `space`
- `del`
- `nothing`

Las imágenes originales tienen una resolución de **200 × 200 píxeles** y se encuentran en formato JPEG y espacio de color RGB.

El dataset no se almacena directamente en el repositorio debido a su tamaño. El proyecto incluye un script que verifica si el dataset está disponible localmente y, en caso contrario, lo descarga automáticamente desde Google Drive.

## Estructura del proyecto

```text
Lab-DeepLearning/
│
├── dataset/                       # Dataset descargado (ignorado por Git)
│   ├── train/
│   └── test/
│
├── notebooks/
│   └── Lab_DeepLearning.ipynb    # Notebook principal
│
├── src/
│   └── download_dataset.py       # Descarga automática del dataset
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Lab-DeepLearning
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

Abrir el archivo:

```text
notebooks/Lab_DeepLearning.ipynb
```

y ejecutar las celdas en orden.

La primera ejecución verifica automáticamente la existencia del dataset. Si la carpeta `dataset/` no se encuentra disponible, el archivo `src/download_dataset.py` descarga y extrae el dataset automáticamente.

Una vez descargado, las siguientes ejecuciones reutilizan los archivos locales y no realizan nuevamente la descarga.

## Análisis Exploratorio

Durante el análisis exploratorio se estudian diferentes características del conjunto de datos, incluyendo:

- Distribución de las clases.
- Cantidad de imágenes por clase.
- Resolución y formato de las imágenes.
- Variabilidad entre imágenes pertenecientes a una misma clase.
- Similitudes visuales entre diferentes letras.
- Estrategia de división de los datos.

## Preprocesamiento

Antes del entrenamiento se plantea aplicar las siguientes transformaciones:

- Redimensionamiento de imágenes de **200 × 200** a **64 × 64 píxeles**.
- Normalización de los valores de los píxeles al intervalo `[0,1]`.
- Procesamiento por lotes (*batching*).
- División de los datos en entrenamiento, validación y prueba.

## Modelos Propuestos

Durante el desarrollo del laboratorio se evaluarán diferentes enfoques:

1. **CNN Base**  
   Red Neuronal Convolucional utilizada como modelo inicial de referencia.

2. **CNN Mejorada**  
   Arquitectura convolucional de mayor profundidad y capacidad.

3. **Red Neuronal Fully Connected**  
   Modelo utilizado para comparar una red neuronal tradicional frente a las CNN.

4. **Modelo clásico de Machine Learning**  
   Se evaluará un algoritmo tradicional como SVM, Random Forest o KNN.

## Evaluación

Los modelos serán comparados utilizando métricas de clasificación como:

- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de confusión

Posteriormente, el modelo con mejor desempeño será evaluado utilizando imágenes de señas realizadas por los integrantes del grupo.

## Tecnologías

- Python
- Jupyter Notebook
- TensorFlow / Keras
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Pillow
- gdown

## Estado del proyecto

### Avance

- [x] Configuración del entorno
- [x] Descarga automática del dataset
- [x] Análisis exploratorio
- [x] Preprocesamiento inicial
- [x] Selección de modelos
- [x] Plan de procesamiento de imágenes

### Entrega final

- [ ] Entrenamiento de CNN Base
- [ ] Entrenamiento de CNN Mejorada
- [ ] Entrenamiento de red Fully Connected
- [ ] Entrenamiento de modelo clásico
- [ ] Image Augmentation
- [ ] Comparación de modelos
- [ ] Evaluación con imágenes propias
- [ ] Análisis de accesibilidad y sesgo
- [ ] Conclusiones finales