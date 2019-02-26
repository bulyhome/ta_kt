import os.path

def get_test_scenarios(filename):
    """
    Parser for the PKG_contents files
    :param filename: PKG_contents filename
    :return:    - list of tuples (/usr/asm/atl.0000/ZX/ZX_CC_free_text.test_scenario.xml, ASML-BB-040-0200A, ZX).
                - empty list is returned in case file cannot be opened or the argument is invalid
    """
    result = []
    test_w_path = ''
    comp = ''
    if os.path.isfile(filename):
        try:
            with open(filename) as f:
                for line in f:
                    if '.test_scenario.xml' in line:
                        if 'atl.0000' in line:
                            test_w_path = line.split()[0]
                            comp = test_w_path.split('/')[-1].split('_')[0]
                        else:
                            bb = '-'.join(line.split()[0].split('-')[:4])
                            result.append((test_w_path, bb, comp))
        except BaseException:
            print("Log: Could not open file")
    return result


def check_all_tests(l):
    """
    Validate the format of the name for *test_scenario.xml
    :param l: list of tuples (/usr/asm/atl.0000/ZX/ZX_CC_free_text.test_scenario.xml, ASML-BB-040-0200A, ZX).
    :return: True / False. For empty list True is returned. For invalid argument, False is returned
    """
    allowed_comp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    allowed_level = ['FC', 'BB', 'CC', 'SY', 'UT']
    if not isinstance(l, list): return False
    for i in l:
        test_w_path = i[0]
        testname = test_w_path.split('/')[-1]
        if '.test_scenario.xml' not in testname: return False
        testname_short_list = testname.replace('.test_scenario.xml', '').split('_')
        if len(testname_short_list) < 3: return False
        comp = testname_short_list[0]
        for c in comp:
            if c not in allowed_comp: return False
        test_level = testname_short_list[1]
        if test_level not in allowed_level: return False
    return True
