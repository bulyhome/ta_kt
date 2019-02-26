import ta
import re


pkg_path = "PKG_contents_0"

if __name__ == '__main__':
    # result_list = ta.get_test_scenarios(pkg_path)
    # final_result = 'OK' if ta.check_all_tests(result_list) else 'NOK'
    # print(final_result)

    filename = 'ZX_CC_free_text.test_scenario.xml'
    match_obj = re.match(r'^([A-Z0-9]+)_(FC|BB|CC|SY|UT)_(.*).test_scenario.xml$', filename)
    if match_obj:
        print(match_obj.group(1))
        print(match_obj.group(2))
        print(match_obj.group(3))
