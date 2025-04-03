import requests

def get_ip_info(ip_address):
    # API-Endpunkt von ipinfo.io
    url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        # Anfrage an die API
        response = requests.get(url)
        
        # Überprüfe den Statuscode der Antwort
        if response.status_code == 200:
            data = response.json()
            # Gibt die Informationen zurück, die wir möchten
            location = data.get('city', 'Unbekannte Stadt') + ", " + data.get('region', 'Unbekannte Region') + ", " + data.get('country', 'Unbekanntes Land')
            return location
        else:
            return f"Fehler: {response.status_code}"
    except Exception as e:
        return f"Fehler: {str(e)}"

def main():
    ip_address = input("Gib die IP-Adresse ein: ")
    location = get_ip_info(ip_address)
    print(f"Die IP-Adresse {ip_address} befindet sich in: {location}")

if __name__ == "__main__":
    main()
