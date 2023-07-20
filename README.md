# Django_project_myblog
## 음악 추천 공유 블로그

## 1. 목표
- 원래는 특정 기능 블로그를 만드는 것이지만 아직 생각하는 것을 원하는 만큼 구현하는데 한계가 있어서 기본 CRUD 구현을 목표로 했습니다.
- 이전에 만들었던 음악 추천 챗봇 서비스를 사용한 유저들끼리 정보를 공유하는 블로그를 목적으로 개발하였습니다. 


## 2. 개발 환경
- Django 4.2.3
- Python 3.11.2
- HTML, CSS, Javascript


## 3.프로젝트 구조와 개발 일정
- 프로젝트 구조
```
myblog
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── templates
│   ├── base.html
│   └── index.html
├── user
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── venv
```
- 개발 일정
  - 개발 기간 : 7월 17일 ~ 7월 20일


## 4. ERD
![Untitled](https://github.com/su0797/Django_project_myblog/assets/95666574/649e54ca-ece2-4f68-93c0-94643f3f5f51)


## 5. 주요 기능
- 회원 가입
- 로그인
- 로그아웃
- 게시물 작성
- 게시물 수정
- 게시물 삭제
- 게시물 검색
- 댓글 작성
- 댓글 삭제


## 6. URL

|URL|기능|
|---|---|
|'/'|메인페이지|
|'blog/'|게시글 전체 페이지|
|'blog/write/'|게시글 작성|
|'blog/detail/<int:pk>'|게시글 조회|
|'blog/edit/<int:pk>/'|게시글 수정|
|'blog/delete/<int:pk>/'|게시글 삭제|
|'blog/search/<str:tag>/'|게시글 검색|
|'user/join/'|회원가입|
|'user/login/'|로그인|
|'user/logout/'|로그아웃|


## 7. 화면
- 메인 페이지
<img width="1429" alt="스크린샷 2023-07-21 오전 1 47 41" src="https://github.com/su0797/Django_project_myblog/assets/95666574/68088b50-f27d-4f3c-aa47-8f10d14244bf">



- 로그인 
<img width="1425" alt="스크린샷 2023-07-21 오전 1 49 09" src="https://github.com/su0797/Django_project_myblog/assets/95666574/e0d8c943-3909-46ac-81c0-52cd7805c2ca">



- 회원가입 
<img width="1429" alt="스크린샷 2023-07-21 오전 1 50 39" src="https://github.com/su0797/Django_project_myblog/assets/95666574/88d6618f-5320-4f53-b1e9-0b730746d097">



- 게시판 메인 페이지
<img width="1428" alt="스크린샷 2023-07-21 오전 1 48 05" src="https://github.com/su0797/Django_project_myblog/assets/95666574/237b1e03-7509-4a89-a39e-d6249e599073">



- 게시글 작성
<img width="1429" alt="스크린샷 2023-07-21 오전 1 48 43" src="https://github.com/su0797/Django_project_myblog/assets/95666574/8ce38726-bcbb-4662-9923-a5467ea3e4dd">



- 게시글 수정
<img width="1427" alt="스크린샷 2023-07-21 오전 1 51 27" src="https://github.com/su0797/Django_project_myblog/assets/95666574/2f55a784-c123-4e8d-a913-96c935f6d9ee">



- 게시글 조회
<img width="1430" alt="스크린샷 2023-07-21 오전 1 51 06" src="https://github.com/su0797/Django_project_myblog/assets/95666574/802d53c4-6b77-47e1-977d-af19d564eaef">



- 게시글 검색
<img width="1429" alt="스크린샷 2023-07-21 오전 1 50 39" src="https://github.com/su0797/Django_project_myblog/assets/95666574/0ed48093-5d17-432a-b83a-3f3c97fb8443">



## 8. 추가 기능
- 전체적인 UI 수정
- 카테고리 세분화 후 검색기능 수정
- 이미지 업로드 기능
- 회원 관련 추가 기능 (비밀번로 변경, 프로필 수정, 닉네임 추가 등)


## 9. 개발하며 느낀점
- 혼자 장고를 이용해서 프로젝트를 처음 진행했는데 역시 예상했던 대로 프로젝트를 생성하고 앱을 만드는 다음 단계부터 조금씩 막혔습니다. 기초적인 부분부터 어려움이 생겨서 쉽지 않았지만 확실히 처음부터 직접 만들다 보니 부족한 부분들을 확실히 알게 되었고 공부를 어떻게 다시 해야 할지 방향성을 알 수 있었습니다.
아직 완성된 프로젝트가 아니니까 8번에 작성한 추가 기능들도 포함해서 아쉬운 부분들을 채우고 더 완성된 프로젝트로 만들겠습니다.


