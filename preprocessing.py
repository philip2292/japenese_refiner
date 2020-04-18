'''
일본어 데이터 정제
오상혁 나윤수
2020.3.30 월 데이터 정제하는 코드
인풋데이터 정제 및 문장부호 정리
'''

import re
def prepro(text):
    # 문장기호 및 깨지는 공백문자 삭제
    sub_punc = re.sub('。|!|\?', '', text)
    sub_u3000=re.sub('　','',sub_punc)
    # 특수기호 〆를 しめ(시메)로 변경
    sub_sime = re.sub('〆', 'しめ', sub_u3000)

    return sub_sime
