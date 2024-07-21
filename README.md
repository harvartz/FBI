# 여성용품 추천 시스템, FBI(Feminine product Based recommending algorIthm)

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
<p align="center">
  <img src="https://github.com/user-attachments/assets/311fcf7a-1302-42fc-97ac-b8f781b99cd5" alt="system architecture" style="width:70%;">
</p>
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
<p align="center">
<img src="https://github.com/user-attachments/assets/b55dd25b-f271-4229-8851-17bd731f5cdb">
</p>
<h2 id="4-사용된-데이터셋과-기술스택">4. 사용된 데이터셋과 기술스택</h2>


### 4-2) 기술 스택

### 4-2) 기술 스택

| 파트           | 기술                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stack**      | ![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![image](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| **Middleware** | ![image](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![image](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Tool**       | ![image](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![image](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) ![image](https://img.shields.io/badge/PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



<h2 id="4-시스템-아키텍쳐">4. 시스템 아키텍쳐</h2>

### 4-1) 개발 구조
<p align="center">
  <img src="https://github.com/user-attachments/assets/3a4bef16-132a-4ed7-a8dd-8394deb04592" alt="아키텍쳐" width="70%">
</p>

### 4-2) 세부 과정
<p align="center">
  <img src="https://github.com/user-attachments/assets/2043573e-0607-4682-9942-f4ba32bf68cd" alt="시스템 세부 과정" width="70%">
</p>

### 4-3) 모델 세부 과정
<p align="center">
  <img src="https://github.com/user-attachments/assets/dc9c2aec-c655-4d26-b1ac-482a295d1176" alt="모델 세부 과정" width="70%">
</p>

### 4-4) 결과 화면
<p align="center">
  <img src="https://github.com/user-attachments/assets/58c3cc27-21ad-4fa4-995f-4bd2df7de203" alt="결과 UI 화면" width="70%">
</p>



<h2 id="5-프로젝트-팀원-소개">5. 프로젝트 팀원 소개</h2>

| 이름   | 개발 분야 |
| ------ | --------- |
| 양석진 | Frontend, Data Modeling, Data Preprocessing, Text Mining |
| 신은지 | Backend, DB, Data Preprocessing, Text Mining |
| 최세화 | Data Architect, Data Preprocessing, Text Mining |


