import pytest
import os

if __name__ == '__main__':
    pytest.main()
    # os.system("pytest --alluredir=output")
    os.system("allure generate output -o report --clean")
    #os.system("allure open report")

