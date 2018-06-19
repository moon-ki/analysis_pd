import pandas as pd

#Series와 dict 데이터를 사용한 DataFrame
# d = {
#     'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#     'two': pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}
#
# df = pd.DataFrame(d)
# print(df)

#list와 dict를 활용
d2 = [
    {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 20, 'phone': '010-2222-2222'},
    {'name': '길동', 'age': 30, 'phone': '010-3333-3333'}]

df = pd.DataFrame(d2)
print(df)

df2=pd.DataFrame(df,columns=['name','phone'])
print(df2)

#데이터 추가(열추가)
df2['height'] = [150, 160, 170]
print(df2)

#인덱스 선택
df3=df2.set_index('name')
print(df3)

#컬럼선택
s=df2['name']
print('컬럼선택!!!:',s)

print('merge')
#merge
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)

print('merge & join')
#merge & join
#공통열인 '고객번호'를 기준으로 데이터를 조인하여 출력한다.
#기본적으로, 양쪽 데이터프로엠에 모두 키가 존재하는 데이터만 합쳐진다.
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

print(pd.merge(df1, df2,how='left'))

#기준열은 on 인수로 명시적 설정이 가능하다.
print('기준열 명시(on)')
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

print(pd.merge(df1, df2,on='성별'))
