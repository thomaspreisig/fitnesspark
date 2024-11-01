import requests
from datetime import datetime

def get_visitors():
    # URL für die AJAX-Anfrage
    url = 'https://www.fitnesspark.ch/wp/wp-admin/admin-ajax.php'
    
    # Parameter für die Anfrage, basierend auf den Informationen, die du gegeben hast
    params = {
        'action': 'single_park_update_visitors',  # Der spezifische Action-Parameter
        'data-park-id': '698',                    # ID des Fitnessparks
        'data-location-id': '31'                  # Weitere ID, falls benötigt
    }
    
    # Optionale Header (User-Agent, Referer), um die Anfrage "wie ein Browser" aussehen zu lassen
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Referer': 'https://www.fitnesspark.ch'
    }
    
    # Anfrage senden und Antwort prüfen
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Löst eine Ausnahme bei HTTP-Fehlern aus

    # Besucherzahl extrahieren, wenn sie im Text der Antwort enthalten ist
    if response.text.isdigit():
        visitors = response.text.strip()
    else:
        visitors = "Keine Daten verfügbar"
    
    return visitors

def log_visitor_count():
    # Besucherzahl abrufen
    visitors = get_visitors()
    
    # Ergebnis in einer Datei speichern
    with open('visitor_log.txt', 'a') as file:
        file.write(f"{datetime.now()}: {visitors} Besucher\n")

# Skript ausführen
log_visitor_count()
