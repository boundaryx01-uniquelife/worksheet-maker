# worksheet-maker

모의고사·학습지 메이커 모음.

- `app/` 영재원 모의고사 메이커 (부산대 과학영재원 중등수학심화 대비)
  - `src/` 템플릿(`app_tpl.html`), 공통 CSS(`sheet.css`), 빌드(`build.py`)
  - `data/` 문제 은행 JSON (`bank_all.json` 30문항)
  - `tools/` 문제 작성·검증·페이지 수 보정 스크립트
  - `dist/math-bank3.html` 빌드 결과 (단일 HTML)
- `hub/` 모의고사 메이커 허브(`index.html`)와 목표별 페이지(`program-gifted.html`), 디자인 시안
- `standalone/` 모의고사 1회 단일 페이지

빌드: `app/src`에서 `python3 build.py` (같은 폴더의 json을 읽도록 경로 조정 필요).
출력: 게시 화면에서는 인쇄창이 막혀 있어 "출력용 파일 받기"로 HTML을 저장한 뒤 브라우저에서 인쇄합니다.
