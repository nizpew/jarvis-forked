from modules.vibranium.vision.vision import Vision
import cv2

if __name__ == "__main__":
    vision = Vision()
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if ret:
        image_path = "test_image.jpg"
        cv2.imwrite(image_path, frame)
        description = vision.generate_description("llava", image_path)
        print("Vision description:", description)
    else:
        print("Erro ao capturar imagem da câmera.")

