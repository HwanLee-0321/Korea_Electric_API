# 한국전력공사(KEPCO) API 활용 가이드

이 프로젝트는 Python을 사용하여 한국전력공사의 공공데이터 API로부터 데이터를 수집하고 JSON 파일로 저장하는 방법을 안내하는 예제 코드입니다.

## 주요 기능

-   한국전력공사에서 제공하는 다양한 전력 관련 데이터를 API를 통해 가져옵니다.
-   수집된 데이터를 `all_kepco_data.json` 파일 형식으로 저장합니다.
-   `config.py` 파일을 통해 API 키를 쉽게 설정할 수 있습니다.

## 요구 사항

-   Python 3.11
-   `requests` 라이브러리

## 설치 및 설정 방법

1.  **저장소 복제:**
    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **필요 라이브러리 설치:**
    ```bash
    pip install requests
    ```

3.  **API 키 설정:**
    -   한국전력공사 공공데이터 포털 (https://bigdata.kepco.co.kr/)에 접속하여 회원가입 및 API 활용 신청 후, 인증키(API Key)를 발급받으세요.
    -   프로젝트 루트 디렉터리에 `config.py` 파일을 생성하고 아래와 같이 발급받은 API 키를 입력하세요.

    ```python
    # config.py
    API_KEY = "여기에_발급받은_API_키를_입력하세요"
    ```
    **중요:** `config.py` 파일은 민감한 정보를 포함하므로 `.gitignore` 파일에 추가하여 Git 저장소에 포함되지 않도록 하는 것을 권장합니다.

## 사용 방법

1.  **스크립트 실행:**
    터미널에서 아래 명령어를 실행하여 데이터를 수집합니다.
    ```bash
    python main.py
    ```

2.  **결과 확인:**
    스크립트 실행이 완료되면, 프로젝트 루트 디렉터리에 `all_kepco_data.json` 파일이 생성됩니다. 이 파일에는 API를 통해 수집된 모든 데이터가 JSON 형식으로 저장되어 있습니다.

## 파일 구조

-   `main.py`: API를 호출하고 데이터를 처리하는 메인 스크립트입니다.
-   `config.py`: API 키와 같은 설정 정보를 저장하는 파일입니다. (직접 생성해야 합니다)
-   `kepco_codes.json`: API 호출에 필요한 지역 및 데이터 코드를 담고 있는 파일입니다.
-   `all_kepco_data.json`: 스크립트 실행 결과 데이터가 저장되는 JSON 파일입니다.
-   `README.md`: 프로젝트에 대한 설명 파일입니다.
-   `LICENSE`: 프로젝트 라이선스 정보입니다.

## 라이선스

이 프로젝트는 MIT License를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.

---

**Disclaimer:** 이 프로젝트는 한국전력공사에서 공식적으로 제공하는 것이 아니며, API 활용을 돕기 위한 참고용 예제입니다.