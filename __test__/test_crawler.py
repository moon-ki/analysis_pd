from collect import crawler as cw

# if __name__ =='__main__':
#     # print('analysis_fd 프로젝트 __main__ 실행')
#     items = [
#         {'restrict1': '서울특별시', 'since:':'2017', 'until':'2017'}
#     ]
#     for item in items :
#         # resultfile = \
#         cw.crawling(**item)

cw.crawling_foreign_visitor(112,2017,2017)
