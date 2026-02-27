from fastapi import FastAPI, Depends

app = FastAPI()

class Settings:
    def __init__(self):
        self.api_key = "my_secret"
        self.debug_mode = True
        self.app_name = "My App"
        self.version = "1.0.0"

def get_settings():
    return Settings()

@app.get("/config")
def get_config(settings: Settings = Depends(get_settings)):
    return {
        'app_name': settings.app_name,
        'version': settings.version,
        'debug_mode': settings.debug_mode,
        'api_key': settings.api_key
    }