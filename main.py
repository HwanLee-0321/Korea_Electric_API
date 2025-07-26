import requests
import json
import time
import os
from datetime import datetime
from config import API_KEY, CODE_FILENAME, DATA_FILENAME

# --- API 호출 함수 ---
def call_api(url, params):
    """API를 호출하고 결과를 반환하는 공통 함수"""
    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
        if data.get('resultCd') == '00' or data.get('resultCd') is None:
            return data.get('data', data.get('totData', []))
        else:
            # 오류 메시지를 좀 더 상세하게 출력
            # print(f"API Error: {data.get('resultMsg', 'Unknown error')} for params: {params}")
            return None
    except requests.exceptions.RequestException as e:
        # print(f"Request Error: {e}")
        return None
    except json.JSONDecodeError:
        # print(f"JSON Parsing Error: {response.text}")
        return None

# --- 1단계: 지역 코드 수집 ---
def collect_and_get_area_codes():
    """법정동 시/군/구 코드를 수집하여 파일로 저장하고, 리스트를 반환합니다."""
    if os.path.exists(CODE_FILENAME):
        print(f"'{CODE_FILENAME}' 파일이 이미 존재하여 코드 수집을 건너뜁니다.")
        with open(CODE_FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f).get('lglDngCityCd', [])

    print("--- 1단계: 법정동 시/군/구 코드 수집 시작 ---")
    url = "https://bigdata.kepco.co.kr/openapi/v1/commonCode.do"
    params = {
        'apiKey': API_KEY,
        'codeTy': 'lglDngCityCd',
        'returnType': 'json'
    }
    area_codes = call_api(url, params)

    if area_codes:
        codes_to_save = {'lglDngCityCd': area_codes}
        with open(CODE_FILENAME, 'w', encoding='utf-8') as f:
            json.dump(codes_to_save, f, indent=2, ensure_ascii=False)
        print(f"총 {len(area_codes)}개의 코드를 수집하여 '{CODE_FILENAME}'에 저장했습니다.")
        return area_codes
    else:
        print("코드 수집에 실패하여 프로세스를 중단합니다.")
        return []

# --- 2단계: 전체 데이터 수집 ---
def collect_all_data(area_codes):
    """모든 지역, API, 기간에 대해 데이터를 수집합니다."""
    api_configs = {
        'contract_usage': {
            'url': "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/contractType.do",
            'params': {"cntrCd": ""}
        },
        'industry_usage': {
            'url': "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do",
            'params': {"bizCd": ""}
        },
        'household_average': {
            'url': "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/houseAve.do",
            'params': {}
        },
        'customer_change': {
            'url': "https://bigdata.kepco.co.kr/openapi/v1/change/custNum/industryType.do",
            'params': {"bizCd": ""}
        }
    }

    start_date = datetime(2020, 7, 24)
    end_date = datetime(2025, 7, 24)
    date_range = list(generate_date_range(start_date, end_date))

    total_requests = len(area_codes) * len(api_configs) * len(date_range)
    completed_requests = 0
    all_results = {name: [] for name in api_configs.keys()}

    print(f"\n--- 2단계: 총 {total_requests}건의 월별 데이터 수집 시작 ---")

    for area in area_codes:
        if '미분류' in area.get('codeNm', ''):
            continue # 미분류 지역은 건너뛰기

        for api_name, config in api_configs.items():
            for year, month in date_range:
                params = config['params'].copy()
                params['apiKey'] = API_KEY
                params['returnType'] = 'json'
                params['year'] = year
                params['month'] = month
                params['metroCd'] = area['uppoCd']
                
                # household_average API는 cityCd를 사용하지 않음
                if api_name != 'household_average':
                    params['cityCd'] = area['code']

                result = call_api(config['url'], params)
                if result:
                    for item in result:
                        item['query_year'] = year
                        item['query_month'] = month
                        item['query_metroNm'] = area['uppoCdNm']
                        item['query_cityNm'] = area['codeNm']
                    all_results[api_name].extend(result)
                
                completed_requests += 1
                progress = (completed_requests / total_requests) * 100
                print(f"진행률: {progress:.2f}% ({completed_requests}/{total_requests})", end='\r')
                time.sleep(0.1)

    return all_results

def generate_date_range(start_date, end_date):
    """(년, 월) 튜플을 생성하는 제너레이터"""
    current_date = start_date
    while current_date <= end_date:
        yield (str(current_date.year), f"{current_date.month:02d}")
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)

def main():
    """전체 프로세스를 실행하고 결과를 저장합니다."""
    if API_KEY == "발급받은_API키를_여기에_붙여넣으세요":
        print("!!! 경고: config.py 파일의 API_KEY를 실제 키로 변경해주세요. !!!")
        return

    # 1단계 실행
    area_codes = collect_and_get_area_codes()
    if not area_codes:
        return

    # 2단계 실행
    all_data = collect_all_data(area_codes)

    # 3단계: 결과 저장
    with open(DATA_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n====================================================")
    print(f"✅ 모든 프로세스 완료! '{DATA_FILENAME}' 파일로 저장되었습니다.")
    print(f"====================================================")

if __name__ == "__main__":
    main()
