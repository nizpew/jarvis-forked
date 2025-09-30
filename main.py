# main.py
from modules.vibranium.vision.vision import Vision
import os
import cv2
from modules.Interlocus import Interlocus
from modules.ollama_nlp import OllamaNLP
from dotenv import load_dotenv
import asyncio
import modules.tools.get_current_weather as weather_module
from modules.tools.duckduckgo_search import DuckDuckGoSearch

load_dotenv(override=True)

# Variáveis de ambiente com valores padrão
JARVIS_MODEL = os.getenv('JARVIS_MODEL', 'fotiecodes/jarvis:3b')
VISION_MODEL = os.getenv('VISION_MODEL', 'llava')

def main():
    interlocus = Interlocus()
    ollam_nlp = OllamaNLP()
    vision = Vision()
    duck_search = DuckDuckGoSearch()

    if not JARVIS_MODEL:
        print("Erro: JARVIS_MODEL não definido. Verifique o .env")
        return

    while True:
        user_input = interlocus.listen()

        # Comandos de visão
        visionKeywords = [
            'what do you see', 'what are you looking at', 'tell me what you see',
            'look at this', 'describe this', 'describe what you see', 'describe'
        ]
        if any(visionKeyword in user_input for visionKeyword in visionKeywords):
            print("Looking...")
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cap.release()
            cv2.destroyAllWindows()

            images_dir = os.path.join("assets", "images")
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            image_path = os.path.join("assets", "images", "image.jpg")
            cv2.imwrite(image_path, frame)

            print("Thinking...")
            description = vision.generate_description(VISION_MODEL, image_path)
            asyncio.run(interlocus.speak(description))
            continue

        # Comandos de desligamento
        goodByeKeywords = ['sleep', 'goodbye', 'go to sleep', 'shut down', 'shutdown', 'exit', 'quit']
        if any(goodByeKeyword in user_input for goodByeKeyword in goodByeKeywords):
            print("Exiting...")
            good_bye_res = ollam_nlp.generate_text(
                JARVIS_MODEL, user_input, "You have been asked to shutdown, say goodbye to the user."
            )
            asyncio.run(interlocus.speak(good_bye_res))
            break

        # Comando DuckDuckGo
        if any(phrase in user_input.lower() for phrase in duck_search.trigger_phrases()):
            result = duck_search.perform_search(user_input)
            asyncio.run(interlocus.speak(result))
            continue

        # Comando de previsão do tempo detectando cidade automaticamente
        if "weather" in user_input.lower():
            city = weather_module.get_user_city()  # função que detecta cidade via IP
            weather_info = weather_module.get_current_weather(city)
            response = f"Weather in {city}: {weather_info}"
            asyncio.run(interlocus.speak(response))
            continue

        # Resposta geral via OllamaNLP
        processed_input = ollam_nlp.generate_text(JARVIS_MODEL, user_input)
        asyncio.run(interlocus.speak(processed_input))

if __name__ == "__main__":
    main()

