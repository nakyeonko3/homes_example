# 파이썬 실행 환경

- 가상 환경 venv
- formater
- linter

# 블로킹

바운드 현상에 의해 코드 실행이 멈추 게 되는 현상

- cpu 바운드
  cpu의 연산 속도에 의해 프로그램 실행 속도가 제한 되는 것

- io 바운드
  네트워크 IO 바운드
  네트워크 서버 응답 때가지 시간이 걸림.

# 논블로킹

바운드에 의해 코드 실행이 멈추지 않는 것

# 동기 vs 비동기

코드가 작성 순서대로 실행 되지 않음
비순차적
요청 응답에 적절함
코루틴
async await
자바스크립트의 async await도 마찬가지로 비동기로 동작하고
await는 해당 코드가 비동기 코드의 실행 순서를 결정해준다.

- 비동기 코드가 위와 같은 블로킹 현상을 나름대로 해결해준다.

# 파이썬의 코루틴 : 서브루틴, 코루틴, 메인루틴

비동기 코드들은 코루틴으로 실행된다.

- 코루틴
  다양한 진입점과 다양한 탈출점이 있음

  - 어웨이터블 객체에만 await을 쓸수 있음
  - 어웨이터블 객체: 테스크, 코루틴, 퓨처

- 서브 루틴
  하나의 진입점과 하나의 탈춤점이 있음.

# 세션

서버와 통신을 연결을 유지 하는 것.

# 파이썬 코루틴 활용

## 언패킹, 패킹

https://wikidocs.net/22801

```python
result = await asyncio.gather(*[fetcher(session, url) for url in urls])
```

# 컴퓨터 구조

- 컴퓨터의 구성 요소
  입출력 장치
  cpu
  주메모리, 보조메모리
  시스템버스

- 운영체제
  설계한 이상으로 프로그램을 설계 가능하게 해줌
  컴퓨터 시스템을 운영하고 관리하는 프로그램

- 프로세스
  프로그램: 정적 상태의 코드들, 보조메모리에 저장되어 있음
  프로세스: 동적인 상태, 실행되고 있는 프로그램. 주 메모리에 올라와서 작업이 실행되는 상태
  스레드:
  - 프로세스 내에서 처리하는 여러 작업의 단위
  - 하나 망가지면 전체 프로세스에 영향을 끼침

# 동시성 vs 병렬성

- 동시성
  한 번에 여러개의 작업을 동시에 **스위칭**하면서 처리함.
  하나의 장치 안에서 여러개의 작업을 스위칭 하면서 진행함.

- 병렬성
  한 번에 여러개의 작업을 **병렬적**으로 처리함.
  여러개의 스레드에 각각 다른 일을 부여해서 일을 병렬적으로 진행함.

- 파이썬에서는 병렬성이 안된다.
- 파이썬 병렬성은 메모리 부하가 있다.

- threading.get_ident()
- executor = ThreadPoolExecutor(max_workers=15)

- GIL
- 멀티 프로세싱

# 파이썬 멀티 프로세싱, 멀티 스레딩, 비동기

io 바운드에서는 멀티 스레딩이 의미가 있지만
cpu 바운드에서는 멀티 스레딩이 별로임.
유휴 상태가 거의 없기 때문에 동시성을 사용하는 느낌이 별로 없다.

강의 다 듣고 정리하는 편이 나을듯

# 에러 기록

---

## TypeError: 'type' object does not support the asynchronous context manager protocol

- aiohttp.ClientSession가 아니라 aiohttp.ClientSession()가 되어야 함
- 괄호가 안 붙어서 객체가 아래 코드 처럼 type으로만 인식된다.

```python
    async with aiohttp.ClientSession as session:
TypeError: 'type' object does not support the asynchronous context manager protocol
>>> import aiohtpp
>>> aiohttp.ClientSession
<class 'aiohttp.client.ClientSession'>
```

# 질문

---

어떻게 하면 어떤 부분이 공부가 부족한지 알 수 있을까?

보기 쉽게 자료 정리 하는 법


# 궁금한 것들

---

- **파이썬 멀티 프로세싱, 멀티 스레딩, 비동기**
  이부분은 직접 파이썬으로 웹서버 많이 만들어보고.
  인공지능 프로그램도 돌려보고 해봐야 될 것 같다.

- python session
  연결 상태를 유지함
  https://reqbin.com/code/python/9ooszjzg/python-requests-session-example

  https://requests.readthedocs.io/en/latest/user/advanced/

  연결 상태를 유지하기 때문에 핸드쉐이크 비용이 덜 발생함

- keep alive

- HTTP 영구 연결
  https://en.wikipedia.org/wiki/HTTP_persistent_connection

- javascript의 비동기, await, fetch 실행 순서들

```javascript
async function getWaifuImgUrl() {
  const response = await fetch("https://api.waifu.pics/sfw/waifu");
  const message = await response.json();
  console.log("getWaifuImgUrl()");
  return message.url;
}
```

- PATH 환경 변수

- python
  sys.set_int_max_str_digits(0)?

- 종속성 관리

- poetry
