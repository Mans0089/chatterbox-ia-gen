import os

# Windows tiene CURL_CA_BUNDLE apuntando a un certificado de PostgreSQL que no existe;
# se ignora aquí para que las descargas por HTTPS usen los certificados de certifi.
for _var in ("CURL_CA_BUNDLE", "REQUESTS_CA_BUNDLE", "SSL_CERT_FILE"):
    _ruta = os.environ.get(_var)
    if _ruta and not os.path.isfile(_ruta):
        os.environ.pop(_var)

import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

print("Cargando el modelo...")

modelo = ChatterboxMultilingualTTS.from_pretrained(
    device="cpu"
)

texto = "Messi es mejor que Cristiano Ronaldo, en ia generativa vamos a crear imagenes, texto, audio y si el compu aguanta, crearemos videos"

print("Generando el audio...")

audio = modelo.generate(
    texto,
    language_id="es",
    exaggeration=0.7, # Expresividad o emoción
    cfg_weight=0.4, # Afecta velocidad y ritmo
    temperature=0.8, # Controla variabilidad
    repetition_penalty=1.2, # Penaliza repeticiones extrañas
    min_p=0.05, # Filtra opciones improbables durante la generacion
    top_p=1.0 # Controla el muestreo probalistico
)

ta.save(
    "audio.wav",
    audio,
    modelo.sr
)

print("Audio generado")
