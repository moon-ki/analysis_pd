import collect
from config import CONFIG
import analyze
import pandas as pd
import matplotlib.pyplot as plt

import visualize

#실행 부

if __name__=='__main__':

    resultfiles={}
    resultfiles['tourspot_visitor']=collect.crawling_tourspot_visitor(restrict1=CONFIG['district1'], **CONFIG['common'])

    resultfiles['foreign_visitor']=[]
    for country in CONFIG['countries'] :
        rf=collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    #1. analysis and visualize
    # result_analysis=analyze.analysis_correlation(resultfiles)
    # visualize.graph_scatter(result_analysis)

    #2. analysis and visualize
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    # 장소별로 상관계수를 구하여 그린다.
    #result_analysis는 아래와 같은 데이터 프레임
    #tourspot   r_중국   r_일본  r_미국
    # 경복궁     0.2     0.4     0.5
    # 컬럼이 많은경우
    graph_table = pd.DataFrame(result_analysis, columns=['tourspot','r_중국', 'r_일본', 'r_미국'])
    graph_table=graph_table.set_index('tourspot')
    graph_table.plot(kind='bar')
    #
    plt.show()