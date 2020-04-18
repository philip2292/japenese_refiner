'''
일본어 데이터 정제
오상혁 나윤수
2020.4.1 수 샘플 생성
'''

import sys

text=sys.argv[1]
sample_num=sys.argv[2]
save_point=sys.argv[3]
#입력 오류 대처
if len(sys.argv)!=4:
    print('대상 텍스트 파일과 샘플의 문장 수 저장 위치를 입력해주세요')
    raise ValueError

text=open(text,'r',encoding='utf-8')
# 텍스트 파일을 list형식으로 읽어오기
text_list = text.readlines()

# 전체 파일에서 샘플 데이터 출력
sample_list = []
len_data = len(text_list)
sample_num=int(sample_num)
sample_count = round(len_data/sample_num)
for i in range(len_data):
    if i % sample_count == 0:
        sample_list.append(text_list[i])

# list 형식을 str 형식의 파일로 변환
sample_str = ''.join(sample_list)

#파일 저장
write_text=open(save_point,'w',encoding='utf-8')
write_text.write(sample_str)
