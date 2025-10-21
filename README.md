# Korea Electric Power Corporation (KEPCO) API Utilization Guide

This project provides an object-oriented Python backend to collect data from the Korea Electric Power Corporation's (KEPCO) public data API and an Electron-based frontend to interact with it.

## Available Languages

*   [English](README.md)
*   [한국어](docs/README_ko.md)
*   [中文](docs/README_zh.md)
*   [日本語](docs/README_ja.md)
*   [Español](docs/README_es.md)
*   [Deutsch](docs/README_de.md)
*   [Français](docs/README_fr.md)
*   [العربية](docs/README_ar.md)

## Key Features

*   **Object-Oriented Python Backend:** Collects various power-related data provided by KEPCO via their API, structured into `KepcoApiClient` and `DataCollector` classes for better maintainability and extensibility.
*   **Electron Frontend:** A desktop application built with Electron, providing a graphical user interface to trigger data collection and display the results.
*   **API Key Configuration:** Easy API key configuration through a `config.py` file.
*   **Data Output:** Collected data is output to standard output (stdout) by the Python script, which is then captured and displayed by the Electron application.

## Requirements

*   **Python 3.11+**
    *   `requests` library
*   **Node.js (LTS recommended)**
    *   `npm` (Node Package Manager)
    *   `electron`

## Installation and Setup

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Install Python Dependencies:**

    ```bash
    pip install requests
    ```

3.  **Install Node.js Dependencies:**

    ```bash
    npm install
    ```

4.  **API Key Configuration:**

    *   Visit the KEPCO Public Data Portal ([https://bigdata.kepco.co.kr/](https://bigdata.kepco.co.kr/)), sign up, apply for API usage, and obtain an authentication key (API Key).
    *   Open `config.py` in the project's root directory and enter your obtained API key as shown below.

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **Important:** The `config.py` file contains sensitive information, so it's recommended to add it to your `.gitignore` file to prevent it from being included in your Git repository.

## Usage

### Running the Electron Application

To start the desktop application:

```bash
npm start
```

Click the "Fetch KEPCO Data" button in the application to initiate data collection. The collected data will be displayed within the application window.

### Running the Python Backend (Standalone)

You can also run the Python script directly from the terminal. The collected data will be printed to standard output.

```bash
python main.py
```

## Project Structure

```
.
├── kepco_api/
│   ├── __init__.py
│   ├── client.py       # KEPCO API client for making requests
│   └── collector.py    # Orchestrates data collection
├── src/
│   ├── main/
│   │   ├── main.js         # Electron main process
│   │   └── preload.js      # Electron preload script
│   └── renderer/
│       ├── index.html      # Renderer process HTML
│       ├── renderer.js     # Renderer process JavaScript
│       └── style.css       # Renderer process styles
├── config.py           # API key and configuration
├── main.py             # Entry point for the Python backend
├── kepco_codes.json    # (Generated) Stores regional and data codes
├── package.json        # Node.js project configuration
├── package-lock.json   # Node.js dependency lock file
├── README.md           # Project description (English)
├── README_ko.md        # Project description (Korean)
├── README_zh.md        # Project description (Chinese)
├── README_ja.md        # Project description (Japanese)
├── README_es.md        # Project description (Spanish)
├── README_de.md        # Project description (German)
├── README_fr.md        # Project description (French)
├── README_ar.md        # Project description (Arabic)
├── LICENSE             # Project license information
└── ... (other files like .git, node_modules, etc.)
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

-----

**Disclaimer:** This project is not officially provided by the Korea Electric Power Corporation and is intended as a reference example to assist with API utilization.
