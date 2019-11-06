from junitparser import TestCase, TestSuite, JUnitXml, Skipped, Error

# Create cases
case1 = TestCase('case1')
case1.result = Skipped()
case2 = TestCase('case2')
case2.result = Error('Example error message', 'the_error_type')

# Create suite and add cases
suite = TestSuite('suite1')
suite.add_property('build', '55')
suite.add_testcase(case1)
suite.add_testcase(case2)
suite.remove_testcase(case2)

# Add suite to JunitXml
xml = JUnitXml()
xml.add_testsuite(suite)
xml.write('C:/Users/RAG/Desktop/venky-python/junit.xml')