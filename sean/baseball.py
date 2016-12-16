import pandas as pd

def from_files(files):
    시즌프레임 = []
    for 경로 in files:
        프레임 = pd.read_excel(경로)
        프레임 = 프레임.set_index('선수명')
        프레임 = 프레임[['안타', '홈런', '타석']]
        시즌프레임.append(프레임)
    return 시즌프레임