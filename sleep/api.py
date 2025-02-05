import base64

import cv2
import numpy as np
import torch
from PIL import Image
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from transformers import AutoImageProcessor, AutoModelForImageClassification

app = FastAPI()

# Load the model and processor
processor = AutoImageProcessor.from_pretrained("MichalMlodawski/open-closed-eye-classification-mobilev2")
model = AutoModelForImageClassification.from_pretrained("MichalMlodawski/open-closed-eye-classification-mobilev2")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive base64 encoded image data from the client
            base64_image = await websocket.receive_text()

            # Remove the data URL prefix if present
            if 'base64,' in base64_image:
                base64_image = base64_image.split('base64,')[1]

            # Decode base64 to bytes
            image_bytes = base64.b64decode(base64_image)

            # Convert bytes to numpy array
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Convert to PIL Image
            image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Preprocess the image and perform inference
            inputs = processor(images=image_pil, return_tensors="pt")
            with torch.no_grad():
                logits = model(**inputs).logits

            # Get the predicted class
            predicted_class = logits.argmax(-1).item()

            # Send the result back to the client
            await websocket.send_text(f"Predicted class: {predicted_class}")

    except WebSocketDisconnect:
        print("Client disconnected")
