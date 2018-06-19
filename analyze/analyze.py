import json
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import math

def analysis_correlation_by_tourspot(resultfiles):

    # 1-1.파일을 열어 해당 데이터를 json 객체로 반환(json 활용)
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8')as infile:
        json_data = json.loads(infile.read())
        print(json_data)

    # 1-2.json Frame으로 변환 (pandas 활용)
    tourspotVisitorTable = pd.DataFrame(json_data, columns=['date', 'tourist_spot', 'count_forigner'])

    # 1-3. 필터링을 위한, spot 객체 확보
    touristSpots = tourspotVisitorTable['tourist_spot'].unique()

    result=[]
    for touristSpot in touristSpots:
        tempTable = tourspotVisitorTable[tourspotVisitorTable['tourist_spot']==touristSpot]
        tempTable = tempTable.set_index('date')
        # print(tempTable)
        ###각각의 spot 별로 중국, 일본, 미국의 출입국 데이터와 merge시킨다.
        data = {}
        for filename in resultfiles['foreign_visitor']:

            # 2-1.파일을 열어 해당 데이터를 json 객체로 반환(json 활용)
            with open(filename, 'r', encoding='utf-8')as infile:
                json_data = json.loads(infile.read())

            # 2-2.데이터 Frame으로 변환 (pandas 활용)
            foreignVisitorTable = pd.DataFrame(json_data, columns=['date', 'contry_name', 'visit_count'])

            # 2-3. merge를 위한, foreignvisitor_table 테이블의 key 셋팅(date)
            foreignVisitorTable = foreignVisitorTable.set_index('date')

            # format: |date|tourist_spot|count_forigner|contry_name|visit_count|
            mergeTable=pd.merge(
                        tempTable,
                        foreignVisitorTable,
                        left_index=True, right_index=True)
            print(mergeTable)

            contryName = mergeTable['contry_name'].unique().item(0)

            # 상관계수 계산
            r = ss.pearsonr(mergeTable['visit_count'], mergeTable['count_forigner'] )[0]
            # r = analysis_correlation(mergeTable['count_forigner'], mergeTable['visit_count'])

            data['tourspot']= touristSpot
            indexNm='r_' + contryName
            data[indexNm]=r

        result.append(data)

    # print(result)
    return result


def analysis_correlation(resultfiles):

    # 1-1.파일을 열어 해당 데이터를 json 객체로 반환(json 활용)
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8')as infile:
        json_data = json.loads(infile.read())
        print(json_data)

    # 1-2.json데이터 Frame으로 변환 (pandas 활용)
    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_forigner', 'date', 'tourist_spot'])

    # 1-3.아래 쿼리와 같은 group by 연산하여 데이터 Frame으로 저장
    #select date,
    #       sum(count_forigner) as count_forigner
    #  from tourspotvisitor_table
    # group by date
    sum_tourspotvisitor_table = pd.DataFrame( tourspotvisitor_table.groupby('date')['count_forigner'].sum() )

    #외국인들의 방문자수 데이터 처리
    results=[]
    # resultfiles['foreign_visitor']는 리스트 형식으로 중국, 일본, 미국에 대한 파일path가 있음.
    for filename in resultfiles['foreign_visitor']:
        # 2-1.파일을 열어 해당 데이터를 json 객체로 반환(json 활용)
        with open(filename, 'r', encoding='utf-8')as infile:
            json_data = json.loads(infile.read())

        # 2-2.데이터 Frame으로 변환 (pandas 활용)
        foreignvisitor_table=pd.DataFrame(json_data,columns=['contry_name', 'date', 'visit_count'])

        # 2-3. merge를 위한, foreignvisitor_table 테이블의 key 셋팅(date)
        foreignvisitor_table = foreignvisitor_table.set_index('date')

        # 3-1 테이블 merge
        # select a.date,
        #        a.count_forigner,
        #        b.contry_name,
        #        b.visit_count
        #   from sum_tourspotvisitor_table a,
        #        foreignvisitor_table b
        #  where a.date = b.date

        merge_table = pd.merge(
                        sum_tourspotvisitor_table,
                        foreignvisitor_table,
                        left_index=True, right_index=True)

        print(merge_table)

        # 3-2 상관계수 구하여 그래프그리기 위한 데이터 셋생성: visit_count와 count_forigner 데이터가 서로 연관성이 있는지 분석한다.
        x = list(merge_table['visit_count'])
        y = list(merge_table['count_forigner'])

        contry_name = foreignvisitor_table['contry_name'].unique().item(0) # 중복을 제거하여 0번째 값을 가져온다.
        # r= ss.pearsonr(x,y)[0] #상관계수 아래와 같음
        r= correlation_coefficient(x,y)

        data= {'x':x, 'y':y, 'contry_name':contry_name, 'r':r}
        # {'x':[....], 'y':[....], 'contry_name':'중국 or 일본 or 미국', 'r': 0.29949666408732034}
        results.append(data)

        # merge_table['visit_count'].plot(kind='bar')
        # plt.show()

    # 3-3 x,y,r,contry_name의 dict 정보를 list로 묶어서 리턴
    return results

def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0
    return r








