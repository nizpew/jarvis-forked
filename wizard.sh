#!/bin/bash

# =============================
# Wizard de instalação do J.A.R.V.I.S
# =============================

echo "Atualizando sistema..."
sudo apt update || echo "Falha no update"
sudo apt install -y software-properties-common wget curl git build-essential python3.10 python3.10-venv python3.10-dev portaudio19-dev || echo "Falha na instalação de pacotes do sistema"

# =============================
# Criar e ativar venv
# =============================
PYTHON=python3.10
VENV_DIR=venv

if [ -d "$VENV_DIR" ]; then
    echo "Removendo venv antigo..."
    rm -rf $VENV_DIR
fi

echo "Criando ambiente virtual..."
$PYTHON -m venv $VENV_DIR || echo "Falha ao criar venv"
echo "Ativando venv..."
source $VENV_DIR/bin/activate || echo "Falha ao ativar venv"

# =============================
# Atualizar pip, setuptools e wheel
# =============================
echo "Atualizando pip, setuptools e wheel..."
pip install --upgrade pip setuptools wheel || echo "Falha na atualização"

# =============================
# Instalar pacotes pip exatos
# =============================
echo "Instalando pacotes Python..."

pip install annotated-types==0.7.0 \
anyio==4.11.0 \
attrs==25.3.0 \
babel==2.17.0 \
beautifulsoup4==4.14.2 \
blinker==1.9.0 \
Brotli==1.1.0 \
certifi==2025.8.3 \
cffi==2.0.0 \
charset-normalizer==3.4.3 \
click==8.3.0 \
coloredlogs==15.0.1 \
colorlog==6.9.0 \
csvw==3.6.0 \
decorator==4.4.2 \
dlinfo==2.0.0 \
duckduckgo_search==5.3.1b1 \
elevenlabs==2.16.0 \
espeakng-loader==0.2.4 \
exceptiongroup==1.3.0 \
Flask==3.1.2 \
flatbuffers==25.9.23 \
googlesearch-python==1.3.0 \
h11==0.16.0 \
h2==4.3.0 \
hpack==4.1.0 \
httpcore==1.0.9 \
httpx==0.28.1 \
humanfriendly==10.0 \
hyperframe==6.1.0 \
idna==3.10 \
imageio==2.37.0 \
imageio-ffmpeg==0.6.0 \
isodate==0.7.2 \
itsdangerous==2.2.0 \
Jinja2==3.1.6 \
joblib==1.5.2 \
jsonschema==4.25.1 \
jsonschema-specifications==2025.9.1 \
kokoro-onnx==0.4.9 \
language-tags==1.2.0 \
MarkupSafe==3.0.3 \
MouseInfo==0.1.3 \
moviepy==1.0.3 \
mpmath==1.3.0 \
numpy==2.2.6 \
ollama==0.6.0 \
onnxruntime==1.23.0 \
opencv-python==4.12.0.88 \
packaging==25.0 \
phonemizer-fork==3.3.2 \
pillow==11.3.0 \
platformdirs==4.4.0 \
proglog==0.1.12 \
protobuf==6.32.1 \
psutil==7.1.0 \
PyAudio==0.2.14 \
PyAutoGUI==0.9.54 \
pycparser==2.23 \
pydantic==2.11.9 \
pydantic_core==2.33.2 \
PyGetWindow==0.0.9 \
PyMsgBox==2.0.1 \
PyOpenGL==3.1.10 \
PyOpenGL-accelerate==3.1.10 \
pyparsing==3.2.5 \
pyperclip==1.11.0 \
PyQt5==5.15.11 \
PyQt5-Qt5==5.15.17 \
PyQt5_sip==12.17.0 \
PyRect==0.2.0 \
PyScreeze==1.0.1 \
python-dateutil==2.9.0.post0 \
python-dotenv==1.0.1 \
python3-xlib==0.15 \
pyttsx3==2.99 \
pytweening==1.2.0 \
pywhatkit==5.4 \
pywhispercpp==1.3.3 \
referencing==0.36.2 \
regex==2025.9.18 \
requests==2.31.0 \
rfc3986==1.5.0 \
rpds-py==0.27.1 \
scipy==1.15.3 \
segments==2.3.0 \
setuptools==80.9.0 \
six==1.17.0 \
sniffio==1.3.1 \
socksio==1.0.0 \
sounddevice==0.5.2 \
soupsieve==2.8 \
SpeechRecognition==3.10.4 \
sympy==1.14.0 \
tapo==0.8.6 \
termcolor==3.1.0 \
tqdm==4.67.1 \
typing_extensions==4.15.0 \
typing-inspection==0.4.1 \
uritemplate==4.2.0 \
urllib3==2.5.0 \
webrtcvad==2.0.10 \
websockets==15.0.1 \
Werkzeug==3.1.3 \
wheel==0.45.1 \
wikipedia==1.4.0 || echo "Falha na instalação de algum pacote"

echo "Instalação concluída! Ambiente virtual pronto."
echo "Para ativar, rode: source $VENV_DIR/bin/activate"

