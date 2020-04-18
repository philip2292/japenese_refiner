'''
일본어 데이터 정제
오상혁 나윤수
2020.4.1 수 데이터 정제하는 코드
좋은 문장 선별
[한자로만 된 문장 제거]
문장에서 조사는 히라가나로만 작성됨
조사가 없는 문장은 비문일 확률이 높으므로
한자로만 되어있거나 가타카나로만 되어있는 문장 제거
[적절한 길이 이외 문장 제거]
너무 짧아서 문장 성분이 부족할거라 예상 되는 문장과
너무 길어서 사용 하기 힘든 문장 제거
'''
import re
def good(text,min=9,max=135):

    #한자로만 된 문장 제거
    sub_chinese_character= re.sub('\n[^あ-んア-ン]*\n','',text)
    #가타카나로만 되어있는 문장 제거
    sub_kata=re.sub('\n[ア-ンー]*\n','',sub_chinese_character)
    #입력받은 길이 이외의 문장 제거
    sub_kata_list=sub_kata.split('\n')

#최소값 제거
    min_list=[]
    min=int(min)
    for i in sub_kata_list:
        if len(i)>=min:
            min_list.append(i)

#최대값 제거
    max_list=[]
    max=int(max)
    for i in min_list:
        if len(i)<=max:
            max_list.append(i)

#str문으로 변경
    sub_len_long='\n'.join(max_list)
    return sub_len_long

