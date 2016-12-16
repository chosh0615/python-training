import pandas as pd

def 표범위목록구하기(프레임):
    시작목록 = list(프레임[프레임.notnull().sum(1) == 1].index)
    끝목록 = 시작목록[1:] + [len(프레임)]    
    return list(zip(시작목록, 끝목록))

def 지표추출(경로):    
    프레임 = pd.read_excel(
        경로, skiprows=3, parse_cols='C:K', header=None)
    프레임 = 프레임.dropna(how='all')
    프레임 = 프레임.reset_index(drop=True)
    
    표범위목록 = 표범위목록구하기(프레임)
    표목록 = []
    for 범위 in 표범위목록:
        시작, 끝 = 범위
        if 끝 - 시작 < 2:
            continue
        표 = 프레임[시작:끝]
        표목록.append(표)
    return 표목록

def 엑셀로내보내기(표목록, 파일명):
    엑셀파일 = pd.ExcelWriter(파일명)

    for i, 표 in enumerate(표목록):        
        표.to_excel(엑셀파일, '지표 {}'.format(i+1))

    엑셀파일.save()