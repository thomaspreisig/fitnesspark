import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_visitors():
    url = 'https://www.fitnesspark.ch/wp/wp-admin/admin-ajax.php'  # Ersetze dies durch die tatsächliche URL der Seite
    response = requests.get(url)
    response.raise_for_status()  # Fehlerbehandlung

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Den gewünschten <span> anhand seiner Attribute finden
    visitor_span = soup.find('span', {
        'data-park-id': '698',
        'data-location-name': 'FP_Glattpark'
    })
    
    if visitor_span and visitor_span.text:
        visitors = visitor_span.text.strip()
    else:
        visitors = "Keine Daten verfügbar"

    return visitors

def log_visitor_count():
    visitors = get_visitors()
    with open('visitor_log.txt', 'a') as file:
        file.write(f"{datetime.now()}: {visitors} Besucher\n")

log_visitor_count()
