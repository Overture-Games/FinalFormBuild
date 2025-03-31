import itertools
import os
from pydub import AudioSegment

# Definir los instrumentos y sus opciones (1-5)
instruments = ["Arpegio", "Bass", "Beat", "Layer", "Lead", "Percussion", "Strings", "Synth"]
options = range(1, 6)

# Definir rutas
input_folder = "assets/PartA"
output_folder = "assets/MixA"

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Generar todas las combinaciones posibles
combinations = itertools.product(options, repeat=len(instruments))

for combo in combinations:
    combo_str = "".join(map(str, combo))  # Convertir la combinación a string (ej: "24244234")
    mix = None  # Mezcla inicial vacía

    for instrument, option in zip(instruments, combo):
        file_path = f"{input_folder}/{instrument}/{instrument}{option}.wav"

        if os.path.exists(file_path):
            audio = AudioSegment.from_wav(file_path)

            if mix is None:
                mix = audio  # Primera pista
            else:
                mix = mix.overlay(audio)  # Superponer pista
        else:
            print(f"Archivo no encontrado: {file_path}")

    if mix:
        output_path = f"{output_folder}/{combo_str}.wav"
        mix.export(output_path, format="wav")
        print(f"Exportado: {output_path}")
