# 백화점 애완 시설 예약 시스템, The pet

<!-- 목차 -->
<details>
  <summary>목차</summary>
  <ol>
    <li>
        <a href="#1-프로젝트-소개">프로젝트 소개</a>
        <ul>
            <li>1) 프로젝트 주제</li>
            <li>2) 서비스 개요 및 배경</li>
            <li>3) 서비스 목표</li>
        </ul>
    </li>
    <li>
        <a href="#2-서비스-기능-소개">서비스 기능 소개</a>
        <ul>
            <li>1) 메인 기능</li>
            <li>2) 서브 기능</li>
            <li>3) 관련 문서</li>
        </ul>
    </li>
    <li>
        <a href="#3-사용된-데이터셋과-기술스택">사용된 데이터셋과 기술스택</a>
        <ul>
            <li>1) 어떤 데이터셋을 어떻게 전처리하고 사용할것인지</li>
            <li>2) 어떤 방법, 라이브러리나 알고리즘을 사용할것인지</li>
        </ul>
    </li>
    <li>
        <a href="#4-시스템-아키텍쳐">시스템 아키텍쳐</a>
        <ul>
            <li>1) 개발 구조</li>
        </ul>
    </li>
    <li><a href="#5-프로젝트-팀원-소개">프로젝트 팀원 소개</a></li>
  </ol>
</details>

<h2 id="1-프로젝트-소개">1. 프로젝트 소개</h2>

---
### 1-1) 프로젝트 주제
‘FBI’는 여성용품 안전성과 과도한 다양성으로 여성용품 선택에 고전하는 소비자를 위해 상품 유사도를 기반으로 여성용품을 추천하는 서비스이다.

### 1-2) 서비스 개요 및 목표
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/be0af166-6ca7-4959-a437-d027e538c2f2/b3954dbc-24ef-4a5a-b9b1-f63277d12691/Untitled.png)
여성 헬스 케어 기업 [Monthly thing]에서 사용자와 상품의 데이터를 제공받고, 상품 간 유사도를 판별하여 사용자에게 새로운 상품을 추천한다. ‘FBI’는 여성용품을 항목화 하여, 여성 건강에 직결되는 상품의 안전성을 보장하고, 개개인에 맞는 상품 추천을 통해 건강한 소비를 돕는 것을 목표로 한다


* 주 사용자 : 먼슬리싱 사용자, 먼슬리싱 관리자

<h2 id="2-서비스-기능-소개">2. 서비스 기능 소개</h2>

---

### 2-1) 메인 기능
* 일반 사용자
  * 새로운 여성용품 정보를 입력한다.
  * 기존 상품과 유사하면 같은 상품으로 분류한다.
  * 전례 없는 상품 데이터로 판단되면, 태그 분류를 통해 특징을 추출한다.
● 특정 사용자에게 여성용품을 추천한다.

<h2 id="3-사용된-데이터셋과-기술스택">3. 사용된 데이터셋과 기술스택</h2>

### 3-1) 개발 일정
![개발 일정](https://github.com/user-attachments/assets/849f6dc7-267c-4554-b855-358fb1bbb18d)

<h2 id="4-사용된-데이터셋과-기술스택">4. 사용된 데이터셋과 기술스택</h2>


### 4-2) 기술 스택

| 파트                         | 기술                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Team** :metal:             | ![image](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) ![image](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) ![image](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white) ![image](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)                                                                                                                                                                                                                                                                                                                                                         |
| **Frontend** :ok_hand:             | ![image](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![image](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![image](https://img.shields.io/badge/jsp-007396?style=for-the-badge&logo=java&logoColor=white) |
| **Backend** :raised_back_of_hand: | ![image](https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white) ![image](https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white) |
| **Database** :raised_back_of_hand: | ![image](https://img.shields.io/badge/oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white) |
| **Tool** :metal: | ![image](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white) ![image](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) ![image](https://img.shields.io/badge/UML-007396?style=for-the-badge&logo=uml&logoColor=white) ![image](https://img.shields.io/badge/word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white) ![image](https://img.shields.io/badge/powerpoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white) ![image](https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white) |



<h2 id="4-시스템-아키텍쳐">4. 시스템 아키텍쳐</h2>

### 4-1) 개발 구조
![image](https://github.com/user-attachments/assets/f1e616bf-1b63-4c19-8f4f-3b4326c750c8)

### 4-2) 세부 과정
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/be0af166-6ca7-4959-a437-d027e538c2f2/5bb807d0-c71c-4474-884e-bad554567a19/Untitled.png)

### 4-3) 데이터 전처리 과정

### 4-4) 데이터 전처리 결과

### 4-5) 모델 세부 과정

### 4-3) 데이터 전처리 과정

### 4-4) 결과 화면

<h2 id="5-프로젝트-팀원-소개">5. 프로젝트 팀원 소개</h2>

| 이름   | 개발 기능 | 산출물 |
| ------ | --------- | ------ |
| 양석진 | 로그인, 회원가입, 관리자 예약 관리 | 프로젝트 기획서, 프로젝트 발표 자료, ERD |
| 박보선 | 예약 페이지, 메인 페이지 구성 | 시연 영상, ERD |
| 홍승아 | 알림 기능, 관리자 리뷰 관리 | 스토리보드, ERD |
| 조재룡 | 사용자 리뷰 관리 | 스토리보드, ERD |

