# 내장 스킬과 앱 연동

2.1.0부터 market-news-radar, world-memory-autopilot, evidence-first-portfolio-advisor는 이 플러그인의 skills/ 아래에 함께 포함된다. 외부 설치본이 없어도 해당 형제 디렉터리의 SKILL.md와 참고 자료를 읽는다. portfolio-ledger-maintenance는 포함하지 않는다. .app.json에는 Alpaca, Wolfram, Binance, Exa, 공식 Notion 앱을 선언한다. 선언은 현재 세션의 인증·도구 노출·Python 실행 가능성을 보장하지 않는다. 사용 직전에 실제 가용성을 확인한다.

## ChatGPT 실행 경계

실제 ChatGPT 세션에 Python 실행, 필요한 네트워크 및 패키지 설치, 요청된 내장 차트 기능이 있어야 해당 계산 경로를 실행할 수 있다. 스킬을 내장했다고 없는 실행 기능을 흉내 내지 않는다. 실행할 수 없는 계산만 중단하고 도구로 직접 검증한 근거와 한계를 제공한다. 세 스킬은 근거와 계산을 제공하며, 하영 모드의 최종 설명은 하영의 어조로 작성하되 World Memory의 링크 우선·쓰기 결과 계약은 보존한다.

## Binance와 Exa

Binance는 요청과 관련된 암호화폐 시장 관측에, Exa는 출처 탐색과 원문 수집에 사용한다. Exa가 노출되지 않았으면 호출한 척하지 않는다. 검색 결과와 원문 확인 상태를 구분하고 각 스킬의 근거 규칙을 따른다. World Memory 0.17.0은 publisher-web-search.md의 6개 매체 검색을 기본으로 하며, Market News Radar의 별도 RSS 수집 정책으로 덮어쓰지 않는다. Binance 데이터를 포트폴리오 검증기가 지원하지 않는 입력으로 끼워 넣거나 World Memory의 검증된 공급자 계획에 추가하지 않는다. Binance와 Alpaca 연결은 시장 데이터 분석용이며 이 플러그인은 주문·취소·이체·자동매매를 실행하지 않는다.


## 가용성 판정

필요한 기능마다 `available`, `unavailable`, `unknown` 중 하나로 판정한다. 현재 컨텍스트의 스킬 목록이나 실제 호출 가능한 도구가 증거다. `unknown`을 설치됨이나 호출 가능으로 추정하지 않는다. 스킬 설치와 플러그인·커넥터 연결은 별도 상태다.

스킬이 필요하지만 없으면 실행한 척하지 말고 기능 제한과 아래 정확한 설치 후보를 사용자에게 알린다. 자동 설치는 사용자의 명시적 요청이 있을 때만 가능하다.

| 내부 스킬 | 정본 저장소 |
|---|---|
| `$evidence-first-portfolio-advisor` | `https://github.com/devninjadev/PortfolioAnalysisSkillChatGPT` |
| `$world-memory-autopilot` | `https://github.com/devninjadev/WorldMemoryLite` |
| `$market-news-radar` | `https://github.com/devninjadev/market-news-radar` |

## Evidence-first Portfolio Advisor

핵심 경로는 필요한 실행 기능을 제공하는 ChatGPT 환경과 Python 런타임, 스킬의 검증된 CLI와 Yahoo Finance/yfinance다.

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
