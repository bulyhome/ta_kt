import unittest
import ta


class TestTA(unittest.TestCase):
    def test_gettestscenarios(self):
        # check the case where there is no matching test
        result_valid = []
        self.assertListEqual(ta.get_test_scenarios('PKG_contents_0'), result_valid)

        # check the case where there are 3 tests
        result_valid = [
            ('/usr/asm/atl.0000/HWWE/tstpkg/HWWE_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWE'),
            ('/usr/asm/atl.0000/HWWQ/tstpkg/HWWQ_UT_unit_tester.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWQ'),
            ('/usr/asm/atl.0000/HWWZ/tstpkg/HWWZ_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWZ')]
        self.assertListEqual(ta.get_test_scenarios('PKG_contents_3'), result_valid)

        # check the case where there are 2163 tests
        result_valid = 2163
        self.assertEqual(len(ta.get_test_scenarios('PKG_contents_2163')), result_valid)

        # check the case for invalid argument - number
        result_valid = []
        self.assertListEqual(ta.get_test_scenarios(123), result_valid)

        # check the case for invalid argument - True
        result_valid = []
        self.assertListEqual(ta.get_test_scenarios(True), result_valid)

        # check the case for invalid argument - file does not exist
        result_valid = []
        self.assertListEqual(ta.get_test_scenarios('PKG_contents_123'), result_valid)

    def test_checkalltests(self):
        # check the case where a valid list is provided
        input_list = [
            ('/usr/asm/atl.0000/HWWE/tstpkg/HWWE_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWE'),
            ('/usr/asm/atl.0000/HWWQ/tstpkg/HWWQ_UT_unit_tester.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWQ'),
            ('/usr/asm/atl.0000/HWWZ/tstpkg/HWWZ_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWZ')]
        self.assertTrue(ta.check_all_tests(input_list))

        # check the case where an empty list is provided
        input_list = []
        self.assertTrue(ta.check_all_tests(input_list))

        # check the case where invalid input - number is provided
        input_list = 1
        self.assertFalse(ta.check_all_tests(input_list))

        # check the case where invalid input - True is provided
        input_list = True
        self.assertFalse(ta.check_all_tests(input_list))

        # check the case where wrong component is provided
        input_list = [
            ('/usr/asm/atl.0000/HWWE/tstpkg/HWWe_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWE'),
            ('/usr/asm/atl.0000/HWWQ/tstpkg/HWWQ_UT_unit_tester.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWQ'),
            ('/usr/asm/atl.0000/HWWZ/tstpkg/HWWZ_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWZ')]
        self.assertFalse(ta.check_all_tests(input_list))

        # check the case where wrong test level is provided
        input_list = [
            ('/usr/asm/atl.0000/HWWE/tstpkg/HWWE_CQ_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWE'),
            ('/usr/asm/atl.0000/HWWQ/tstpkg/HWWQ_UT_unit_tester.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWQ'),
            ('/usr/asm/atl.0000/HWWZ/tstpkg/HWWZ_CC_autotest.test_scenario.xml', 'ASML-BB-001-0017A', 'HWWZ')]
        self.assertFalse(ta.check_all_tests(input_list))




if __name__ == '__main__':
    unittest.main()