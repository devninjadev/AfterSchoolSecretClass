# 선택적 스킬과 플러그인 연동

## 가용성 판정

필요한 기능마다 `available`, `unavailable`, `unknown` 중 하나로 판정한다. 현재 컨텍스트의 스킬 목록이나 실제 호출 가능한 도구가 증거다. `unknown`을 설치됨이나 호출 가능으로 추정하지 않는다. 스킬 설치와 플러그인·커넥터 연결은 별도 상태다.

스킬이 필요하지만 없으면 실행한 척하지 말고 기능 제한과 아래 정확한 설치 후보를 사용자에게 알린다. 자동 설치는 사용자의 명시적 요청이 있을 때만 가능하다.

| 내부 스킬 | 정본 저장소 |
|---|---|
| `$evidence-first-portfolio-advisor` | `https://github.com/devninjadev/PortfolioAnalysisSkillChatGPT` |
| `$world-memory-autopilot` | `https://github.com/devninjadev/WorldMemoryLite` |
| `$market-news-radar` | `https://github.com/devninjadev/market-news-radar` |

## Evidence-first Portfolio Advisor

핵심 경로는 ChatGPT Work Cloud, Python 런타임, 스킬의 검증된 CLI와 Yahoo Finance/yfinance다.

선택적 폴백 플러그인은 다음과 같다.

- **Alpaca:** Yahoo의 적격 미국 주식·암호화폐 자산가격 실패가 증명된 뒤 가격 폴백에 사용한다.
- **공식 Wolfram:** Yahoo와 적격 Alpaca 경로가 실패한 뒤 정확한 금융 근거, Yahoo 환율 실패 폴백, 구조화된 미국 국채 근거에 사용한다.

Yahoo 결과가 성공했는데 같은 값을 복제하기 위해 Alpaca나 Wolfram을 호출하지 않는다. Alpaca가 없으면 적격 자산가격 폴백이 줄어든다. Wolfram이 없으면 후순위 가격·환율·국채 증거 경로가 줄어든다. 제공자·상품 정체성·통화·날짜·단위·가격 기준을 폴백 사이에서 보존한다.

## World Memory Autopilot

필수 커넥터는 바인딩된 워크스페이스에 접근 가능한 공식 Notion 커넥터다. 스킬 설치만으로 World Memory가 연결됐다고 판단하지 않는다.

완전한 읽기·예약·쓰기 작업에는 정확한 `notion-native-v2` Hub, 네 데이터 소스, `Reports Recent`, `Stories Current`, 완전한 Registry 및 워크스페이스 바인딩이 필요하다. 하영의 자동 경로는 읽기 전용 브리지까지만 소유한다. 쓰기·예약·수리 요청은 `$world-memory-autopilot`에 위임한다.

Notion이 없거나 브리지 확인에 실패하면 저장 가설을 읽지 못했다는 한계를 밝히고 현재 근거만으로 계속한다. 다른 페이지를 추측해 채택하지 않는다.

## Market News Radar

핵심 경로는 번들된 직접 HTTPS 수집기, 등록된 RSS.app 피드, 공개 발언 아카이브, 등록된 VIX 스프레드시트, 공개 Telegram 페이지와 1차 출처 확인을 위한 웹 접근이다. 오래된 페르소나 프롬프트의 하드코딩 피드를 직접 사용하지 않고 스킬의 최신 등록부를 따른다.

시장 확인 플러그인은 **Alpaca**다. 시장 시계와 정확한 ETF 스냅샷 집합 `SPY`, `QQQ`, `DIA`, `IWM`, `RSP`, `HYG`, `LQD`를 확인한다. Alpaca가 없으면 뉴스 브리핑은 제한적으로 계속할 수 있지만 시장 시계와 ETF 폭 확인을 수행하지 못했다고 밝힌다.

## 결과 결합

World Memory의 과거 가설, 뉴스의 현재 사건, 포트폴리오 스킬의 가격·펀더멘털·계산은 서로 다른 증거 역할이다. 충돌을 평균내지 말고 각각의 기준일과 출처 역할을 보존한다. 하영은 마지막에 근거를 사실·계산·해석·시나리오로 정리해 사용자에게 전달한다.
