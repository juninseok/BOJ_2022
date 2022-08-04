# 해쉬 테이블 구현하기

table = list(0 for i in range(10))          # 해쉬 테이블을 for문과 list형식으로 만든다.
                                            # 이때의 10에는 원하고자하는 table의 size를 넣으면 된다.

def hash_function(key):                     # 입력된 key를 이용하여 해쉬코드를 즉 해쉬값을 나머지를 이용하는 division function을 이용하여 나타낸 함수이다.
    hash_key = ord(key)                     # 아스키 코드로 변환하는 ord() 함수를 이용하여 키 값이 문자열인 경우 아스키 코드로 변환하게 하여 나타낸다.
    return hash_key % 10                    # key를 table의 size로 나눈 나머지를 반환한다.

def hash_save(key,data):                    # 해쉬함수를 거쳐 도출된 해쉬 주소에 해당하는 데이터를 저장하는 함수이다.
    index = hash_function(key)              # 해쉬함수를 통해 도출한 값을 table의 index의 값으로 지정한다.
    table[index] = data                     # 리스트 접근 방식을 통해서 data를 해당 index에 저장한다.

def hash_print(key):
    index = hash_function(key)              # 해쉬함수를 통해 도출한 값을 table의 index의 값으로 지정한다.
    print(table[index])                     # 해당하는 table의 값을 꺼내온다.



