
Recomenda-se criar um **virtual environment** para instalar todas as dependências.

---

## Modificações feitas no código original

1. **Remoção do ElevenLabs:** substituído pelo Kokoro local para TTS.
2. **Removida integração com lâmpadas Tapo:** o código foi ajustado para evitar erros ao não ter lâmpadas.
3. **Ajuste do OllamaNLP:** adicionado fallback caso `JARVIS_MODEL` não esteja definido, evitando erro `model is required`.
4. **Correção do fluxo do Interlocus:** garantindo que a síntese de voz com Kokoro use uma voz válida do arquivo `voices-v1.0.bin`.
5. **Dependências de pacotes atualizadas** para rodar em Python 3.10, com remoção de módulos obsoletos.

---

## Ferramentas e Modelos Utilizados

- **Kokoro (TTS local)**: Modelo ONNX para síntese de voz.  
  Arquivo principal: `kokoro-v0_19.onnx`  
  Arquivo de vozes: `voices-v1.0.bin`  

- **Vibranium Vision**: Módulo de visão computacional que usa OpenCV para capturar e descrever imagens.  

- **Ollama**: Modelo de NLP para processar comandos e gerar respostas inteligentes.  

- **Whisper (opcional)**: Modelo de transcrição de áudio para texto (já integrado ao Interlocus).  

- **Bibliotecas Python**: ver seção Dependências abaixo.

---

## Dependências (com versões recomendadas)

```text
aiohttp==3.8.4
numpy==1.24.5
opencv-python==4.8.1.78
scipy==1.11.2
webrtcvad==2.0.10
kokoro-onnx==0.19.0
python-dotenv==1.0.1
ollama==1.0.0

