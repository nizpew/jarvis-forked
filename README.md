# J.A.R.V.I.S (Forked & Modified)

**Aviso:** Este projeto é baseado no [repositório original do J.A.R.V.I.S](https://github.com/codewithbro95/J.A.R.V.I.S).  
Este fork está hospedado em: [https://github.com/nizpew/jarvis-forked](https://github.com/nizpew/jarvis-forked)

Este fork contém ajustes para rodar localmente, com TTS offline usando Kokoro, integração opcional de Whisper, e correções em OllamaNLP para evitar erros caso certas variáveis não estejam definidas.

---



Requerimentos: 
RAM: ~3.3–3.5 GB
Disco:  Total aproximado: 4,5–5,7 GB

---

## Instalação

Recomenda-se criar um **virtual environment** para instalar todas as dependências.  

### Passos

1. Clonar o repositório:

```bash


git clone https://github.com/nizpew/jarvis-forked.git
cd jarvis-forked

  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin

  sudo apt-get install portaudio19 ; wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx\nwget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json

chmod +x wizard.sh
./wizard.sh
```

3. Ativar o ambiente virtual:

```bash
source venv/bin/activate
```











---

## Modificações feitas no código original

1. **Remoção do ElevenLabs:** substituído pelo Kokoro local para TTS.
2. **Removida integração com lâmpadas Tapo:** o código foi ajustado para evitar erros ao não ter lâmpadas.
3. **Ajuste do OllamaNLP:** adicionado fallback caso `JARVIS_MODEL` não esteja definido, evitando erro `model is required`.
4. **Correção do fluxo do Interlocus:** garantindo que a síntese de voz com Kokoro use uma voz válida do arquivo `voices-v1.0.bin`.
5. **Dependências de pacotes atualizadas** para rodar em Python 3.10, com remoção de módulos obsoletos.

---

## Ferramentas e Modelos Utilizados

* **Kokoro (TTS local)**: Modelo ONNX para síntese de voz.

  * Arquivo principal: `kokoro-v0_19.onnx`
  * Arquivo de vozes: `voices-v1.0.bin`

* **Vibranium Vision**: Módulo de visão computacional que usa OpenCV para capturar e descrever imagens.

* **Ollama**: Modelo de NLP para processar comandos e gerar respostas inteligentes.

* **Whisper (opcional)**: Modelo de transcrição de áudio para texto.

* **Bibliotecas Python**: ver seção Dependências abaixo.

---

## Dependências (com versões recomendadas)


WIZARD.SH já faz tudo


```text
aiohttp==3.8.4
numpy==1.24.5
opencv-python==4.8.1.78
scipy==1.11.2
webrtcvad==2.0.10
kokoro-onnx==0.19.0
python-dotenv==1.0.1
ollama==1.0.0
```

1. Ativar o venv:

```bash
source venv/bin/activate
sudo chmod +x wizard.sh ; ./wizard.sh
ollama serve &

```

2. Rodar o J.A.R.V.I.S:

```bash
python main.py
#agora fala alguma coisa, aceita apenas inglês por enquanto.
```

3. Para utilizar TTS offline ou NLP, garanta que os arquivos de modelo estejam na pasta `models`.

---

