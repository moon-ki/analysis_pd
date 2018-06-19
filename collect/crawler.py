from .api import api
import json

# 전처리 프로세스: 원하는 포멧으로 데이터 전처리
#============================================================================================================
def preprocess_foreign_visitor(data):
    data['country_code']=data['natCd']
    data['contry_name']=data['natKorNm'].replace(' ','')
    data['date'] = data['ym']
    data['visit_count'] = data['num']
    del data['natCd']
    del data['natKorNm']
    del data['ym']
    del data['num']
    del data['ed']
    del data['edCd']
    del data['rnum']
    # print('crawler.preprocess_foreign_visitor:',type(data), data)
    return data

def preprocess_tourspot_visitor(post):

    # if  post['csForCnt'] :
    post['count_forigner'] = post['csForCnt']
    # if  post['csNatCnt']:
    post['count_locals'] = post['csNatCnt']

    post['tourist_spot'] = post['resNm'].replace(' ','')
    post['date'] = post['ym']
    post['restrict1'] = post['sido']
    post['restrict2'] = post['gungu']
    del post['csForCnt']
    del post['csNatCnt']
    del post['resNm']
    del post['ym']
    del post['sido']
    del post['gungu']
    del post['addrCd']
    del post['rnum']
#============================================================================================================


# Crawling: 제공하는 API를 활용해 data를 가져오고, 파일로 떨어뜨리는 기능
#============================================================================================================
def crawling_tourspot_visitor(restrict1, restrict2='',start_year='', end_year='', fetch=False, result_directory='', service_key=''):
    result=[]
    fileName= '%s/%s_touris_%s_%s.json' % (result_directory,restrict1,start_year,end_year) #"서울특별시_tourist_2017_2017.json"
    # print('filename:',filename)

    if fetch:
        for year in range(start_year,end_year+1):    # 년도 range
            for month in range(1,13):        # 월   range
                for posts in api.pd_fetch_tourspot_visitor(YM='{0:04d}{1:02d}'.format(year, month),
                                                           SIDO=restrict1,
                                                           GUNGU=restrict2,
                                                           service_key=service_key):
                    for post in posts:
                        preprocess_tourspot_visitor(post)
                    result+=posts

        # File Export 하기!
        with open(fileName, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(result, indent=4,sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)
    return fileName

def crawling_foreign_visitor(contryCode, start_year, end_year, fetch, result_directory, service_key):
    result=[]
    fileName = '%s/%s(%s)_foreignVisitor_%s_%s.json' % (result_directory, contryCode[0], contryCode[1], start_year, end_year)
    if fetch:
        for year in range(start_year,end_year+1):
            for month in range(1,13):

                for data in api.pd_fetch_foreign_visitor(YM='{0:04d}{1:02d}'.format(year, month),
                                                         ED_CD='E',# 방문객구분 (D: 국민 해외 관광객,  E: 방한 해외 관광객)
                                                         NAT_CD=contryCode[1],
                                                         service_key=service_key):
                    data = preprocess_foreign_visitor(data)
                    result.append(data)

        # print(type(data),data)
        # contryName=data['contry_name']
        # fileName='%s/%s(%s)_foreignVisitor_%s_%s.json' % (result_directory,contryName,contryCode,start_year,end_year)
        print('fileName:',fileName)

        with open(fileName, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(result, indent=4,sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return fileName
#============================================================================================================