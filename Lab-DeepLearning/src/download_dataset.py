"""
download_dataset.py

Descarga automáticamente una copia del dataset ASL Alphabet desde Google
Drive si aún no existe en la carpeta dataset/.

Fuente original:
https://www.kaggle.com/datasets/grassknoted/asl-alphabet

Uso
-----
from src.download_dataset import ensure_dataset

dataset_path = ensure_dataset()
"""

from pathlib import Path
import zipfile
import gdown


# CONFIGURACIÓN

# ID de la copia de dataset.zip almacenada en Google Drive
FILE_ID = "1HphszWjr2tD2asupYP0zpJZuolie7Ink"

# URL de descarga
URL = f"https://drive.google.com/uc?id={FILE_ID}"

# Carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carpeta donde quedará el dataset
DATASET_DIR = BASE_DIR / "dataset"

# El ZIP usado por el proyecto conserva el nombre original de Kaggle
# (asl_alphabet_train), mientras que algunas copias antiguas lo renombraron
# a "train". Se aceptan ambas variantes para que el proyecto sea reproducible.
TRAIN_DIR_NAMES = ("train", "asl_alphabet_train")

# Archivo ZIP temporal
ZIP_PATH = BASE_DIR / "dataset.zip"


# DESCARGAR DATASET

def download_dataset():
    """
    Descarga el dataset desde Google Drive y lo descomprime.
    """

    print("Descargando dataset desde Google Drive...")

    downloaded_path = gdown.download(
        url=URL,
        output=str(ZIP_PATH),
        quiet=False
    )

    if downloaded_path is None or not ZIP_PATH.is_file():
        raise RuntimeError(
            "No se pudo descargar el dataset. Verifique el acceso al archivo "
            "de Google Drive o descárguelo desde la fuente original de Kaggle."
        )

    print("Extrayendo dataset...")

    try:
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(BASE_DIR)
    finally:
        # El ZIP es temporal y no forma parte de la entrega.
        if ZIP_PATH.exists():
            ZIP_PATH.unlink()

    print("Dataset descargado correctamente.\n")


# VERIFICAR DATASET

def dataset_exists():
    """
    Verifica que el dataset exista y tenga la estructura esperada.
    """

    train = next(
        (DATASET_DIR / name for name in TRAIN_DIR_NAMES
         if (DATASET_DIR / name).exists()),
        None
    )
    test = DATASET_DIR / "test"

    return (
        DATASET_DIR.exists()
        and train is not None
        and test.exists()
        and any(train.iterdir())
        and any(test.iterdir())
    )


# ASEGURAR DATASET

def ensure_dataset():
    """
    Si el dataset ya existe, lo utiliza.
    En caso contrario, lo descarga automáticamente.
    """

    if dataset_exists():
        print("Dataset encontrado.\n")
        return DATASET_DIR

    print("Dataset no encontrado.\n")

    download_dataset()

    # Verificar nuevamente
    if not dataset_exists():
        raise FileNotFoundError(
            "El dataset no se encontró después de la descarga."
        )

    return DATASET_DIR


# EJECUCIÓN DIRECTA

if __name__ == "__main__":
    ensure_dataset()
