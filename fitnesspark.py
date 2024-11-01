import requests
import csv
from datetime import datetime
import pytz

def get_visitors():
    # URL für die AJAX-Anfrage mit vollständigen Parametern
    url = 'https://www.fitnesspark.ch/wp/wp-admin/admin-ajax.php'
    
    # Parameter für die Anfrage
    params = {
        'action': 'single_park_update_visitors',  # Der spezifische Action-Parameter
        'location_id': '31',                      # ID des Fitnessparks
        'location_name': 'FP_Glattpark'           # Name der Location
    }
    
    # Header für die Anfrage
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Referer': 'https://www.fitnesspark.ch'
    }
    
    # Anfrage senden und Antwort prüfen
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Löst eine Ausnahme bei HTTP-Fehlern aus

    # Antwort ausgeben, um zu überprüfen, ob die Besucherzahl enthalten ist
    print("Antworttext:", response.text)
    
    # Besucherzahl extrahieren, falls im Text der Antwort eine Zahl enthalten ist
    if response.text.isdigit():
        visitors = int(response.text.strip())
    else:
        visitors = "Keine Daten verfügbar"  # Falls keine Zahl gefunden wird
    
    return visitors

def log_visitor_count():
    # Zeitzone UTC+1 definieren
    zurich_timezone = pytz.timezone("Europe/Zurich")
    
    # Aktuelles Datum und Uhrzeit in UTC+1
    timestamp = datetime.now(zurich_timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    # Besucherzahl abrufen
    visitors = get_visitors()
    
    # CSV-Datei mit Datum/Uhrzeit und Besucherzahl aktualisieren
    with open('visitor_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Überschrift hinzufügen, falls die Datei neu ist
        file.seek(0, 2)  # Datei an das Ende setzen
        if file.tell() == 0:  # Wenn die Datei leer ist
            writer.writerow(["Datum und Uhrzeit", "Anzahl Besucher"])
        
        # Datenzeile hinzufügen
        writer.writerow([timestamp, visitors if visitors is not None else "Keine Daten verfügbar"])

# Skript ausführen
log_visitor_count()
