#configuration
import os

CONFIG = {
    'district1' :'서울특별시',
    'countries':[('중국', 112), ('일본', 130), ('미국', 275)],
    'common':{
        'service_key':'hrxMJxnrvisj57nkxxK95SWQ1i4D5F1RMgIsqgpJ0SqTEbU7cqBQhxaDPIyJ1qca3OqokFYrhufzh1%2F%2Fjoht9w%3D%3D',
        'start_year':2017, #CONFIG['common'][start_year]
        'end_year':2017,
        'fetch': False,
        'result_directory':'__results__/crawling'
    }
}

if os.path.exists(CONFIG['common']['result_directory']) is False:
    print('create directory')
    os.makedirs(CONFIG['common']['result_directory'])