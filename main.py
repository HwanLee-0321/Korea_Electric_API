import json
import sys
from config import API_KEY, CODE_FILENAME
from kepco_api.client import KepcoApiClient
from kepco_api.collector import DataCollector

def main():
    """
    애플리케이션 메인 실행 함수
    """
    try:
        # 1. 클라이언트 및 컬렉터 초기화
        client = KepcoApiClient(API_KEY)
        collector = DataCollector(client, CODE_FILENAME)

        # 2. 지역 코드 가져오기
        area_codes = collector.get_area_codes()
        if not area_codes:
            return

        # 3. 모든 데이터 수집
        all_data = collector.collect_all_data(area_codes)

        # 4. 결과 출력
        print(json.dumps(all_data, ensure_ascii=False))

    except ValueError as e:
        # API 키가 설정되지 않은 경우와 같은 명시적 오류 처리
        error_message = {"error": str(e)}
        print(json.dumps(error_message, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # 그 외 예상치 못한 오류 처리
        error_message = {"error": f"예상치 못한 오류가 발생했습니다: {e}"}
        print(json.dumps(error_message, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
