# 韩国电力公司 (KEPCO) API 利用指南

本项目提供了一个面向对象的 Python 后端，用于从韩国电力公司 (KEPCO) 的公共数据 API 收集数据，以及一个基于 Electron 的前端与之交互。

## 可用语言

*   [English](../README.md)
*   [한국어](README_ko.md)
*   [中文](README_zh.md)
*   [日本語](README_ja.md)
*   [Español](README_es.md)
*   [Deutsch](README_de.md)
*   [Français](README_fr.md)
*   [العربية](README_ar.md)

## 主要特点

*   **面向对象的 Python 后端：** 通过 KEPCO 的 API 收集各种电力相关数据，并将其结构化为 `KepcoApiClient` 和 `DataCollector` 类，以提高可维护性和可扩展性。
*   **Electron 前端：** 一个使用 Electron 构建的桌面应用程序，提供图形用户界面来触发数据收集并显示结果。
*   **API 密钥配置：** 通过 `config.py` 文件轻松配置 API 密钥。
*   **数据输出：** 收集到的数据由 Python 脚本输出到标准输出 (stdout)，然后由 Electron 应用程序捕获并显示。

## 要求

*   **Python 3.11+**
    *   `requests` 库
*   **Node.js (推荐 LTS 版本)**
    *   `npm` (Node 包管理器)
    *   `electron`

## 安装与设置

1.  **克隆仓库：**

    ```bash
    git clone https://github.com/your-username/Korea_Electric_Power_Corporation_API_Guid.git
    cd Korea_Electric_Power_Corporation_API_Guid
    ```

2.  **安装 Python 依赖：**

    ```bash
    pip install requests
    ```

3.  **安装 Node.js 依赖：**

    ```bash
    npm install
    ```

4.  **API 密钥配置：**

    *   访问 KEPCO 公共数据门户 ([https://bigdata.kepco.co.kr/](https://bigdata.kepco.co.kr/))，注册、申请 API 使用并获取认证密钥 (API Key)。
    *   打开项目根目录下的 `config.py` 文件，并按如下所示输入您获得的 API 密钥。

    ```python
    # config.py
    API_KEY = "ENTER_YOUR_API_KEY_HERE"
    ```

    **重要提示：** `config.py` 文件包含敏感信息，建议将其添加到您的 `.gitignore` 文件中，以防止其被包含在您的 Git 仓库中。

## 使用方法

### 运行 Electron 应用程序

要启动桌面应用程序：

```bash
npm start
```

点击应用程序中的“Fetch KEPCO Data”按钮以启动数据收集。收集到的数据将显示在应用程序窗口中。

### 运行 Python 后端 (独立)

您也可以直接从终端运行 Python 脚本。收集到的数据将打印到标准输出。

```bash
python main.py
```

## 项目结构

```
.
├── kepco_api/
│   ├── __init__.py
│   ├── client.py       # 用于发出请求的 KEPCO API 客户端
│   └── collector.py    # 协调数据收集
├── src/
│   ├── main/
│   │   ├── main.js         # Electron 主进程
│   │   └── preload.js      # Electron 预加载脚本
│   └── renderer/
│       ├── index.html      # 渲染器进程 HTML
│       ├── renderer.js     # 渲染器进程 JavaScript
│       └── style.css       # 渲染器进程样式
├── config.py           # API 密钥和配置
├── main.py             # Python 后端的入口点
├── kepco_codes.json    # (生成) 存储区域和数据代码
├── package.json        # Node.js 项目配置
├── package-lock.json   # Node.js 依赖锁定文件
├── README.md           # 项目描述 (英文)
├── README_ko.md        # 项目描述 (韩文)
├── README_zh.md        # 项目描述 (中文)
├── README_ja.md        # 项目描述 (日文)
├── README_es.md        # 项目描述 (西班牙文)
├── README_de.md        # 项目描述 (德文)
├── README_fr.md        # 项目描述 (法文)
├── README_ar.md        # 项目描述 (阿拉伯文)
├── LICENSE             # 项目许可证信息
└── ... (其他文件，如 .git, node_modules 等)
```

## 许可证

本项目采用 MIT 许可证。有关详细信息，请参阅 `LICENSE` 文件。

-----

**免责声明：** 本项目并非由韩国电力公司官方提供，仅作为协助 API 利用的参考示例。