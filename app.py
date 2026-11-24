
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import numpy as np
import joblib
import os
import uvicorn
import logging

app = FastAPI()

# Configure templates and static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# Load ML model
MODEL_PATH = os.path.join(BASE_DIR, "california.joblib")

obj = joblib.load(MODEL_PATH)

model = obj["model"]
cols = obj["columns"]


# Field information
FIELD_INFO = {
    "MedInc": ("Median Income", "Median income of households"),
    "HouseAge": ("House Age", "Median age of houses"),
    "AveRooms": ("Average Rooms", "Average number of rooms"),
    "AveBedrms": ("Average Bedrooms", "Average bedrooms"),
    "Population": ("Population", "Area population"),
    "AveOccup": ("Average Occupancy", "Average household occupancy"),
    "Latitude": ("Latitude", "Geographical latitude"),
    "Longitude": ("Longitude", "Geographical longitude")
}


@app.api_route("/", methods=["GET", "POST"])
async def Main(request: Request):

    prediction = None
    error = None
    submitted_values = {}

    if request.method == "POST":

        try:
            form = await request.form()

            In = []

            for i in cols:

                value = str(form.get(str(i), "")).strip()

                if value == "":
                    raise ValueError(f"Please enter {i}")

                v = float(value)

                if not np.isfinite(v):
                    raise ValueError(f"Invalid value for {i}")

                In.append(v)
                submitted_values[str(i)] = value

            Input = np.array([In])

            out = model.predict(Input)

            prediction = float(out[0])

        except ValueError as e:
            error = str(e)

        except Exception:
            logging.exception("Prediction error")
            error = "Something went wrong while predicting."

    fields = []

    for i in cols:

        label, hint = FIELD_INFO.get(
            str(i),
            (str(i).replace("_", " ").title(),
             "Enter a numeric value")
        )

        fields.append({
            "key": str(i),
            "label": label,
            "hint": hint
        })

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "fields": fields,
            "prediction": prediction,
            "error": error,
            "submitted_values": submitted_values
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
