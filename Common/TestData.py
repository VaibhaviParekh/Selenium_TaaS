
import pandas

from Common import Config


class TestData:

    obj_config = Config.Config()

    def __init__(self):
        """ Constructor """

    def read_testdata(self, file_name, sheet_name):
        full_path = self.obj_config.testdata_path + file_name
        df = pandas.read_excel(full_path, sheet_name=sheet_name)

        return df
