import matplotlib.pyplot as plt

def graph_scatter(result_analysis):
    # result_analysis = [{'x':[....], 'y':[....], 'contry_name':'중국', 'r': 0.xxxx},
    #                    {'x':[....], 'y':[....], 'contry_name':'일본', 'r': 0.xxxx},
    #                    {'x':[....], 'y':[....], 'contry_name':'미국', 'r': 0.xxxx} ]
    # 1. subplots 선언
    fig, subplots =plt.subplots(1, len(result_analysis), sharey=True) #sharey=True: y축을 공유시킨다.

    # 2.
    for index, result in enumerate(result_analysis):# enumerate: index와 함께 리스트를 리턴하는 함수
        # index별 x축 라벨
        subplots[index].set_xlabel('{0}인 입국자수'.format(result['contry_name']))
        #공유할 y축 라벨
        index==0 and subplots[index].set_ylabel('관광지 입장객 수')
        # index별 title을 소수점 5자리 처리하여 셋팅
        subplots[index].set_title('r={:.5f}'.format(result['r']))#.5f 소수점 5자리수
        #그래프 셋팅
        subplots[index].scatter(
            result['x'],
            result['y'],
            c='black',  #점색
            s=6         #점크기
        )
    plt.subplots_adjust(wspace=0) # 그래프간 간격조정
    plt.show()
