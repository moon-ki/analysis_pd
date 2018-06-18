import collect

items = [
    {'restrict1': '서울특별시', 'restrict2':'','since':2017, 'until':2017}
]
for item in items :
    collect.crawling_tourspot_visitor(**item)

# for country in [('중국', 112), ('일본', 130), ('미국', 275)] :
#         collect.crawling_foreign_visitor(country[1], 2017, 2017)
