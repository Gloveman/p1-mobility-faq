# SKN26-1st-3Team

---
## 👋🏻 팀 소개
### 📌 **Team 차곡차곡**

<table align="center">
  <tr>
    <td align="center" width="160px"><img src="./images/Leonardo.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./images/Bluebear.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./images/Katie.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./images/Tom Nook.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./images/Dotty.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./images/lsabelle.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
  </tr>
  <tr>
    <td align="center"><b>이창우</b></td>
    <td align="center"><b>김지윤</b></td>
    <td align="center"><b>박기은</b></td>
    <td align="center"><b>박은지</b></td>
    <td align="center"><b>윤정연</b></td>
    <td align="center"><b>홍지윤</b></td>
  </tr>
  <tr>
    <td align="center">PM/FULL STACK</td>
    <td align="center">FRONT</td>
    <td align="center">FRONT</td>
    <td align="center">DB/BACK</td>
    <td align="center">FRONT</td>
    <td align="center">DB/BACK</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Gloveman"><img src="https://img.shields.io/badge/Gloveman-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/JiyounKim-EllyKim"><img src="https://img.shields.io/badge/JiyounKim-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/gieun-Park"><img src="https://img.shields.io/badge/gieun--Park-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/lo1f0306"><img src="https://img.shields.io/badge/lo1f0306-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/dimolto3"><img src="https://img.shields.io/badge/dimolto3-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/jyh-skn"><img src="https://img.shields.io/badge/jyh--skn-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
  </tr>
</table>




---


## 🚗 목적지 주변 주차장&주유소 조회 시스템🚗

### 📌 개발 기간
2026.02.05 ~ 2026.02.06

### 📌 프로젝트 개요
공공데이터 기반의 MySQL 공간 쿼리를 활용해 목적지 반경 내 시설을 정밀하게 필터링하며, 
가격 변동이 잦은 주유소 정보는 실시간 API로 정확성을 높였습니다. 
지도 시각화와 카드 UI를 통해 복잡한 검색 과정 없이 직관적인 모빌리티 환경을 제공합니다.

### 📌 프로젝트 내용
1️⃣ **장소 기반 주차장 & 주유소 검색 및 시각화**
- 사용자의 검색 의도에 맞춰 정보를 파악할 수 있는 직관적인 모빌리티 탐색 환경을 제공
- 사용자가 입력한 장소 또는 주소의 좌표를 분석하여, 해당 위치 반경 내의 정보를 조회
- 주차장과 주유소 정보를 동시에 제공하여 최신성과 안정성을 확보
- 실시간 위치 추적 없이도 원하는 장소 주변 상황을 미리 탐색해 볼 수 있어 사용자 편의성을 높임
- 방대한 양의 데이터를 지도 마커와 카드를 활용하여 한눈에 파악할 수 있도록 구현

2️⃣ **공공데이터 Open API 수집 및 가공**
- 신뢰성 높은 공공기관의 데이터를 활용하여 프로젝트에 데이터셋을 구축
- 공공데이터 Open API를 통해 전국의 주유소 및 주차장 정보 수집
- 수집한 주차장 데이터를 프로젝트용 DB에 적재하여, API 호출 없이 시스템 내에서 독립적으로 데이터 핸들링 가능하도록 설계
- 주유소 정보는 실시간 API 호출을 활용하여 변동성 있는 가격의 정확성을 높임

3️⃣ **MySQL 인프라 구축 및 공간 데이터 활용** 
- 대량의 데이터를 효율적으로 관리하고 정교한 위치 기반 필터링을 수행할 수 있는 백엔드 구조를 실현
- 수집한 수만 건에 달하는 주차장 공공데이터를 MySQL 환경에 안정적으로 구축
- 위도와 경도 데이터를 활용한 공간 쿼리를 작성하여 사용자가 지정한 위치에서 정확한 거리 내에 있는 정보만을 추출하는 고정밀 필터링 프로세스를 구현
- 프로젝트 활용 목적에 맞는 핵심 데이터만을 선별하여 시스템의 효율성을 높임

 


---

## 📝 데이터 베이스(ERD)
<img src="images/ERD.png" width="500" alt="ERD">

---
## 📂 프로젝트 설계
```bash
project-root/           
├── data/
│   └── create_table.sql              # 테이블 생성 용 DB 쿼리
├── images/                           # Streamlit 페이지들   
├── pages/                            # README 프로필 이미지
│   ├── 01_entry_page.py              # main page
│   ├── 02_nearby_parkinglots.py      # 목적지 주변 주차장 조회 페이지
│   ├── 03_category_parkinglots.py  # 지역별 주차장 조회 페이지
│   ├── 04_search_gas_station.py      # 검색 장소 주변 주유소 조회 페이지
│   └── 05_search_parking_gas.py      # 주차장 & 주유소 통합 조회 페이지
├── prototype/                        # 실험적 기능 작성용
├── src/                              # 소스 코드 모듈
│   ├── __init__.py            
│   ├── API_Gas.ipynb                 # 주유소 api 테스트용 notebook
│   ├── collect_data.py               # parking_lot db 적재
│   ├── config.py                     # env 파일에서 db 연결 정보, API key 등 불러오기
│   ├── db_crud.py                    # mysql DB와 통신
│   ├── model.py                      # DB entity class 및 파싱용 class들 
│   └── utils.py                      # API 호출 등 유틸 함수 모음
├── app.py                            # Streamlit main 진입점 
├── requirements.txt                  # 필요 라이브러리 목록
├── .gitignore                
└── README.md                         # 프로젝트 소개 페이지
```

---
## 🛠️ 기술 스택
- **Backend**: ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **Frontend**: ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) 
- **Database**: ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
- **Data:** ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
- **Infra**: ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)


## ✅수행 결과
### Home화면
<img width="1800" height="900" alt="image" src="https://github.com/user-attachments/assets/f15e1087-711b-440d-b0ab-f687b1ce1ed4" />

### 주차장 조회 화면 
<img width="1800" height="900" alt="image" src="https://github.com/user-attachments/assets/a5a90d7c-132b-4e6f-b1aa-c6c09da41b2c" />

### 지도에 표출되는 마커 정보와 카카오 맵 연동
<img width="1800" height="900" alt="image" src="https://github.com/user-attachments/assets/2e7df91a-19a2-408d-ba16-b88cc3ce20cd" />

### 주유소 조회 화면
<img width="1902" height="904" alt="image" src="https://github.com/user-attachments/assets/d2c2e411-32c8-46a2-b7ac-b1fc05cf3848" />

### 주차장과 주유소 통합 조회 화면
<img width="1880" height="906" alt="image" src="https://github.com/user-attachments/assets/e5bd57cf-f5ad-4385-940e-10c9ff964529" />

---
## 🫱🏻‍🫲🏻팀원 회고

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">이창우</td>
            <td style="text-align: center; border: 1px solid #ddd;">김지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 전반을 깊이 이해하고 주도적으로 이끌어 주셨으며, 초반 시스템 구축을 거의 혼자 담당해 주신 덕분에 전반적으로 완성도 높은 결과물을 도출할 수 있었습니다. 또한 해결이 쉽지 않은 부분들을 도맡아 주셔서 프로젝트가 원활하게 진행되는 데 큰 기여를 해주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박기은</td>
            <td style="border: 1px solid #ddd; padding: 10px;">전체적인 코드 구조 설계와 백엔드 구현을 책임감 있게 맡아주셨습니다. 오류나 이슈가 발생했을 때도 빠르게 원인을 파악해 해결해 주셨습니다. 기술적인 부분에서 신뢰할 수 있는 팀원일 뿐만 아니라 프로젝트 전반의 안정성을 높여준 핵심적인 역할을 해주셨다고 생각합니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박은지</td>
            <td style="border: 1px solid #ddd; padding: 10px;">팀의 중심이 되어 프로젝트 전반을 책임져 주셨습니다. 꼼꼼한 일 처리와 팀원들의 고충을 해결해 주시는 모습에 큰 신뢰를 느꼈습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 전반의 기틀을 잡고 팀원들을 이끌어 주신 덕분에 프로젝트를 수월하게 진행할 수 있었습니다. 수많은 오류 수정과 DB 구현까지 도맡아 하신 우리 조의 주축이셨으며, 핵심적인 역할을 수행해 주신 덕분에 짧은 시간 내에 완성도 높은 결과를 낼 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">홍지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 전반에 대한 이해와 기술적인 구현 및 정교한 작업을 도맡아 진행해주셨습니다. 특히 다른 사람들의 소스 내용도 깊이 이해하시고, 내용을 모두 파악하고 계시는 부분이 인상깊었습니다. 프로젝트의 가장 처음이었던 프로토 타입부터, 매일 가장 마지막까지 코드가 잘 구동되는지 확인 작업을 하시는 부분에서 큰 책임감을 느꼈습니다.</td>
        </tr>
    </tbody>
</table>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">김지윤</td>
            <td style="text-align: center; border: 1px solid #ddd;">이창우</td>
            <td style="border: 1px solid #ddd; padding: 10px;">pandas를 활용해 보신 경험으로 지역별 주차장 조회 페이지를 만들어 주셨고, 이후 주차장 조회와 주유소 조회를 합친 ‘통합 페이지’ 구현에도 많은 시간을 들여 성공해내시는 모습을 보여주셨습니다. 또한 테스트 과정에서 생긴 여러 버그들과 개선 사항을 빠르게 고쳐주셔서 프로젝트 유지 보수에 큰 도움을 주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박기은</td>
            <td style="border: 1px solid #ddd; padding: 10px;">스트림릿과 백엔드를 연동하는 과정에서 발생한 이슈들을 끝까지 해결해 주셨습니다. 문제 해결 능력이 뛰어나 프로젝트가 안정적으로 완성될 수 있었습니다. 기능 구현 과정에서도 의견을 적극적으로 공유해 주셔서 협업이 원활했습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박은지</td>
            <td style="border: 1px solid #ddd; padding: 10px;">뛰어난 코딩 실력으로 다수의 기능을 구현하셨습니다. 창의적인 아이디어 제안 덕분에 프로젝트의 완성도가 한층 높아졌습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">질문에 항상 친절하게 답해주시고, 끊임없이 할 일을 찾아 나서는 열정적인 모습 덕분에 팀원들 모두 자극을 받아 열심히 임할 수 있었습니다. 특히 구현하기 까다로운 기능들도 끝까지 포기하지 않고 해결해 내는 모습이 정말 대단하다고 생각했습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">홍지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">뛰어난 소통 능력으로 프로젝트 내내 분위기 환기와 함께 문제상황을 명확하게 정리하는데 항상 큰 도움을 받았습니다. 화면의 큰 축을 맡아 빠르게 화면을 구현하고 다양한 오류상황에 대해 대처하셔서 저희가 구상했던 다양한 목표들을 빨리 이룰 수 있었습니다.</td>
        </tr>
    </tbody>
</table>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">박기은</td>
            <td style="text-align: center; border: 1px solid #ddd;">이창우</td>
            <td style="border: 1px solid #ddd; padding: 10px;">각 페이지의 전체적인 UI 디자인을 맡아 주셨고,  프로젝트에서 구현된 여러 기능들을 직접 구현해 보시는 등 많은 노력을 해 주셨습니다. 또한 코드를 작성하는 동안 발표 자료를 잘 정리해 주셔서 시간을 많이 아낄 수 있었던 것 같습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">김지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">웹페이지 디자인과 PPT 제작을 담당해 주셨으며, 웹페이지 구조를 깔끔한 시안으로 정리해 주셔서 이를 바탕으로 Streamlit 화면을 수월하게 구축할 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박은지</td>
            <td style="border: 1px solid #ddd; padding: 10px;">팀의 미적 감각을 책임지며 완성도 높은 PPT를 제작해 주셨습니다. 디자인뿐만 아니라 코드 기여까지 해주신 다재다능한 팀원입니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">디자인 전반을 도맡아 하셨을 정도로 팀 내에서 가장 뛰어난 감각을 보여주셨습니다. 이슈 관리나 PPT 제작 등 세세한 부분까지 꼼꼼히 챙겨주신 덕분에 프로젝트가 한결 원활하게 진행될 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">홍지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">항상 테스트를 주도적으로 실행해주셔서 많은 에러를 찾아 프로그램의 완성도를 높일 수 있었습니다. 팀에서 심미적 안목이 높으셔서, 코드 수정 외에도 화면 디자인과 PPT 제작, 문서작업을 추가적으로 맡아주셔서 감사했습니다. 
        </tr>
    </tbody>
</table>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">박은지</td>
            <td style="text-align: center; border: 1px solid #ddd;">이창우</td>
            <td style="border: 1px solid #ddd; padding: 10px;">처음에는 코드 작성에 어려움이 있어 ERD 작성 등을 맡으셨는데, 이후 AI 도구를 활용하여 주유소 API를 직접 작성하고 페이지까지 만드시는 등 프로젝트에 많은 기여를 해 주셨습니다. 이후에도 프로젝트에 추가된 여러 유용한 기능들을 제안해 주셨고, 직접 구현해 보기도 하셨습니다. </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">김지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 전반에 적극적으로 나서 주도적인 역할을 수행하였으며, AI를 활용해 다양한 에러 상황을 빠르게 해결해 주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박기은</td>
            <td style="border: 1px solid #ddd; padding: 10px;">Streamlit 환경에서 오픈 API를 연동하여 실시간 데이터 조회 기능을 구현해주셨습니다. Llm언어 도움을 받아 스스로 구현해보려고 하는 모습이 책임감있게 느껴졌습니다. 시스템 구현 화면 녹화까지 마무리해주셔서 프로젝트 일정을 무리없이 소화할 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 기간 중 컨디션이 좋지 않으셨음에도 불구하고 열정적으로 참여해 주시는 모습이 정말 인상적이었습니다. 특히 최종 검수 단계에서 예리하게 여러 오류를 찾아내고 수정해 주신 덕분에 프로젝트의 완성도를 크게 높일 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">홍지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 구상회의에서부터 내용을 주도하시면서 프로젝트의 방향성을 잘 잡아주셨고, 오픈 API와의 실시간 연동을 통해, 프로젝트의 큰 축을 맡아주셨습니다. 또, 항상 코드의 에러사항을 누구보다 빠르게 잡아주시면서도, 세세한 부분까지 신경을 많이 써주셨습니다. </td>
        </tr>
    </tbody>
</table>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">윤정연</td>
            <td style="text-align: center; border: 1px solid #ddd;">이창우</td>
            <td style="border: 1px solid #ddd; padding: 10px;">test_app에 실험적인 기능들을 구현해 보셨습니다. 리스트 아래 페이지 번호로 넘기기와 같이 실제 페이지에 기능을 추가하는데 있어 많은 도움이 되었습니다. 또한 README 파일을 작성을 담당해 주셔서 코드 작성에 집중할 수 있었던 것 같습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">김지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">AI를 활용해 프로젝트에 필요한 기능을 구현해 주었으며, 전반적인 프로젝트 내용을 체계적이고 깔끔하게 정리해 주었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박기은</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 아이디어를 구체화하고 GitHub README를 체계적으로 정리해주셔서 프로젝트의 전반적인 흐름과 핵심 기능을 명확히 전달했습니다.
기획 이해도가 높고, 문서화를 통해 팀의 공통 인식을 형성하는 데 기여했습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박은지</td>
            <td style="border: 1px solid #ddd; padding: 10px;">묵묵히 본인의 역할을 수행하며 가독성 높은 README를 완성해 주셨습니다. 덕분에 프로젝트의 전체 흐름을 명확히 파악할 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">홍지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 구상 단계에서부터 다양한 아이디어로 프로젝트가 확장되는데 기여를 많이 해주셨습니다. 직접 아이디어를 소스에 구현하는 작업과 함께 프로젝트에 필요한 산출물 작성을 도맡아 해주셨습니다.</td>
        </tr>
    </tbody>
</table>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">홍지윤</td>
            <td style="text-align: center; border: 1px solid #ddd;">이창우</td>
            <td style="border: 1px solid #ddd; padding: 10px;">DB 설정과 데이터 적재 부분을 맡으셨는데, 로컬 환경이 아닌 클라우드 DB를 사용하여 데이터 동기화 문제를 생각하지 않아도 되었습니다. 또한 초반에 프로젝트 구조를 잡을 때 많은 도움을 주셨고, db 연결 정보나 API key를 불러오는 과정을 config 파일로 분리하는 등 미처 생각하지 못한 부분을 짚어주셔서 더욱 완성도 높은 프로젝트가 되었던 것 같습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">김지윤</td>
            <td style="border: 1px solid #ddd; padding: 10px;">데이터베이스를 구조적으로 잘 설계하고 꼼꼼하게 구축해 주셨고, 실행 중 발생한 오류에 대해서도 원인을 분석해 신속하게 해결하며 프로젝트 안정성에 크게 기여해 주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박기은</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 목적에 맞는 데이터를 선별하고 정제하여 실제 기능 구현에 바로 활용할 수 있도록 정리해 주셨습니다. 덕분에 데이터 기반 기능이 안정적으로 구현될 수 있었습니다. 또한 데이터 정리 과정에서 팀원들과 적극적으로 소통하며 필요한 형태로 데이터를 제공해 주셔서 개발 및 시각화 작업에 큰 도움이 되었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">박은지</td>
            <td style="border: 1px solid #ddd; padding: 10px;">탄탄한 데이터베이스 설계로 프로젝트의 토대를 마련해 주셨습니다. 파트를 가리지 않고 프론트엔드까지 적극 지원해주셔서 큰 힘이 되었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">가장 중요한 DB 구축 과정을 주도하고, 모르는 부분은 조원들에게 친절히 설명해 주셔서 빠른 시간 내에 성과를 낼 수 있었습니다. 관련 분야 경력자로서 중심을 잘 잡아주신 덕분에 팀원들 모두 믿음을 가지고 프로젝트에 몰입할 수 있었습니다. </td>
        </tr>
    </tbody>
</table>
