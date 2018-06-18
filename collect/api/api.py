from urllib.parse import urlencode
from .web_request import json_request
import math

serviceKey='hrxMJxnrvisj57nkxxK95SWQ1i4D5F1RMgIsqgpJ0SqTEbU7cqBQhxaDPIyJ1qca3OqokFYrhufzh1%2F%2Fjoht9w%3D%3D'
#serviceKey='musIsiEIsEo1%2FQUXNqYMVuRCIZBV%2BDo2z2ZujkgZEt2Ti63cXqWdk82AeaouBRQcpA2IFG3mm4%2Br5wgNXM6z6w%3D%3D'
#serviceKey='%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D'

# URL 생성 공통모듈
#====================================================================================================================================
def pd_gen_url(
        endPoint,
        # _type='json',
        **params):# 딕셔너리형 가변인수
    return "%s?serviceKey=%s&_type=json&%s" % (endPoint, serviceKey,urlencode(params))
#====================================================================================================================================

# 데이터 gathering 모듈
#====================================================================================================================================
def pd_fetch_foreign_visitor(YM, NAT_CD, ED_CD):
    endPoint='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url=pd_gen_url(
        endPoint=endPoint,
        YM=YM,
        NAT_CD=NAT_CD,
        ED_CD=ED_CD
    )
    json_result = json_request(url=url)
    print(type(json_result),json_result)
    datas=json_result['response']['body']['items']['item']
    yield datas

def pd_fetch_tourspot_visitor(YM, SIDO, GUNGU='',RES_NM='',numOfRows=20):
    endPoint='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    #요청 prameter를 반영한 URL을 생성한다.
    hasNext = True
    currPageNo = 1
    while hasNext:
        url=pd_gen_url(# region='5%EC%9B%94',
                       endPoint=endPoint,
                       YM=YM,
                       SIDO=SIDO,
                       GUNGU=GUNGU,
                       RES_NM=RES_NM,
                       numOfRows=numOfRows,
                       pageNo=currPageNo
                       # serviceKey=serviceKey
                       )

        json_result = json_request(url=url)

        #데이터 get
        posts = None if json_result is None else json_result['response']['body']['items']['item']
        totalCount= json_result['response']['body']['totalCount']
        numOfRows = json_result['response']['body']['numOfRows']
            #마지막페이지 구하기
        lastPage=math.ceil(totalCount/numOfRows)

        yield posts

        if lastPage==currPageNo:
            hasNext=False
        else:
            currPageNo+=1
#====================================================================================================================================