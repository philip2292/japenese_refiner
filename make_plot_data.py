'''
일본어 데이터 정제
오상혁 나윤수
2020.4.1 수 통계 데이터 및 그래프

최대값, 평균값, 적절한 문장 범위 선택 가능
'''

#
import numpy as np
import matplotlib.pyplot as plt
import sys

#입력 오류 대처
if len(sys.argv)!=3:
    print('대상 텍스트 파일과 원하는 통계 옵션을 선택해 주세요')
    print('통계 옵션은 최대값 출력 : max \t 평균값 출력 mean \n 적절한 길이 범위 : arrange \t 모든데이터 : all ')
    raise ValueError

text=sys.argv[1]
option=sys.argv[2]

#텍스트 불러오기
text=open(text,'r',encoding='utf-8')
text_list=text.readlines()
text_list.sort(key=len)

#문장 길이값 구하기 \n을 제외하기 위해 1을 뺌
list_len=[]
for i in text_list:
    list_len.append(len(i)-1)

#문장 길이값 구한것을 길이로 오름차순 정렬
sort_li_len=sorted(list_len)

#문장 길이값의 종류 구하기
set_li=set(sort_li_len)
list_set=list(set_li)
list_set.sort()


#딕셔너리 형식으로 만들기
result=dict()
for i in list_set:
    result[i]=sort_li_len.count(i)

#키값(문장길이 종류) 추출
key_list=[]
for i in result.keys():
    key_list.append(i)

#벨류값(문장길이 종류값의 합) 추출
value_list=[]
for i in result.values():
    value_list.append(i)

#최대값
max_len=max(key_list)
#평균
mean_len=np.mean(list_len)


#8분위한 전체 데이터의 첫번째 값
limit_min=round(mean_len/4)
#8분위한 전체 데이터의 8분위 값
limit_max=round(mean_len/4*7)
#평균과 가장 긴 문장의 차를 5등분한 값
limit_max_divide=round((max_len-mean_len)/5)

#최대값 표시
if option=='max':
    print('최대값은',max_len,'입니다')
    plt.plot(key_list,value_list)
    plt.axvline(x=max_len,color='red',linestyle='--')
    plt.xticks([max_len],size=15)
    plt.xlabel('lengths')
    plt.ylabel('amount')
    plt.show()
#평균값 표시
elif option=='mean':
    print('평균값은',mean_len,'입니다')
    plt.plot(key_list, value_list)
    plt.axvline(x=mean_len,color='red',linestyle='--')
    plt.xticks([mean_len],size=15)
    plt.xlabel('lengths')
    plt.ylabel('amount')
    plt.show()
#적정 범위 표시
elif option=='range':
    print('정제 설정 범위는',limit_min,'에서',limit_max_divide,'입니다')
    plt.plot(key_list, value_list)
    plt.axvline(x=limit_min,color='red',linestyle='--')
    plt.axvline(x=limit_max_divide,color='red',linestyle='--')
    plt.xticks([limit_min,limit_max_divide],size=15)
    plt.xlabel('lengths')
    plt.ylabel('amount')
    plt.show()
#전부 표시
elif option=='all':
    plt.plot(key_list, value_list)
    plt.axvline(x=max_len,color='red',linestyle='--')
    plt.axvline(x=limit_min,color='red',linestyle='--')
    plt.axvline(x=mean_len,color='red',linestyle='--')
    plt.axvline(x=limit_max_divide,color='red',linestyle='--')
    plt.xticks([max_len,mean_len,limit_min,limit_max_divide],size=15)
    plt.xlabel('lengths')
    plt.ylabel('amount')
    plt.show()
#예외 표시
else:
    print('max mean range all 중에 선택해 주세요')

