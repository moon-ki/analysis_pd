from collect import crawler as cw

#api.pd_fetch_tourspot_visitor 테스트
# result=[]
# for post in api.pd_fetch_tourspot_visitor( YM='{0:04d}{1:02d}'.format(2017, 1),
#                                            SIDO='서울특별시',
#                                            GUNGU='',
#                                            RES_NM='',
#                                            numOfRows=10
#                                            ):
#     result+=post
# print(type(result), result)

# if __name__ =='__main__':
    # print('analysis_fd 프로젝트 __main__ 실행')
items = [
    {'restrict1': '서울특별시', 'restrict2':'','since':2017, 'until':2017}
]
for item in items :
    cw.crawling(**item)