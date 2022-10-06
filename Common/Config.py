import configparser

# from TestScripts.TestPyTest import setGlobalParam


class Config:
    aa_url = ""
    aca_url = ""
    browser_type = ""
    min_timeout = 0
    max_timeout = 0
    mid_timeout = 0
    timeout_type = ""
    project_path = ""
    testdata_path = ""
    document_path = ""
    agency = ""
    aa_user = ""
    aa_pwd = ""
    aca_user = ""
    aca_pwd = ""
    log_level = 0
    headless = False

    # Read the configuration properties and store them so they can be referred as required.
    def __init__(self):
        """
        Constructor
        """
    def set_config_values(self, set_global_param):
        obj_config = configparser.ConfigParser()

        obj_config.read('..\\Config.Properties')
        Config.agency = obj_config.get("Application", "Agency")
        Config.aa_url = obj_config.get("Application", "AAURL")
        Config.aca_url = obj_config.get("Application", "ACAURL")
        Config.aa_user = obj_config.get("Application", "AAUserID")
        Config.aa_pwd = obj_config.get("Application", "AAPwd")
        Config.aca_user = obj_config.get("Application", "ACAUserID")
        Config.aca_pwd = obj_config.get("Application", "ACAPwd")
        Config.browser_type = obj_config.get("Environment", "BrowserType")
        Config.headless = obj_config.get("Environment", "Headless")
        Config.min_timeout = obj_config.get("Timeout", "MinTimeOut")
        Config.mid_timeout = obj_config.get("Timeout", "MidTimeOut")
        Config.max_timeout = obj_config.get("Timeout", "MaxTimeOut")
        Config.timeout_type = obj_config.get("Timeout", "TimeoutType")
        Config.project_path = obj_config.get("Path", "ProjectFolderPath")
        Config.testdata_path = obj_config.get("Path", "TestDataPath")
        Config.log_level = obj_config.get("Logs", "LogLevel")

        if Config.browser_type == "Ie":
            Config.document_path = obj_config.get("Path", "DocumentPathIE")
        elif Config.browser_type == "Chrome":
            Config.document_path = obj_config.get("Path", "DocumentPathChrome")