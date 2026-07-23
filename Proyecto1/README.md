# Proyecto 1 - Obtención y Limpieza de Datos

## Universidad del Valle de Guatemala
**Facultad de Ingeniería**  
**Departamento de Ciencias de la Computación**  
**CC3084 – Data Science**

---

## Descripción

Este proyecto implementa un proceso completamente reproducible para la obtención, integración, análisis y limpieza de los datos de establecimientos educativos de Guatemala que ofrecen el nivel **Diversificado**.

El objetivo es transformar un conjunto de datos crudos en un conjunto limpio, consistente y listo para análisis, documentando cada una de las transformaciones realizadas.

El proyecto fue desarrollado siguiendo las especificaciones del **Proyecto 1 – Obtención y Limpieza de Datos** del curso CC3084. :contentReference[oaicite:1]{index=1}

---

# Objetivos

- Automatizar la descarga de datos desde el portal del Ministerio de Educación.
- Integrar la información de todos los departamentos.
- Realizar un diagnóstico del estado inicial del conjunto de datos.
- Detectar problemas de calidad.
- Diseñar e implementar un plan de limpieza.
- Validar automáticamente la calidad del conjunto limpio.
- Generar un dataset final listo para análisis.
- Elaborar el libro de códigos.

---

# Estructura del proyecto

```
Proyecto/
│
├── Proyecto1.ipynb
├── data/
│   ├── raw/
│   ├── csv/
│   └── clean/
│
├── outputs/
│   ├── registro_transformaciones.csv
│   ├── reporte_formatos.csv
│   ├── comparacion_calidad.csv
│   ├── posibles_duplicados.csv
│   └── libro_codigos.csv
│
├── README.md
└── requirements.txt
```

---

# Flujo de trabajo

El notebook está organizado en diez etapas principales.

## 1. Obtención de datos

Se automatiza la descarga de los establecimientos educativos utilizando Selenium.

- Navegación automática del portal del MINEDUC.
- Descarga por departamento.
- Renombrado automático de archivos.

---

## 2. Conversión y unión

Se leen todos los archivos descargados.

Posteriormente:

- se convierten a DataFrames;
- se unifican en un único conjunto de datos;
- se exporta un CSV con los datos crudos.

---

## 3. Diagnóstico del conjunto

Se realiza un análisis exploratorio del estado inicial.

Se incluyen:

- número de registros;
- número de variables;
- tipos de datos;
- valores faltantes;
- valores únicos;
- duplicados exactos;
- formatos inconsistentes;
- problemas potenciales de calidad.

---

## 4. Plan de limpieza

Antes de modificar el conjunto de datos se documentan:

- problemas encontrados;
- transformación propuesta;
- justificación;
- riesgos asociados.

---

## 5. Limpieza de datos

Se aplican múltiples procesos de limpieza.

Entre ellos:

- eliminación de espacios innecesarios;
- normalización de texto;
- conversión de mayúsculas;
- tratamiento de valores faltantes;
- estandarización de teléfonos;
- validación de departamentos y municipios;
- detección de duplicados exactos;
- detección de duplicados parciales utilizando **RapidFuzz**;
- verificación de consistencia entre variables.

Todas las modificaciones quedan registradas para garantizar la reproducibilidad.

---

## 6. Registro de transformaciones

Cada transformación realizada queda documentada indicando:

- variable;
- problema detectado;
- transformación aplicada;
- registros afectados;
- justificación.

---

## 7. Validación del conjunto limpio

Se ejecutan pruebas automáticas para verificar que:

- no existan duplicados exactos;
- los tipos de datos sean correctos;
- no existan espacios al inicio o final;
- los teléfonos tengan formato consistente;
- departamentos y municipios pertenezcan al catálogo oficial;
- no existan categorías inconsistentes.

---

## 8. Informe de calidad

Se compara el estado del conjunto de datos antes y después de la limpieza.

Se evalúan métricas como:

- registros;
- variables;
- valores faltantes;
- duplicados;
- categorías inconsistentes;
- errores corregidos.

---

## 9. Generación del conjunto limpio

Se genera un único archivo CSV con:

- estructura uniforme;
- nombres descriptivos;
- tipos de datos adecuados;
- información validada.

---

## 10. Libro de códigos

Se documenta cada variable indicando:

- descripción;
- tipo de dato;
- dominio;
- tratamiento aplicado;
- variables derivadas;
- fuente;
- versión del conjunto.

---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Selenium
- RapidFuzz
- Unidecode
- BeautifulSoup
- lxml
- Jupyter Notebook

---

# Requisitos

Instalar las dependencias con:

```bash
pip install pandas numpy selenium rapidfuzz unidecode beautifulsoup4 lxml html5lib openpyxl
```

---

# Ejecución

Abrir el notebook:

```bash
jupyter notebook Proyecto1.ipynb
```

Ejecutar todas las celdas en orden.

---

# Resultados generados

El proyecto produce, entre otros:

- Datos crudos en CSV.
- Dataset limpio final.
- Registro de transformaciones.
- Reporte de formatos.
- Comparación antes/después.
- Posibles duplicados.
- Libro de códigos.

---

# Fuente de datos

Ministerio de Educación de Guatemala (MINEDUC)

Portal de búsqueda de establecimientos educativos.

---

# Reproducibilidad

Todo el flujo del proyecto se encuentra automatizado y documentado en el notebook, permitiendo reproducir completamente la obtención, limpieza y validación del conjunto de datos.

---

# Autores

Proyecto desarrollado para el curso:

**CC3084 – Data Science**

Universidad del Valle de Guatemala.