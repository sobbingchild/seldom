# coding=utf-8
import os
import time
import logging
import unittest
from .HTML_test_runner import HTMLTestRunner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


pyse_str = """                            
 ______  __   __  _______  _______ 
|   _  ||  | |  ||  _____||   ____|
|  |_| ||  |_|  || |_____ |  |____ 
|   ___||_     _||_____  ||   ____|
|  |      |   |   _____| ||  |____ 
|__|      |___|  |_______||_______|
"""


def main(path=None,
         title="pyse Test Report",
         description="Test case execution",
         debug=False):
    """
    runner test case
    :param path:
    :param title:
    :param description:
    :param debug:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if debug is False:
        for filename in os.listdir(path):
            if filename == "reports":
                break
        else:
            os.mkdir(os.path.join(path, "reports"))

        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        report = os.path.join(path, "reports", now + "_result.html")

        with(open(report, 'wb')) as fp:
            tests = unittest.defaultTestLoader.discover(path, pattern='test*.py')
            runner = HTMLTestRunner(stream=fp, title=title, description=description)
            print(pyse_str)
            runner.run(tests)
    else:
        tests = unittest.defaultTestLoader.discover(path, pattern='test*.py')
        runner = unittest.TextTestRunner(verbosity=2)
        logger.info("pyse run test 🛫🛫!")
        print(pyse_str)
        runner.run(tests)
        logger.info("End of the test 🔚!")


if __name__ == '__main__':
    main()

