import unittest
import os.path

from boa3.boa3 import Boa3
from boa3_test.test_drive.testrunner.neo_test_runner import NeoTestRunner

PROJECT_PATH = os.sep.join(os.path.dirname(__file__).split(os.sep)[:-1])

class TestHelloWorld(unittest.TestCase):
    neoxp_config_file = PROJECT_PATH + '/default.neo-express'
    smart_contract_root_folder = PROJECT_PATH + '/smart_contracts'
    smart_contract_path = PROJECT_PATH + '/smart_contracts/hello_world.py'
    nef_path = smart_contract_path.replace('.py', '.nef')

    runner: NeoTestRunner = None

    @classmethod
    def setUpClass(cls):
        Boa3.compile_and_save(cls.smart_contract_path)
        cls.runner = NeoTestRunner(cls.neoxp_config_file)

    def test_method(self):
        pass

if __name__ == '__main__':
    unittest.main()
