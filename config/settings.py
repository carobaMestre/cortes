import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

class Settings:
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")  # Aqui é necessário usar a string "YOUTUBE_API_KEY"
    GPT_API_KEY = os.getenv("GPT_API_KEY")  # Aqui também, "GPT_API_KEY" precisa estar entre aspas

settings = Settings()

# Usando a API key
print(f"Chave do YouTube: {settings.YOUTUBE_API_KEY}")
print(f"Chave do GPT: {settings.GPT_API_KEY}")
