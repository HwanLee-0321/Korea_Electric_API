# Guide d'utilisation de l'API de la Korea Electric Power Corporation (KEPCO)

Ce projet fournit un backend Python orienté objet pour collecter des données de l'API de données publiques de la Korea Electric Power Corporation (KEPCO) et un frontend basé sur Electron pour interagir avec elle.

## Langues disponibles

*   [Anglais](../README.md)
*   [한국어](README_ko.md)
*   [中文](README_zh.md)
*   [日本語](README_ja.md)
*   [Español](README_es.md)
*   [Deutsch](README_de.md)
*   [Français](README_fr.md)
*   [العربية](README_ar.md)

## Fonctionnalités clés

*   **Backend Python Orienté Objet :** Collecte diverses données liées à l'énergie fournies par la KEPCO via son API, structurées en classes `KepcoApiClient` et `DataCollector` pour une meilleure maintenabilité et extensibilité.
*   **Frontend Electron :** Une application de bureau construite avec Electron, offrant une interface utilisateur graphique pour déclencher la collecte de données et afficher les résultats.
*   **Configuration de la clé API :** Configuration facile de la clé API via un fichier `config.py`.
*   **Sortie des données :** Les données collectées sont envoyées à la sortie standard (stdout) par le script Python, qui est ensuite capturée et affichée par l'application Electron.

## Prérequis

*   **Python 3.11+**
    *   bibliothèque `requests`
*   **Node.js (LTS recommandé)**
    *   `npm` (Gestionnaire de paquets Node)
    *   `electron`

## Installation et configuration

1.  **Cloner le dépôt :**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Installer les dépendances Python :**

    ```bash
    pip install requests
    ```

3.  **Installer les dépendances Node.js :**

    ```bash
    npm install
    ```

4.  **Configuration de la clé API :**

    *   Visitez le portail de données publiques de la KEPCO ([https://bigdata.kepco.co.kr/]), inscrivez-vous, demandez l'utilisation de l'API et obtenez une clé d'authentification (clé API).
    *   Ouvrez `config.py` dans le répertoire racine du projet et entrez votre clé API obtenue comme indiqué ci-dessous.

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **Important :** Le fichier `config.py` contient des informations sensibles, il est donc recommandé de l'ajouter à votre fichier `.gitignore` pour éviter qu'il ne soit inclus dans votre dépôt Git.

## Utilisation

### Exécution de l'application Electron

Pour démarrer l'application de bureau :

```bash
npm start
```

Cliquez sur le bouton "Fetch KEPCO Data" dans l'application pour lancer la collecte de données. Les données collectées seront affichées dans la fenêtre de l'application.

### Exécution du backend Python (autonome)

Vous pouvez également exécuter le script Python directement depuis le terminal. Les données collectées seront imprimées sur la sortie standard.

```bash
python main.py
```

## Structure du projet

```
.
├── kepco_api/
│   ├── __init__.py
│   ├── client.py       # Client API KEPCO pour effectuer des requêtes
│   └── collector.py    # Orchestre la collecte de données
├── src/
│   ├── main/
│   │   ├── main.js         # Processus principal Electron
│   │   └── preload.js      # Script de préchargement Electron
│   └── renderer/
│       ├── index.html      # HTML du processus de rendu
│       ├── renderer.js     # JavaScript du processus de rendu
│       └── style.css       # Styles du processus de rendu
├── config.py           # Clé API et configuration
├── main.py             # Point d'entrée pour le backend Python
├── kepco_codes.json    # (Généré) Stocke les codes régionaux et de données
├── package.json        # Configuration du projet Node.js
├── package-lock.json   # Fichier de verrouillage des dépendances Node.js
├── README.md           # Description du projet (Anglais)
├── README_ko.md        # Description du projet (Coréen)
├── README_zh.md        # Description du projet (Chinois)
├── README_ja.md        # Description du projet (Japonais)
├── README_es.md        # Description du projet (Espagnol)
├── README_de.md        # Description du projet (Allemand)
├── README_fr.md        # Description du projet (Français)
├── README_ar.md        # Description du projet (Arabe)
├── LICENSE             # Informations sur la licence du projet
└── ... (autres fichiers comme .git, node_modules, etc.)
```

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

-----

**Avertissement :** Ce projet n'est pas fourni officiellement par la Korea Electric Power Corporation et est destiné à servir d'exemple de référence pour faciliter l'utilisation de l'API.