from selenium import webdriver
import pyderman as dr
import os

class Imdb(webdriver.Chrome):
    def __init__(self, driver_path, teardown=False) -> None:
        dr.install(dr.chrome, file_directory=driver_path, overwrite=True, filename='chromedriver.exe', verbose=False)
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += ';'+self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()

    def enter_site(self):
        self.get()