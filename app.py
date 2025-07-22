def monetization_consulting():
    print("=== SNS 수익모델 컨설팅 프로그램 ===")
    print("시중 코치 방법 기반: 단계별 전략 (affiliate → courses) (e.g., Daria Astanaeva, Thinkific platforms)")
    
    # 입력: 현재 단계
    stage = input("현재 단계 (초창기/중간/수익화): ")
    audience_size = input("오디언스 규모 (e.g., 1000명): ")
    content_type = input("주 콘텐츠 유형 (e.g., 자기관리 팁): ")
    
    # 분석 및 제안 (7 options from Bulkly, diversified income)
    strategies = {
        "초창기": ["Affiliate 마케팅: 뉴스킨 제품 링크 (e.g., 10% 커미션, Uscreen 스타일).",
                   "스폰서십: 브랜드 콜라보 (초기 1000명부터 가능).",
                   "팁: 콘텐츠에 CTA 추가 (e.g., '링크 bio')."],
        "중간": ["멤버십: Patreon-like 루틴방 (월 5000원, exclusive 콘텐츠).",
                 "웹클래스: Thinkific로 코스 판매 (e.g., '변신 루틴' 10만원).",
                 "팁: 이메일 리스트 빌드 (Daria 방법)."],
        "수익화": ["온라인 코스: 풀 패키지 (courses + coaching, 100만원+).",
                   "상품화: eBook/머치 (content_type 기반).",
                   "팁: 다각화 - 7 streams (affiliate + ads)."]
    }
    
    # 출력
    print(f"\n[{stage} 단계 수익화 플랜]")
    for strat in strategies.get(stage, ["단계 확인하세요."]):
        print(strat)
    
    print("\n[전체 로드맵: 초창기(저비용), 중간(커뮤니티), 수익화(고가 상품)]")
    print("예상 수익: 오디언스 " + audience_size + " 기준, 초창기 월 100만원 가능 (GlobeNewswire 코치 팁).")

if __name__ == "__main__":
    monetization_consulting()