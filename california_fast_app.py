import numpy as np
import joblib
from fastapi import FastAPI
import uvicorn

app=FastAPI()

obj=joblib.load('california.joblib')
model=obj['model']
cols=obj['columns']

@app.get('/')
def Main():
    return('welcome')

@app.get('/predict')
def predict(MEDInc: float, HouseAge: float,
               AveRooms: float, AveBedrms: float,
                 Population: float, AveOccup: float,
                   Latitude: float, Longitude: float):
    
    Input=[[MEDInc, HouseAge, AveRooms, AveBedrms,
             Population, AveOccup, Latitude, Longitude]]
    out=model.predict(Input)
    return(f"the MED House Val is {out}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


## at last run and link will http://0.0.0.0:8000 but change http://127.0.0.1:8000