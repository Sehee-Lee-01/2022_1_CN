# 2022_1_CN
To study Computer Network of 1st semester

## 중간고사 대체 프로젝트

- 소켓 통신을 활용하여 Server, Client 프로그램 작성
  * 프로그래밍 언어는 C, Java, Python 으로 구현

- TCP 기반 소켓프로그래밍 작성후 
   Client에서는 HTTP 프로토콜의 GET/HEAD/POST/PUT Request를 요청하고
   Server에서는 Client의 Request에따라 응답 메시지를 구성하여 Response하도록 구현
   (TCP 기반 Client, Server 구현한 프로그램 파일을 제출)
   * 예) Method-응답 xxx의 case 5개 이상 수행.
      GET-응답 4xx, GET-응답 2xxx, HEAD-응답 1xx, POST-응답 2xxx, POST-응답 1xx 등
   * 소켓 통신은 PC가 2대 이상이면 Client, Server 실행은 분리하여 진행을 권장
      2대 이상 환경이 안되는 경우는 localhost로 진행도 가능

* 제출: 소스파일과 Readme 파일(*.txt, 워드파일 등) 을 작성하여 제출 

## 과제

와이어샤크로 DNS, TCP 인 경우에 메시지를 캡쳐하여 분석 

1) 웹사이트 접속후 메뉴 클릭, 검색창에 키워드 입력을 수행하거나 명령어창에서 nslookup 웹사이트(www.naver.com 등)을 진행한다. 와이어사크에서 DNS query and response 메시지를 캡쳐하고 메시지를 분석하여 설명한다.

2) 와이어사크에서 TCP인 경우를 캡쳐하여 TCP Segment의 format을 분석하여 설명하시오. 캡쳐한 TCP의 헤더 정보(sequence number, ack number, Flag, Reserved 값 등 확인)에 저장된 값을 분석하여 정리한다.   

제출: PPT 파일을 작성하여 제출  
제출일정 : 5월20일(금)

