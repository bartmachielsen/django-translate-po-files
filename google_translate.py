import requests


def translate(text, language, source_language, api_key):
    response = requests.post(
        "https://translation.googleapis.com/language/translate/v2",
        json={
            "q": text,
            "target": language,
            "source": source_language
        },
        params={
            "key": api_key
        })
    if not response.ok:
        response.raise_for_status()
    response = response.json()
    translations = response.get('data', {}).get('translations')
    return translations[0].get('translatedText') if translations else None
