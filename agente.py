import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai

MODELO = "gemini-3.5-flash-lite"
BASE = Path(__file__).parent
INSTRUCCIONES = (BASE / "prompts" / "sistema.md").read_text(encoding="utf-8")

for archivo in sorted((BASE / "conocimientos").iterdir()):
    if archivo.is_file() and not archivo.name.startswith("."):
        contenido = archivo.read_text(encoding="utf-8")
        INSTRUCCIONES += f'\n<documento nombre="{archivo.name}">\n{contenido}\n</documento>\n'

load_dotenv()
client = genai.Client()

if len(sys.argv) < 2:
    sys.exit('Uso: python agente.py "tu pregunta"')

interaccion = client.interactions.create(
    model=MODELO,
    input=" ".join(sys.argv[1:]),
    system_instruction=INSTRUCCIONES,
)
print(interaccion.output_text)
