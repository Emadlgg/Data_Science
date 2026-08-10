# Laboratorio 3 - Deep Learning: reconocimiento de señas ASL

Proyecto del curso **CC3084 - Data Science** de la Universidad del Valle de Guatemala.

## Integrantes

- Milton Polanco
- Osman de León

## Objetivo

El laboratorio compara modelos de aprendizaje automático y profundo para clasificar imágenes del alfabeto del Lenguaje de Señas Americano (ASL). Se trabajó con las 29 clases del conjunto: las letras A-Z y las categorías `del`, `nothing` y `space`.

## Dataset

Se utiliza [ASL Alphabet](https://www.kaggle.com/datasets/grassknoted/asl-alphabet), con 87,000 imágenes de entrenamiento balanceadas: 3,000 imágenes JPEG RGB de 200 x 200 píxeles por clase. La carpeta de prueba oficial contiene 28 imágenes adicionales.

El dataset no se guarda en Git por su tamaño. `src/download_dataset.py` comprueba si ya existe localmente y, si falta, descarga desde Google Drive una copia del archivo original de Kaggle. El enlace de Drive funciona como espejo para facilitar la reproducción del laboratorio; la fuente del conjunto sigue siendo Kaggle.

## Estructura

```text
Lab-DeepLearning/
├── dataset/                         # Se descarga al ejecutar; ignorado por Git
│   ├── asl_alphabet_train/          # 29 carpetas de entrenamiento
│   └── test/                        # 28 imágenes oficiales
├── notebooks/
│   └── Lab_DeepLearning.ipynb      # Análisis, modelos y resultados
├── own_images/
│   ├── Milton Polanco/              # Cinco fotografías propias
│   ├── Osman/                       # Cinco fotografías propias
│   └── README.md
├── src/
│   └── download_dataset.py         # Descarga y validación del dataset
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Emadlgg/Data_Science.git
cd Data_Science/Lab-DeepLearning
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Abra `notebooks/Lab_DeepLearning.ipynb` y ejecute todas las celdas en orden. La primera ejecución descargará y extraerá aproximadamente 1.1 GB si `dataset/` no existe. Las ejecuciones posteriores reutilizarán los archivos locales.

El notebook crea temporalmente `artifacts/models/` para guardar los modelos entrenados. Esa carpeta también está ignorada por Git porque se reconstruye al ejecutar el análisis completo.

## Metodología

- Análisis de balance, formato, resolución, variabilidad interna y clases visualmente similares.
- Submuestra estratificada de 500 imágenes por clase y división 70/15/15.
- Redimensionamiento a 64 x 64, normalización y procesamiento por lotes.
- Comparación de dos CNN, dos redes completamente conectadas y dos configuraciones de Random Forest.
- Reentrenamiento de las dos CNN con rotación, traslación, zoom y contraste.
- Selección por F1 macro de validación y análisis final en prueba.
- Evaluación externa con cinco fotografías de letras distintas por cada integrante.
- Discusión de cambio de dominio, accesibilidad, sesgo y limitaciones.

No se aplicó volteo horizontal durante el aumento de datos porque cambia la lateralidad de la seña. La validación y la prueba permanecieron sin transformaciones.

## Resultados

La CNN mejorada sin aumento de datos fue la mejor configuración:

| Modelo | F1 macro de validación | F1 macro de prueba |
|---|---:|---:|
| CNN mejorada | 0.9807 | 0.9800 |
| Random Forest sin límite de profundidad | 0.9613 | 0.9678 |
| Red completamente conectada regularizada | 0.3810 | 0.3866 |
| CNN base | 0.2043 | 0.2099 |

El aumento de datos no mejoró las CNN con el presupuesto de épocas utilizado. En las diez fotografías propias, el modelo acertó 3 de 10: 2 de 5 fotografías de Milton y 1 de 5 de Osman. Esta caída se analiza como cambio de dominio entre las imágenes controladas de Kaggle y fotografías tomadas con otras personas, cámaras, fondos y condiciones de iluminación.

El resultado corresponde a un prototipo de clasificación de señas estáticas. No debe interpretarse como un traductor completo ni como un sistema listo para uso de accesibilidad.
