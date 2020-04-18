'''
일본어 데이터 정제
오상혁 나윤수
2020.4.1 수
데이터 정제 메인 코드
[텍스트 파일명 입력]
정제할 텍스트 파일명을 입력
[저장 위치 및 파일 명]
파일 이름 및 경로를 설정 할 수 있습니다

'''
import sys
from good_sentence import *
from bad_sentence import *
from preprocessing import *
import time

#입력 오류 대처
if len(sys.argv)<3 or len(sys.argv)> 5:
    print('------------------------------------------------------------------------')
    print('다음과 같은 형식으로 입력해주세요')
    print(' 예) [파일명] [저장 위치 및 저장할 파일 명]')
    print('     text.txt    c:/work/fine_data.txt')
    print('------------------------------------------------------------------------')
    raise ValueError

#입력값 받기
file=sys.argv[1]
text_name=sys.argv[2]
min_range=sys.argv[3]
max_range=sys.argv[4]
#텍스트 불러오기
text=open(file,'r',encoding='utf-8')
text_str=''.join(text)
t1=time.time()

#인풋데이터 수정
preprocess=prepro(text_str)
t2=time.time()
print('인풋 데이터 수정 완료','걸린시간:',round(t2-t1),'초')
t3=time.time()

#안좋은 문장 제거
bad_sentence_file=bad(preprocess)
t4=time.time()
print('안 좋은 문장 제거 완료','걸린시간:',round(t4-t3),'초')
t5=time.time()

#좋은 문장 정리
good_sentence_file=good(bad_sentence_file,min_range,max_range)
t6=time.time()
print('좋은 문장 설정 완료','걸린시간:',round(t6-t5),'초')
t7=time.time()

#문장길이 오름차순 정렬
text_sort=good_sentence_file.split('\n')
text_sort_len=text_sort.sort(key=len)
str_len='\n'.join(text_sort)
t8=time.time()
print('문장 길이 오름차순 정렬 완료','걸린시간:',round(t8-t7),'초')

#파일 저장
t9=time.time()
write_text=open(text_name,'w',encoding='utf-8')
write_text.write(str_len)
t10=time.time()
print('저장 완료','걸린시간:',round(t10-t9),'초')


