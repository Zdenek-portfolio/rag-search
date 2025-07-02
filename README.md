# Interní dokumentový vyhledávač s AI

Tato aplikace umožňuje nahrávat dokumenty (PDF, DOCX, TXT) a vyhledávat v jejich obsahu pomocí přirozeného jazyka díky OpenAI GPT a embeddingům.

## Spuštění projektu

```bash
python -m venv venv
source venv/bin/activate  # nebo .\venv\Scripts\activate na Windows
pip install -r requirements.txt
python run.py
```

Do `.env` přidej svůj OpenAI klíč:
```
OPENAI_API_KEY=tvuj-klic
```
