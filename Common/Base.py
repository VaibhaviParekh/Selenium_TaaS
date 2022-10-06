from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from Common import Config
from selenium import webdriver


class Base:

    obj_driver = None
    obj_driver_aca = None
    obj_config = Config.Config()

    def __init__(self):
        """        Constructor         """

    # Set up the driver according to the settings in configuration properties.
    # Open the application URL as specified in the Configuration settings.
    def open_url(self, url=None):
        if Base.obj_config.headless == 'True':
            if Base.obj_config.browser_type == "Firefox":
                options = FirefoxOptions()
                options.add_argument("--headless")
                self.obj_driver = webdriver.Firefox(options=options, executable_path="..\\geckodriver.exe")
            elif Base.obj_config.browser_type == "Chrome":
                options = ChromeOptions()
                options.add_argument("--headless")
                self.obj_driver = webdriver.Chrome("..\\chromedriver.exe", options=options)
        else:
            if Base.obj_config.browser_type == "Firefox":
                self.obj_driver = webdriver.Firefox(executable_path="..\\geckodriver.exe")
            elif Base.obj_config.browser_type == "Ie":
                ieCapabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
                ieCapabilities["nativeEvents"] = False
                ieCapabilities["unexpectedAlertBehaviour"] = "accept"
                ieCapabilities["ignoreProtectedModeSettings"] = True
                ieCapabilities["disable-popup-blocking"] = True
                ieCapabilities["enablePersistentHover"] = True
                ieCapabilities["ignoreZoomSetting"] = True
                self.obj_driver = webdriver.Ie("..\\IEDriverServer.exe", desired_capabilities=ieCapabilities)
            elif Base.obj_config.browser_type == "Chrome":
                self.obj_driver = webdriver.Chrome("..\\chromedriver.exe")
            elif Base.obj_config.browser_type == "PhantomJS":
                self.obj_driver = webdriver.PhantomJS("..\\phantomjs.exe")
            else:
                self.obj_driver = webdriver.Chrome("..\\chromedriver.exe")

        if Base.obj_config.timeout_type == "Max":
            self.obj_driver.implicitly_wait(int(Base.obj_config.max_timeout))
        elif Base.obj_config.timeout_type == "Mid":
            self.obj_driver.implicitly_wait(int(Base.obj_config.mid_timeout))
        else:
            self.obj_driver.implicitly_wait(int(Base.obj_config.min_timeout))

        if url is None:
            self.obj_driver.get(Base.obj_config.aa_url)

            self.obj_driver.maximize_window()

    def open_url_aca(self, url=None):
        if Base.obj_config.headless == 'True':
            if Base.obj_config.browser_type == "Firefox":
                options = FirefoxOptions()
                options.add_argument("--headless")
                self.obj_driver_aca = webdriver.Firefox(options=options, executable_path="..\\geckodriver.exe")
            elif Base.obj_config.browser_type == "Chrome":
                options = ChromeOptions()
                options.add_argument("--headless")
                self.obj_driver_aca = webdriver.Chrome("..\\chromedriver.exe", options=options)
        else:
            if Base.obj_config.browser_type == "Firefox":
                self.obj_driver_aca = webdriver.Firefox(executable_path="..\\geckodriver.exe")
            elif Base.obj_config.browser_type == "Ie":
                self.obj_driver_aca = webdriver.Ie("..\\IEDriverServer.exe")
            elif Base.obj_config.browser_type == "Chrome":
                self.obj_driver_aca = webdriver.Chrome("..\\chromedriver.exe")
            elif Base.obj_config.browser_type == "PhantomJS":
                self.obj_driver_aca = webdriver.PhantomJS("..\\phantomjs.exe")
            else:
                self.obj_driver_aca = webdriver.Chrome("..\\chromedriver.exe")

        if Base.obj_config.timeout_type == "Max":
            self.obj_driver_aca.implicitly_wait(int(Base.obj_config.max_timeout))
        elif Base.obj_config.timeout_type == "Mid":
            self.obj_driver_aca.implicitly_wait(int(Base.obj_config.mid_timeout))
        else:
            self.obj_driver_aca.implicitly_wait(int(Base.obj_config.min_timeout))

        if url is None:
            self.obj_driver_aca.get(Base.obj_config.aca_url)

            self.obj_driver_aca.maximize_window()