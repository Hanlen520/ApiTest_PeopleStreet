import requests
from util.test_star_end import TestStarEnd
from  util.modules import ddt
from  config import root_path
from util.gettestdata import get_testcase
from util.modules.HTMLTestRunner_API import set_response,set_data
from config import host
from common.get_token import get_token

case_path = root_path + '\\data\\streetlight_data.xlsx'

light_data = get_testcase(case_path, "streetlight", '智能路灯')
# casedata = get_testcase(case_path, 2, '智能路灯')
token = get_token()
print(token)

@ddt.ddt
class StreetLightTest(TestStarEnd):


    @ddt.data(*light_data)
    def test_addGetway(self, light_data):
        url=host+light_data['url']
        print(url)
        params=light_data['body']
        method=light_data['method']
        asserts=light_data['asserts']
        header = {'Content-Type': 'application/x-www-form-urlencoded',
                  "token":token}
        r = requests.post(url,params,headers=header)
        response=r.text
        set_response(response)
        print(requests)

if __name__=="__main__":
    print("")