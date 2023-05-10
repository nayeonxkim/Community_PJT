# 커뮤니티 생성

- 목적 : DRF와 Vue를 사용하여 혼자 처음부터 끝까지 하나의 웹 프로젝트 완성하기
- 기능 : 게시글 CRUD, 댓글 CRUD, 회원가입 및 로그인/로그아웃

---

## 백엔드

### 프로젝트 구조

프로젝트 back

ㄴ articles 앱

ㄴ accounts 앱





### 프로젝트 준비

1. 가상환경 설치 및 활성화

2. django 3.2.18 설치 & django restframework 설치

3. django 프로젝트 `back` 시작





### articles 애플리케이션

1. articles 애플리케이션 생성 및 settings.py에 등록

2. `Article` 모델 생성

3. `Article` 모델 admin에 등록

4. `ArticleSerializer` 시리얼라이저 생성

5. urls.py에 articles 앱의 urls 분리

6. articles 앱 urls 생성





### Article CRUD

1. url 생성

2. views에 함수 정의
- api_view 데코레이터

- `Article` 모델에서 인스턴스 혹은 전체 받아오기

- `ArticleSerializer` 로 받아온 데이터 직렬화

- Response로 serializer.data JSON으로 내보내기
3. 포스트맨에서 확인
