import unittest

from . import tests_models
from . import tests_views


test_suite = unittest.TestSuite()
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(tests_models))
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(tests_views))

# Запуск тестов
unittest.TextTestRunner().run(test_suite)
