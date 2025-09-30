import asyncio
from kokoro_onnx import Kokoro

async def main():
    kokoro_model_path = "kokoro-v0_19.onnx"
    voices_file_path = "voices-v1.0.bin"
    kokoro_voice = "bm_george"  # voz padrão offline do Kokoro

    # Inicializa o Kokoro
    kokoro = Kokoro(kokoro_model_path, voices_file_path)

    test_text = "Hello, this is a test. Can you hear me?"

    try:
        # Usando a voz bm_george
        audio = kokoro.create(test_text, voice=kokoro_voice)

        output_path = "test_output.wav"
        with open(output_path, "wb") as f:
            f.write(audio)

        print(f"Áudio gerado com sucesso! Arquivo salvo em: {output_path}")

    except Exception as e:
        print(f"Erro ao gerar áudio com Kokoro: {e}")

if __name__ == "__main__":
    asyncio.run(main())

