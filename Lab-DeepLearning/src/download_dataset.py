"""
download_dataset.py

Descarga automáticamente el dataset desde Google Drive
si aún no existe en la carpeta data/dataset.

Uso
-----
from src.download_dataset import ensure_dataset

dataset_path = ensure_dataset()
"""

from pathlib import Path
import zipfile

import gdown


# ======================================================
# CONFIGURACIÓN
# ======================================================

URL = "https://drive.google.com/file/d/1HphszWjr2tD2asupYP0zpJZuolie7Ink/view?usp=sharing"

# Carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carpeta data/
DATA_DIR = BASE_DIR / "data"

# Ruta donde quedará el dataset
DATASET_DIR = DATA_DIR / "dataset"

# Archivo temporal
ZIP_PATH = DATA_DIR / "dataset.zip"


# ======================================================
# DESCARGA
# ======================================================

def download_dataset():
    """
    Descarga el dataset desde Google Drive y lo descomprime.
    """

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Descargando dataset desde Google Drive...")

    gdown.download(
        url=URL,
        output=str(ZIP_PATH),
        quiet=False,
        fuzzy=True
    )

    print("Extrayendo dataset...")

    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(DATA_DIR)

    # Elimina el ZIP para no ocupar espacio
    ZIP_PATH.unlink()

    print("✅ Dataset descargado correctamente.\n")


# ======================================================
# VERIFICACIÓN
# ======================================================

def dataset_exists():
    """
    Verifica que el dataset ya exista.
    """

    train = DATASET_DIR / "train"
    test = DATASET_DIR / "test"

    return (
        train.exists()
        and test.exists()
        and any(train.iterdir())
        and any(test.iterdir())
    )


def ensure_dataset():
    """
    Garantiza que el dataset exista.

    Si no existe, lo descarga automáticamente.
    """

    if dataset_exists():

        print("✅ Dataset encontrado.\n")

        return DATASET_DIR

    print("⚠️ Dataset no encontrado.\n")

    download_dataset()

    return DATASET_DIR


# ======================================================
# EJECUCIÓN DIRECTA
# ======================================================

if __name__ == "__main__":

    ensure_dataset()