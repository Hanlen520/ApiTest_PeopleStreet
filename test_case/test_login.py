import requests
import json
import unittest
from util.test_star_end import TestStarEnd
from util.modules import ddt
from config import root_path
from util.gettestdata import get_testcase
from util.modules.HTMLTestRunner_API import set_response, set_data
from config import host

case_path = root_path + '\\data\\case.xlsx'
# casedata = get_testcase(case_path, 1, '登录')
casedata = get_testcase(case_path, "login", '登录')
print(casedata)


@ddt.ddt
class requsetsTest(TestStarEnd):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}

    @ddt.data(*casedata)
    def test_login(self, casedata):
        url = host + casedata['url']
        params = casedata['body']
        method = casedata['method']
        asserts = casedata['asserts']

        r = requests.post(url, params, headers=self.header)
        response = r.text
        set_response(response)

    # def test_get_token(self):
    #     data = {"loginName": "admin", "password": "123456", "type": "01"}
    #     r = requests.post(host + "/provider/user/bsUser/login", data, headers=self.header)
    #     respon = r.text
    #     print(respon)
    #     token = json.loads(respon)['data']['token']
    #     return token


if __name__ == "__main__":
   print("11")