# Chatterbox: texto a voz en español

Proyecto del curso **IA Generativa** (Ingeniería de Sistemas, Universidad Santo Tomás, Tunja).

Convierte un texto en audio hablado en español usando **Chatterbox Multilingual TTS** de Resemble AI. El modelo corre en CPU, así que no hace falta tarjeta gráfica.

## Cómo funciona

1. Se carga `ChatterboxMultilingualTTS` (se descarga de Hugging Face la primera vez).
2. Se genera el audio del texto con `language_id="es"`.
3. El resultado se guarda como `audio.wav`.

El archivo `audio.wav` del repositorio es un ejemplo generado con el texto que trae el script.

## Tecnologías

- Python 3.12
- [uv](https://docs.astral.sh/uv/) para el entorno y las dependencias
- [chatterbox-tts](https://github.com/resemble-ai/chatterbox) 0.1.7+
- torchaudio (para guardar el `.wav`)

## Instalación y uso

Requisitos: Python 3.12 y uv instalados.

```bash
git clone https://github.com/Mans0089/chatterbox-ia-gen.git
cd chatterbox-ia-gen
uv sync
uv run src/text_to_speech_chatterbox/__init__.py
```

La primera ejecución descarga el modelo, así que tarda un poco. Al terminar aparece `audio.wav` en la carpeta del proyecto.

## Parámetros de generación

En `src/text_to_speech_chatterbox/__init__.py` puedes cambiar la variable `texto` y estos parámetros:

| Parámetro | Valor | Efecto |
|---|---|---|
| `exaggeration` | 0.7 | Expresividad o emoción de la voz |
| `cfg_weight` | 0.4 | Velocidad y ritmo del habla |
| `temperature` | 0.8 | Variabilidad del resultado |
| `repetition_penalty` | 1.2 | Penaliza repeticiones extrañas |
| `min_p` | 0.05 | Descarta opciones improbables al generar |
| `top_p` | 1.0 | Muestreo probabilístico (*nucleus sampling*) |

## Nota sobre Windows

Al inicio del script se eliminan las variables `CURL_CA_BUNDLE`, `REQUESTS_CA_BUNDLE` y `SSL_CERT_FILE` si apuntan a un archivo que no existe. En algunos equipos, la instalación de PostgreSQL deja una de ellas mal configurada, y eso impide descargar el modelo por HTTPS.

## Créditos

- Modelo: [Chatterbox](https://github.com/resemble-ai/chatterbox) de Resemble AI (licencia MIT).
- Autor: Manuel Santiago Martínez Sierra ([@Mans0089](https://github.com/Mans0089)).
