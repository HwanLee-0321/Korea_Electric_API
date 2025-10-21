import json
import os
import sys
import time
from datetime import datetime

class DataCollector:
    """
    KEPCO 데이터 수집기
    """
    def __init__(self, client, code_filename):
        self.client = client
        self.code_filename = code_filename
        self.api_configs = {
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

    def _generate_date_range(self, start_date, end_date):
        """(년, 월) 튜플을 생성하는 제너레이터""" 
        current_date = start_date
        while current_date <= end_date:
            yield (str(current_date.year), f"{current_date.month:02d}")
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)

    def get_area_codes(self):
        """
        법정동 코드를 파일에서 읽거나 API를 통해 수집합니다.
        """
        if os.path.exists(self.code_filename):
            print(f"'{self.code_filename}' 파일이 이미 존재하여 코드 수집을 건너뜁니다.", file=sys.stderr)
            with open(self.code_filename, 'r', encoding='utf-8') as f:
                return json.load(f).get('lglDngCityCd', [])

        print("--- 1단계: 법정동 시/군/구 코드 수집 시작 ---", file=sys.stderr)
        area_codes = self.client.get_area_codes()

        if area_codes:
            codes_to_save = {'lglDngCityCd': area_codes}
            with open(self.code_filename, 'w', encoding='utf-8') as f:
                json.dump(codes_to_save, f, indent=2, ensure_ascii=False)
            print(f"총 {len(area_codes)}개의 코드를 수집하여 '{self.code_filename}'에 저장했습니다.", file=sys.stderr)
            return area_codes
        else:
            print("코드 수집에 실패하여 프로세스를 중단합니다.", file=sys.stderr)
            return []

    def collect_all_data(self, area_codes):
        """
        모든 지역, API, 기간에 대해 데이터를 수집합니다.
        """
        start_date = datetime(2020, 7, 24)
        end_date = datetime(2025, 7, 24)
        date_range = list(self._generate_date_range(start_date, end_date))

        # '미분류' 지역 제외
        valid_area_codes = [area for area in area_codes if '미분류' not in area.get('codeNm', '')]
        
        total_requests = len(valid_area_codes) * len(self.api_configs) * len(date_range)
        completed_requests = 0
        all_results = {name: [] for name in self.api_configs.keys()}

        print(f"\n--- 2단계: 총 {total_requests}건의 월별 데이터 수집 시작 ---", file=sys.stderr)

        for area in valid_area_codes:
            for api_name, config in self.api_configs.items():
                for year, month in date_range:
                    extra_params = config['params'].copy()
                    # household_average API는 cityCd를 사용하지 않음
                    city_cd = area['code'] if api_name != 'household_average' else None
                    
                    result = self.client.get_power_usage(
                        url=config['url'],
                        year=year,
                        month=month,
                        metro_cd=area['uppoCd'],
                        city_cd=city_cd,
                        extra_params=extra_params
                    )

                    if result:
                        for item in result:
                            item['query_year'] = year
                            item['query_month'] = month
                            item['query_metroNm'] = area['uppoCdNm']
                            item['query_cityNm'] = area['codeNm']
                        all_results[api_name].extend(result)

                    completed_requests += 1
                    progress = (completed_requests / total_requests) * 100
                    print(f"진행률: {progress:.2f}% ({completed_requests}/{total_requests})", end='\r', file=sys.stderr)
                    time.sleep(0.1)
        
        print("\n데이터 수집 완료.", file=sys.stderr)
        return all_results
