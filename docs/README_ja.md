# 韓国電力公社 (KEPCO) API 利用ガイド

このプロジェクトは、韓国電力公社 (KEPCO) の公開データ API からデータを収集するためのオブジェクト指向 Python バックエンドと、それと対話するための Electron ベースのフロントエンドを提供します。

## 利用可能な言語

*   [English](../README.md)
*   [한국어](README_ko.md)
*   [中文](README_zh.md)
*   [日本語](README_ja.md)
*   [Español](README_es.md)
*   [Deutsch](README_de.md)
*   [Français](README_fr.md)
*   [العربية](README_ar.md)

## 主な機能

*   **オブジェクト指向 Python バックエンド:** KEPCO が API を介して提供するさまざまな電力関連データを収集し、保守性と拡張性を向上させるために `KepcoApiClient` および `DataCollector` クラスに構造化されています。
*   **Electron フロントエンド:** Electron で構築されたデスクトップアプリケーションで、データ収集をトリガーし、結果を表示するためのグラフィカルユーザーインターフェースを提供します。
*   **API キー設定:** `config.py` ファイルを介した簡単な API キー設定。
*   **データ出力:** 収集されたデータは Python スクリプトによって標準出力 (stdout) に出力され、その後 Electron アプリケーションによってキャプチャおよび表示されます。

## 要件

*   **Python 3.11+**
    *   `requests` ライブラリ
*   **Node.js (LTS 推奨)**
    *   `npm` (Node Package Manager)
    *   `electron`

## インストールとセットアップ

1.  **リポジトリのクローン:**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **Python 依存関係のインストール:**

    ```bash
    pip install requests
    ```

3.  **Node.js 依存関係のインストール:**

    ```bash
    npm install
    ```

4.  **API キー設定:**

    *   KEPCO 公開データポータル ([https://bigdata.kepco.co.kr/](https://bigdata.kepco.co.kr/)) にアクセスし、サインアップして API 使用を申請し、認証キー (API キー) を取得します。
    *   プロジェクトのルートディレクトリにある `config.py` を開き、取得した API キーを以下のように入力します。

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **重要:** `config.py` ファイルには機密情報が含まれているため、Git リポジトリに含まれないように `.gitignore` ファイルに追加することをお勧めします。

## 使用方法

### Electron アプリケーションの実行

デスクトップアプリケーションを起動するには:

```bash
npm start
```

アプリケーションの「KEPCO データ取得」ボタンをクリックしてデータ収集を開始します。収集されたデータはアプリケーションウィンドウ内に表示されます。

### Python バックエンドの実行 (スタンドアロン)

Python スクリプトをターミナルから直接実行することもできます。収集されたデータは標準出力に表示されます。

```bash
python main.py
```

## プロジェクト構造

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

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については `LICENSE` ファイルを参照してください。

-----

**免責事項:** このプロジェクトは韓国電力公社によって公式に提供されているものではなく、API 利用を支援するための参考例として意図されています。