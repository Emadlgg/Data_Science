# Laboratorio 5 - Minería de textos y análisis de sentimiento

**Curso:** CC3084 - Data Science  
**Integrantes:** Osman de León y Milton Polanco

Este laboratorio clasifica tweets como desastre real o no desastre usando el conjunto *Natural Language Processing with Disaster Tweets* de Kaggle.

**Repositorio:** [Lab-MineriayAnalisis](https://github.com/Emadlgg/Data_Science/tree/main/Lab-MineriayAnalisis)

## Archivos principales

- `notebooks/Laboratorio5.ipynb`: análisis completo y ejecutado, continuado a partir del avance.
- `reporte/Laboratorio5_informe.pdf`: informe final.
- `reporte/figuras/`: figuras generadas por el notebook.
- `reporte/train_con_sentimiento.csv`: datos de entrenamiento con puntajes de VADER.
- `data/`: archivos originales de Kaggle.

## Resultado principal

El modelo seleccionado fue regresión logística con TF-IDF de unigramas y bigramas. En el 20% reservado obtuvo 82.34% de exactitud y F1 de 0.7822. Los tweets de desastre real fueron más negativos en promedio, pero agregar la variable de negatividad redujo F1 de 0.7822 a 0.7795.

## Reproducción

Desde la carpeta del laboratorio:

```powershell
python -m pip install -r requirements.txt
```

La semilla usada es 42 y la partición de prueba es estratificada.
