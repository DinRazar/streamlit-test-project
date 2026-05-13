from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI(title="CIFAR-3 Classification API")

model = tf.keras.models.load_model("best_classification_model.h5")
class_names = ["airplane", "ship", "truck"]

def preprocess_image(image: Image.Image):
    image = image.convert("RGB")
    image = image.resize((32, 32))
    img_array = np.array(image).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.get("/")
def root():
    return {"message": "API работает"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image, verbose=0)
    predicted_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return JSONResponse({
        "predicted_class": class_names[predicted_index],
        "confidence": confidence
    })