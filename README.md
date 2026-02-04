# 🚗 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템

전국 자동차 등록 데이터를 기반으로  
자동차 등록 현황을 한눈에 파악하고,  
기업 FAQ를 쉽고 빠르게 검색·조회할 수 있는 서비스입니다.

---

## 📌 목차
- [프로젝트 개요](#-프로젝트-개요)
- [프로젝트 소개](#-프로젝트-소개)
- [팀 소개](#-팀-소개)
- [팀원 소개](#-팀원-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [시스템 아키텍처](#-시스템-아키텍처)
- [프로젝트 구조](#-프로젝트-구조)
- [실행 방법](#-실행-방법)
- [협업 규칙](#-협업-규칙)
- [문서 및 참고 자료](#-문서-및-참고-자료)

---

## 📖 프로젝트 개요
- **프로젝트명**: 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템  
- **프로젝트 기간**: YYYY.MM.DD ~ YYYY.MM.DD  
- **팀 구성**: 6명  
- **목적**:  
  - 전국 자동차 등록 현황 데이터를 효율적으로 제공  
  - 기업 FAQ 정보를 검색·조회할 수 있는 통합 시스템 구축  

---

## 📝 프로젝트 소개
본 프로젝트는 전국 자동차 등록 데이터를 수집·가공하여  
지역별, 차종별 자동차 등록 현황을 시각적으로 제공하고,  
기업에서 자주 묻는 질문(FAQ)을 손쉽게 검색할 수 있도록 돕는 시스템입니다.

데이터 기반의 정보 제공과  
사용자 친화적인 검색 경험을 목표로 합니다.

---

## 👥 팀 소개
> **팀명**: (팀명 입력)

저희 팀은 데이터 처리, 백엔드, 프론트엔드, 기획 역할을 나누어  
협업과 커뮤니케이션을 중요하게 생각하며 프로젝트를 진행하고 있습니다.

- 책임 있는 역할 분담
- 명확한 커뮤니케이션
- 기록을 통한 공유 문화 지향

---

## 🧑‍💻 팀원 소개

| 이름 | 역할 | 담당 업무 | GitHub |
|------|------|----------|--------|
| 박은지 | Frontend | UI/UX 구현 | https://github.com/ |
| 김지윤 | Data | 데이터 수집 및 전처리 | https://github.com/ |
| 박기은 | Backend | DB 설계 | https://github.com/ |
| 윤정연 | Frontend | 화면 구성 | https://github.com/ |
| 이창우 | PM | 기획 및 일정 관리 | https://github.com/ |
| 홍지윤 | Backend | API 설계 및 개발 | https://github.com/ |
---

## ✨ 주요 기능
- 전국 자동차 등록 현황 조회
- 지역별 / 차종별 통계 제공
- 기업 FAQ 검색 및 조회
- 키워드 기반 FAQ 검색 기능

---

## 🛠 기술 스택
- **Backend**: ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
!
- **Frontend**: ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) 
- **Database**: ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
- **Data**: Pandas  
- **Infra**: ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)


---

## 🏗 시스템 아키텍처
> (아키텍처 다이어그램 이미지 또는 설명 추가)

---

## 📂 프로젝트 구조
```bash
project-root/           
├── data/
│   ├── dump.sql              # 테이블 생성 및 데이터 동기화용 DB 쿼리
├── src/                      # 소스 코드 모듈
│   ├── __init__.py            
│   └── database.py           # DB 연결 로직
├── app.py                    # steamlit 메인 페이지 
├── requirements.txt          # 필요 라이브러리 목록
├── .gitignore                
└── README.md                 # 프로젝트 소개, 설치 및 실행 가이드
