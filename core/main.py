import sys
sys.path.append("E:/Daten/James/Growcontroler/GrowControlerProjekt")  # Füge das Stammverzeichnis hinzu
from fastapi import FastAPI
from webinterface import views
import uvicorn
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Growcontroler.settings')

application = get_wsgi_application()

app = FastAPI()
app.include_router(views.router)

@app.post("/api/button_click")
async def handle_button_click(data: dict):
    print(f"Button clicked with data: {data}")
    return {"message": "Button click received"}

# Starte den Django-Entwicklungsserver nicht hier. Verwende stattdessen den Befehl
# python manage.py runserver