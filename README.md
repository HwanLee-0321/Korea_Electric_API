# Korea Electric Power Corporation (KEPCO) API Utilization Guide

This project provides example Python code to collect data from the Korea Electric Power Corporation's (KEPCO) public data API and save it as a JSON file.

|[한국어 README](https://github.com/HwanLee-0321/Korea_Electric_API/blob/main/README(KOR).md)|

## Key Features

  - Fetches various power-related data provided by KEPCO via their API.
  - Saves the collected data in `all_kepco_data.json` format.
  - Allows for easy API key configuration through a `config.py` file.

## Requirements

  - Python 3.11
  - `requests` library

## Installation and Setup

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Install Required Libraries:**

    ```bash
    pip install requests
    ```

3.  **API Key Configuration:**

      - Visit the KEPCO Public Data Portal ([https://bigdata.kepco.co.kr/](https://www.google.com/search?q=https://bigdata.kepco.co.kr/)), sign up, apply for API usage, and obtain an authentication key (API Key).
      - Create a `config.py` file in the project's root directory and enter your obtained API key as shown below.

    <!-- end list -->

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **Important:** The `config.py` file contains sensitive information, so it's recommended to add it to your `.gitignore` file to prevent it from being included in your Git repository.

## Usage

1.  **Run the Script:**
    Execute the following command in your terminal to collect data.

    ```bash
    python main.py
    ```

2.  **Check Results:**
    Once the script finishes execution, an `all_kepco_data.json` file will be created in the project's root directory. This file contains all the data collected via the API in JSON format.

## File Structure

  - `main.py`: The main script for calling the API and processing data.
  - `config.py`: Stores configuration information, such as the API key. (You need to create this yourself)
  - `kepco_codes.json`: Contains regional and data codes required for API calls.
  - `all_kepco_data.json`: The JSON file where the script's output data is saved.
  - `README.md`: Project description file.
  - `LICENSE`: Project license information.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

-----

**Disclaimer:** This project is not officially provided by the Korea Electric Power Corporation and is intended as a reference example to assist with API utilization.
