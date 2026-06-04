#!/bin/bash

set -e

echo "========================================"
echo "Instalando Homebrew"
echo "========================================"

if ! command -v brew >/dev/null 2>&1; then
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

if [ -d "/opt/homebrew" ]; then
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
fi

echo "========================================"
echo "Instalando Python 3.10"
echo "========================================"

brew install python@3.10

echo 'export PATH="/opt/homebrew/opt/python@3.10/bin:$PATH"' >> ~/.zshrc

export PATH="/opt/homebrew/opt/python@3.10/bin:$PATH"

echo "========================================"
echo "Instalando Ollama"
echo "========================================"

brew install ollama

brew services start ollama || true

echo "========================================"
echo "Baixando modelo Llama 3.2"
echo "========================================"

ollama pull llama3.2

echo "========================================"
echo "Instalando PortAudio"
echo "========================================"

brew install portaudio

echo "========================================"
echo "Criando ambiente virtual"
echo "========================================"

rm -rf venv

python3.10 -m venv venv

source venv/bin/activate

echo "========================================"
echo "Atualizando pip"
echo "========================================"

python -m pip install --upgrade pip setuptools wheel

echo "========================================"
echo "Instalando Kokoro"
echo "========================================"

pip install kokoro-onnx

echo "========================================"
echo "Baixando modelos Kokoro"
echo "========================================"

curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx

curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json

echo ""
echo "========================================"
echo "INSTALAÇÃO CONCLUÍDA"
echo "========================================"
echo ""
echo "Para ativar o ambiente futuramente:"
echo ""
echo "source venv/bin/activate"
echo ""
echo "Para testar o Ollama:"
echo ""
echo "ollama run llama3.2"
echo ""
