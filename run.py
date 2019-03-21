# -*- coding: utf-8 -*-
# @Date    : 2018-08-11 15:34:37
# @Author  : Victor
from suite import testsuite
# 运行指定文件中的测试类
from test_case import test_login,test_streetlight

cases = [
test_login.requsetsTest,
test_streetlight.StreetLightTest
    # ,test_login.Testlogin
    # ,test_del_patient.del_patient
]


if __name__ == '__main__':
    # 调试、不生成报告
    # testsuite.run_case(cases)
    # 调试 运行cases中类里面的test_* 方法 生成报告
    # run_case.run_this_case('n', cases)

    # # 运行case文件夹内所有单元测试 生成报告
    testsuite.create_report('y')
    # 发送邮件
    # send_email()
