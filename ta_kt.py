import ta

pkg_path = "PKG_contents_3"

if __name__ == '__main__':
    result_list = ta.get_test_scenarios(pkg_path)
    final_result = 'OK' if ta.check_all_tests(result_list) else 'NOK'
    print(final_result)
