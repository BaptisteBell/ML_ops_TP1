from fastapi import FastAPI
from pydantic import BaseModel
import model_utils

app = FastAPI()

model = model_utils.load_model()

class HouseFeatures(BaseModel):
    size: float
    bedrooms: int
    garden: int

@app.post("/predict")
def predict(house: HouseFeatures):
    predicted_price = model_utils.predict_price(model, house.size, house.bedrooms, house.garden)
    
    return {"prediction": predicted_price}