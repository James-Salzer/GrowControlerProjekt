import sys
sys.path.append("E:/Daten/James/Growcontroler/GrowControlerProjekt")  # Füge das Stammverzeichnis hinzu
from fastapi import FastAPI
from webinterface import views
import uvicorn

app = FastAPI()
app.include_router(views.router)

@app.post("/api/button_click")
async def handle_button_click(data: dict):
    print(f"Button clicked with data: {data}")
    return {"message": "Button click received"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)