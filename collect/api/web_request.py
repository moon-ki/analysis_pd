from urllib.request import Request, urlopen
from datetime import *
import sys
import json

# def print_error(e):
#     print('%s %s' % (e, datetime.now()), file=sys.stderr)
# html_request(url="http://naver.com", encoding="utf-8")
################################################################################################
def html_request(url='',
                 encoding='utf-8',
                 success=None,
                 # error=print_error,
                 error=lambda e:print('%s %s' % (e, datetime.now()), file=sys.stderr)) :
    try:
        # url = "http://www.naver.com"
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding)

        print("%s : success for request[%s]" % (datetime.now(), url))

        if callable(success) is False: #호출할 수 있는 함수가 아닌가?
            return html
        # else:
        success(html)

    except Exception as e:
        if callable(error) is True:# 아무것도 안주면 디폴트는 file=sys.stdout 이다.
            error(e)

################################################################################################
def json_request(url='',
                 encoding='utf-8',
                 success=None,
                 # error=print_error,
                 error=lambda e:print('%s %s' % (e, datetime.now()), file=sys.stderr)) :
    try:
        # url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
        request = Request(url)
        resp = urlopen(request)
        result = resp.read().decode(encoding)

        json_result = json.loads(result)
        print("%s : success for request[%s]" % (datetime.now(), url))

        if callable(success) is False: #호출할 수 있는 함수가 아닌가?
            # print('json을 호출할 수 없음')
            return json_result
        # else:
        # print("외부에서 함수를 호출합니다.")
        success(json_result)
    except Exception as e:
        if callable(error) is True:
            error(e)
        else:
            print('%s %s' % (e, datetime.now()), file=sys.stderr)

def result_print(result):
    print(result)
    print('사용자 출력함수를 사용합니다.')
def error_print(e):
    print(e)
    print('사용자 에러함수를 사용합니다.')
################################################################################################
# json_request(url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list',
#              success=result_print,
#              error=error_print)