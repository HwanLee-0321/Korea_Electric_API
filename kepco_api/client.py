import requests
import json
import sys

class KepcoApiClient:
    """
    한국전력공사 빅데이터 API 클라이언트
    """
    def __init__(self, api_key):
        if not api_key or api_key == "여기에 발급받은 API 키를 입력하세요":
            raise ValueError("API 키가 유효하지 않습니다. config.py 파일을 확인해주세요.")
        self.api_key = api_key

    def _call_api(self, url, params):
        """API를 호출하고 결과를 반환하는 내부 메소드"""
        # 공통 파라미터 추가
        params['apiKey'] = self.api_key
        params['returnType'] = 'json'

        try:
            response = requests.get(url, params=params, timeout=20)
            response.raise_for_status()
            data = response.json()
            if data.get('resultCd') == '00' or data.get('resultCd') is None:
                return data.get('data', data.get('totData', []))
            else:
                print(f"API Error: {data.get('resultMsg', 'Unknown error')}", file=sys.stderr)
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}", file=sys.stderr)
            return None
        except json.JSONDecodeError:
            print("JSON Decode Error", file=sys.stderr)
            return None

    def get_area_codes(self):
        """법정동 시/군/구 코드를 조회합니다."""
        url = "https://bigdata.kepco.co.kr/openapi/v1/commonCode.do"
        params = {'codeTy': 'lglDngCityCd'}
        return self._call_api(url, params)

    def get_power_usage(self, url, year, month, metro_cd, city_cd=None, extra_params=None):
        """
        월별 전력 사용량 데이터를 조회합니다.
        (계약종별, 산업별, 주택평균 등 다양한 API에 대응)
        """
        params = {
            'year': year,
            'month': month,
            'metroCd': metro_cd,
        }
        if city_cd:
            params['cityCd'] = city_cd
        
        if extra_params:
            params.update(extra_params)
            
        return self._call_api(url, params)
