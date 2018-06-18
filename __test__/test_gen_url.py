from collect.api import api

url=api.pd_fetch_foreign_visitor(YM='{0:04d}{1:02d}'.format(2017, 1),
                                 NAT_CD='112',
                                 ED_CD='E'
                                 )
