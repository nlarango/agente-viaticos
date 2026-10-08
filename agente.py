import sys

from dotenv import load_dotenv
from google import genai

MODELO = "gemini-3.8-flash"
INSTRUCCIONES = "Responde siempre en español, en máximo tres frases."

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
