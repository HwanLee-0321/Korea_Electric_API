# 한국전력공사(KEPCO) API 활용 가이드

이 프로젝트는 한국전력공사(KEPCO) 공공 데이터 API로부터 데이터를 수집하기 위한 객체 지향 Python 백엔드와 이를 상호작용하는 Electron 기반 프론트엔드를 제공합니다.

## 사용 가능한 언어

*   [English](../README.md)
*   [한국어](README_ko.md)
*   [中文](README_zh.md)
*   [日本語](README_ja.md)
*   [Español](README_es.md)
*   [Deutsch](README_de.md)
*   [Français](README_fr.md)
*   [العربية](README_ar.md)

## 주요 기능

*   **객체 지향 Python 백엔드:** KEPCO가 API를 통해 제공하는 다양한 전력 관련 데이터를 `KepcoApiClient` 및 `DataCollector` 클래스로 구조화하여 유지보수성과 확장성을 높였습니다.
*   **Electron 프론트엔드:** Electron으로 구축된 데스크톱 애플리케이션으로, 데이터 수집을 트리거하고 결과를 표시하는 그래픽 사용자 인터페이스를 제공합니다.
*   **API 키 설정:** `config.py` 파일을 통해 API 키를 쉽게 설정할 수 있습니다.
*   **데이터 출력:** 수집된 데이터는 Python 스크립트에 의해 표준 출력(stdout)으로 출력되며, Electron 애플리케이션이 이를 캡처하여 표시합니다.

## 요구 사항

*   **Python 3.11+**
    *   `requests` 라이브러리
*   **Node.js (LTS 권장)**
    *   `npm` (Node Package Manager)
    *   `electron`

## 설치 및 설정

1.  **저장소 복제:**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Python 종속성 설치:**

    ```bash
    pip install requests
    ```

3.  **Node.js 종속성 설치:**

    ```bash
    npm install
    ```

4.  **API 키 설정:**

    *   KEPCO 공공 데이터 포털([https://bigdata.kepco.co.kr/](https://bigdata.kepco.co.kr/))에 방문하여 회원가입 후 API 사용을 신청하고 인증 키(API Key)를 발급받으세요.
    *   프로젝트의 루트 디렉토리에 있는 `config.py` 파일을 열고 아래와 같이 발급받은 API 키를 입력하세요.

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **중요:** `config.py` 파일에는 민감한 정보가 포함되어 있으므로, Git 저장소에 포함되지 않도록 `.gitignore` 파일에 추가하는 것을 권장합니다.

## 사용법

### Electron 애플리케이션 실행

데스크톱 애플리케이션을 시작하려면:

```bash
npm start
```

애플리케이션에서 "Fetch KEPCO Data" 버튼을 클릭하여 데이터 수집을 시작합니다. 수집된 데이터는 애플리케이션 창 내에 표시됩니다.

### Python 백엔드 실행 (독립 실행)

터미널에서 Python 스크립트를 직접 실행할 수도 있습니다. 수집된 데이터는 표준 출력으로 인쇄됩니다.

```bash
python main.py
```

## 프로젝트 구조

```
.
├── kepco_api/
│   ├── __init__.py
│   ├── client.py       # KEPCO API 요청을 위한 클라이언트
│   └── collector.py    # 데이터 수집을 조율
├── src/
│   ├── main/
│   │   ├── main.js         # Electron 메인 프로세스
│   │   └── preload.js      # Electron 프리로드 스크립트
│   └── renderer/
│       ├── index.html      # 렌더러 프로세스 HTML
│       ├── renderer.js     # 렌더러 프로세스 JavaScript
│       └── style.css       # 렌더러 프로세스 스타일
├── config.py           # API 키 및 설정
├── main.py             # Python 백엔드의 진입점
├── kepco_codes.json    # (생성됨) 지역 및 데이터 코드 저장
├── package.json        # Node.js 프로젝트 설정
├── package-lock.json   # Node.js 종속성 잠금 파일
├── README.md           # 프로젝트 설명 (영어)
├── README_ko.md        # 프로젝트 설명 (한국어)
├── README_zh.md        # 프로젝트 설명 (중국어)
├── README_ja.md        # 프로젝트 설명 (일본어)
├── README_es.md        # 프로젝트 설명 (스페인어)
├── README_de.md        # 프로젝트 설명 (독일어)
├── README_fr.md        # 프로젝트 설명 (프랑스어)
├── README_ar.md        # 프로젝트 설명 (아랍어)
├── LICENSE             # 프로젝트 라이선스 정보
└── ... (기타 파일: .git, node_modules 등)
```

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 `LICENSE` 파일을 참조하십시오.

-----

**면책 조항:** 이 프로젝트는 한국전력공사에서 공식적으로 제공하는 것이 아니며, API 활용을 돕기 위한 참고 예시로 제작되었습니다.