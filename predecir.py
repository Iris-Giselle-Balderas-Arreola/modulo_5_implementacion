"""Se realizó una función para clasificar SMS nuevos en inglés."""
import os
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
import argparse
from pathlib import Path
import tensorflow as tf

BASE = Path(__file__).resolve().parent

def predecir_mensaje(mensaje, modelo=None):
    """Se devuelve la clase y la puntuación de spam del modelo."""
    if not isinstance(mensaje, str) or not mensaje.strip():
        raise ValueError("Se debe proporcionar un mensaje con texto.")
    if modelo is None:
        modelo = tf.keras.models.load_model(BASE / "modelos/modelo_final.keras")
    probabilidad = float(modelo(tf.constant([mensaje]), training=False).numpy()[0, 0])
    return {"clase": "spam" if probabilidad >= 0.5 else "ham",
            "puntuacion_spam": round(probabilidad, 4)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Se clasifica un SMS en inglés: ham o spam.")
    parser.add_argument("mensaje", help="Mensaje entre comillas")
    args = parser.parse_args()
    print(predecir_mensaje(args.mensaje))
