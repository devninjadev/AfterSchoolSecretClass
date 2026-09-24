# After School Secret Class — 하영

**2.0부터 독립 스킬 배포에서 플러그인 배포로 전환했습니다.** 최하영 투자 페르소나 스킬 `choi-hayoung`을 플러그인 안에 포함하며, 플러그인 설정·아이콘·참조 문서·캐릭터 이미지·실행 스크립트를 함께 배포합니다. 사용자가 `@하영` 또는 `$choi-hayoung`을 호출하면, 고등학교 금융투자부의 부장인 하영이 근거 중심 투자 분석과 캐릭터 서사를 결합해 답합니다.

## 주요 기능

- `@하영`, `하영아`, `최하영 모드로`와 같은 명시적 호출
- 일반 금융 질문을 가로채지 않는 의미 기반 활성화 경계
- 세 개의 정본 First Message 중 재현 가능한 선택
- 실질적인 분석 요청에서는 긴 도입부 자동 생략
- 닫힌 LLM 라우팅 계약과 1회 복구 후 안전 폴백
- 사실·계산·해석·시나리오를 분리하는 투자 근거 계약
- World Memory 자동 읽기와 명시적 요청 없는 쓰기 금지
- 선택적 포트폴리오·시장뉴스·World Memory 스킬 연동
- 드러켄밀러·소로스를 대표 인용 정본으로 분리한 원출처 레지스트리
- 투자 쟁점과 맞닿는 대표 투자자 관점을 자동으로 불러와 현재 근거와 연결
- 일상적 캐릭터 대화에서는 자연스럽게 인용하되, 정확한 문구·시점·공개용 근거는 원문 검증
- 도구를 사용한 분석에서도 하영의 직접 대사는 자연스러운 구어체를 유지하고 지문·표·인용은 역할별 문체를 보존
- 명시적 요청이 있을 때만 캐릭터 시트를 기준으로 이미지 생성

## 설치 및 0.x에서 전환

[GitHub Release v2.0.0](https://github.com/devninjadev/AfterSchoolSecretClass/releases/tag/v2.0.0)에서 `after-school-secret-class-plugin-2.0.0.zip`과 체크섬 파일을 내려받습니다. ZIP은 스킬 단독 압축파일이 아니라, 루트에 `plugin.json`이 있는 완전한 플러그인 패키지입니다.

Plugin Creator에서 이 ZIP을 사용해 플러그인을 생성하거나, 편집 권한이 있는 동일한 패키지 ID의 기존 플러그인을 업데이트할 수 있습니다. 지원되는 설치·업데이트 흐름은 사용 중인 앱과 계정에 따라 다릅니다. ZIP을 개인 스킬 폴더에 그대로 풀어 넣는 0.x 설치 방식은 2.0의 기본 설치 방식이 아닙니다.

기존 사용자는 다음 순서로 전환합니다.

1. 플러그인 버전을 설치하고 내장 `choi-hayoung`이 표시되는지 확인합니다.
2. 별도 설치한 로컬 `choi-hayoung`은 비활성화해 중복 호출을 피합니다. 원본은 백업이나 수정용으로 보관할 수 있습니다.
3. 플러그인을 선택하고 `하영아` 또는 구체적인 분석 요청으로 호출합니다.

```text
하영아
@하영 엔비디아를 분석해 줘
하영이 방식으로 오늘 시장을 설명해 줘
```

기본 시작 문구는 `하영아`입니다. 실질적인 질문이 있으면 긴 도입부를 생략합니다. 로컬 원본과 플러그인은 독립된 사본이므로, 로컬 스킬을 수정해도 설치된 플러그인이 자동으로 갱신되지는 않습니다.

## 플러그인 구성

```text
plugin.json                    # 표준 플러그인 설정, 버전 2.0.0
.codex-plugin/plugin.json      # Codex 호환 설정
assets/gpt-icon.png            # 플러그인 아이콘
skills/choi-hayoung/           # 내장 스킬과 모든 참고 자료
scripts/build_plugin.py        # 패키지·체크섬 재생성
```

기존 캐릭터와 근거 중심 투자 분석 계약은 유지합니다. 새 기능의 추가보다는 **배포·설치 단위를 스킬에서 플러그인으로 바꾸는 메이저 업데이트**입니다. 외부 연동 스킬과 커넥터는 자동 설치되지 않습니다.

## 선택적 연동 스킬

필요한 스킬이 설치되지 않았을 때 하영은 실행한 척하지 않고 기능 제한과 설치 위치를 안내합니다.

| 내부 스킬 | 저장소 |
|---|---|
| `$evidence-first-portfolio-advisor` | [PortfolioAnalysisSkillChatGPT](https://github.com/devninjadev/PortfolioAnalysisSkillChatGPT) |
| `$world-memory-autopilot` | [WorldMemoryLite](https://github.com/devninjadev/WorldMemoryLite) |
| `$market-news-radar` | [market-news-radar](https://github.com/devninjadev/market-news-radar) |

관련 플러그인과 커넥터는 다음과 같습니다.

- **Alpaca:** 적격 미국 주식·암호화폐 가격 폴백, 시장 시계, ETF 시장 폭 확인
- **공식 Wolfram:** 후순위 가격·환율·미국 국채 근거
- **공식 Notion:** `notion-native-v2` World Memory 읽기 및 위임된 쓰기 작업

스킬 설치와 플러그인 연결은 별도 상태입니다. 도구가 없거나 상태가 불명확하면 `unknown` 또는 `unavailable`로 취급합니다.

## World Memory 주의사항

현재 패키지의 `references/world-memory-read-bridge.md`는 제작자가 승인한 개인 `notion-native-v2` Hub와 저장 뷰의 불변 위치에 바인딩되어 있습니다. 인증정보, 쿠키, OAuth 값은 포함하지 않지만 Notion 페이지·데이터소스·저장뷰 ID는 공개 소스에 포함됩니다.

다른 사용자가 설치할 경우 해당 브리지를 자신의 검증된 World Memory 저장소로 교체하거나 World Memory 연동을 비활성화해야 합니다. 제목 검색이나 추측으로 다른 Hub를 채택해서는 안 됩니다.

하영은 관련 투자 질문에서 World Memory를 자동으로 읽을 수 있지만, 다음 표현은 쓰기를 허가하지 않습니다.

```text
기억해 둬
참고해
다음에도 고려해
```

`월드메모리에 저장해`, `새 Story로 기록해`, `기존 가설을 갱신해`, `월드메모리 리포트를 실행해`처럼 명시적인 요청만 `$world-memory-autopilot`의 확인·쓰기 계약으로 진입할 수 있습니다.

## 검증 및 재패키징

```sh
python3 -m unittest discover -s skills/choi-hayoung/tests -p 'test_*.py'
python3 scripts/build_plugin.py
```

계약 테스트 19개와 패키지 검사를 사용합니다. 빌드 스크립트는 두 설정 파일의 이름·버전 일치, 아이콘 경로, 스킬 이름, 심볼릭 링크 제외, ZIP 무결성 및 패키지 파일의 원본 일치를 확인하고 SHA-256 체크섬을 생성합니다. 실제 대화 응답 및 선택적 외부 연동의 성공까지 보증하는 검사는 아닙니다.

## 버전

현재 GitHub 릴리즈: **`2.0.0` (플러그인)**

- `2.0.0`: 독립 스킬에서 플러그인으로 전환. 플러그인 설정·아이콘·내장 `choi-hayoung`을 완전한 ZIP으로 배포하고 기존 사용자 전환 안내를 추가했습니다.

전체 변경 내역은 [CHANGELOG.md](CHANGELOG.md)를 확인하세요.

- `0.9.2`: 도구 기반 분석에서도 하영의 직접 대사를 구어체로 유지하고, 관련 있는 드러켄밀러·소로스 관점을 현재 쟁점과 근거 사이에 자연스럽게 연결하도록 보강했습니다.
- `0.9.1`: 일상 대화의 인용 정책을 완화하고 하영의 대표 인용 정본을 드러켄밀러·소로스로 분리했습니다.
