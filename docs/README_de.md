# Korea Electric Power Corporation (KEPCO) API-Nutzungsleitfaden

Dieses Projekt bietet ein objektorientiertes Python-Backend zur Erfassung von Daten aus der öffentlichen API der Korea Electric Power Corporation (KEPCO) und ein Electron-basiertes Frontend zur Interaktion damit.

## Verfügbare Sprachen

*   [English](../README.md)
*   [한국어](README_ko.md)
*   [中文](README_zh.md)
*   [日本語](README_ja.md)
*   [Español](README_es.md)
*   [Deutsch](README_de.md)
*   [Français](README_fr.md)
*   [العربية](README_ar.md)

## Hauptmerkmale

*   **Objektorientiertes Python-Backend:** Sammelt verschiedene strombezogene Daten, die von KEPCO über deren API bereitgestellt werden, strukturiert in `KepcoApiClient`- und `DataCollector`-Klassen für bessere Wartbarkeit und Erweiterbarkeit.
*   **Electron-Frontend:** Eine mit Electron erstellte Desktop-Anwendung, die eine grafische Benutzeroberfläche zum Auslösen der Datenerfassung und zur Anzeige der Ergebnisse bietet.
*   **API-Schlüssel-Konfiguration:** Einfache API-Schlüssel-Konfiguration über eine `config.py`-Datei.
*   **Datenausgabe:** Die gesammelten Daten werden vom Python-Skript an die Standardausgabe (stdout) ausgegeben, die dann von der Electron-Anwendung erfasst und angezeigt wird.

## Anforderungen

*   **Python 3.11+**
    *   `requests`-Bibliothek
*   **Node.js (LTS empfohlen)**
    *   `npm` (Node Package Manager)
    *   `electron`

## Installation und Einrichtung

1.  **Repository klonen:**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Python-Abhängigkeiten installieren:**

    ```bash
    pip install requests
    ```

3.  **Node.js-Abhängigkeiten installieren:**

    ```bash
    npm install
    ```

4.  **API-Schlüssel-Konfiguration:**

    *   Besuchen Sie das KEPCO Public Data Portal ([https://bigdata.kepco.co.kr/](https://bigdata.kepco.co.kr/)), registrieren Sie sich, beantragen Sie die API-Nutzung und erhalten Sie einen Authentifizierungsschlüssel (API Key).
    *   Öffnen Sie `config.py` im Stammverzeichnis des Projekts und geben Sie Ihren erhaltenen API-Schlüssel wie unten gezeigt ein.

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **Wichtig:** Die Datei `config.py` enthält sensible Informationen. Es wird daher empfohlen, sie zu Ihrer `.gitignore`-Datei hinzuzufügen, um zu verhindern, dass sie in Ihr Git-Repository aufgenommen wird.

## Verwendung

### Ausführen der Electron-Anwendung

Um die Desktop-Anwendung zu starten:

```bash
npm start
```

Klicken Sie in der Anwendung auf die Schaltfläche "Fetch KEPCO Data", um die Datenerfassung zu starten. Die gesammelten Daten werden im Anwendungsfenster angezeigt.

### Ausführen des Python-Backends (eigenständig)

Sie können das Python-Skript auch direkt über das Terminal ausführen. Die gesammelten Daten werden auf der Standardausgabe ausgegeben.

```bash
python main.py
```

## Projektstruktur

```
.
├── kepco_api/
│   ├── __init__.py
│   ├── client.py       # KEPCO API-Client für Anfragen
│   └── collector.py    # Organisiert die Datenerfassung
├── src/
│   ├── main/
│   │   ├── main.js         # Electron Hauptprozess
│   │   └── preload.js      # Electron Preload-Skript
│   └── renderer/
│       ├── index.html      # Renderer-Prozess HTML
│       ├── renderer.js     # Renderer-Prozess JavaScript
│       └── style.css       # Renderer-Prozess Stile
├── config.py           # API-Schlüssel und Konfiguration
├── main.py             # Einstiegspunkt für das Python-Backend
├── kepco_codes.json    # (Generiert) Speichert regionale und Datencodes
├── package.json        # Node.js Projektkonfiguration
├── package-lock.json   # Node.js Abhängigkeits-Sperrdatei
├── README.md           # Projektbeschreibung (Englisch)
├── README_ko.md        # Projektbeschreibung (Koreanisch)
├── README_zh.md        # Projektbeschreibung (Chinesisch)
├── README_ja.md        # Projektbeschreibung (Japanisch)
├── README_es.md        # Projektbeschreibung (Spanisch)
├── README_de.md        # Projektbeschreibung (Deutsch)
├── README_fr.md        # Projektbeschreibung (Französisch)
├── README_ar.md        # Projektbeschreibung (Arabisch)
├── LICENSE             # Projektlizenzinformationen
└── ... (andere Dateien wie .git, node_modules, etc.)
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Details finden Sie in der Datei `LICENSE`.

-----

**Haftungsausschluss:** Dieses Projekt wird nicht offiziell von der Korea Electric Power Corporation bereitgestellt und dient als Referenzbeispiel zur Unterstützung der API-Nutzung.