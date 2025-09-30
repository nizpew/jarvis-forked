import os
import asyncio
import onnxruntime as ort
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

class TextToSpeech:
    def __init__(self):
        # Caminho do modelo ONNX local
        self.model_path = os.getenv("KOKORO_MODEL_PATH", "kokoro-v0_19.onnx")
        self.session = ort.InferenceSession(self.model_path)
        print(f"Kokoro model loaded from {self.model_path}")

    async def speak(self, text: str):
        try:
            print("Saying:", text)

            # TODO: preprocess 'text' para vetor de tokens esperado pelo modelo Kokoro
            input_tokens = self.text_to_tokens(text)

            # Executa o modelo ONNX
            audio = self.session.run(None, {"input": input_tokens})[0]

            # Normaliza áudio para float32
            audio = np.float32(audio / np.max(np.abs(audio)))

            # Reproduz áudio
            sd.play(audio, samplerate=22050)
            sd.wait()
        except Exception as e:
            print(f"Error during local TTS: {e}")

    def text_to_tokens(self, text: str):
        """
        Converta texto em tokens compatíveis com Kokoro.
        Isso depende de como o modelo foi treinado.
        """
        # Aqui você precisa implementar o tokenizer correto ou carregar vocabulário
        # Exemplo genérico:
        tokens = np.array([ord(c) for c in text], dtype=np.int64)
        tokens = np.expand_dims(tokens, 0)  # batch dimension
        return tokens

