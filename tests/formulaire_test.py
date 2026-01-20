import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.ReadData import ReadData
from selenium.webdriver.edge.service import Service


class TestSendFormulaire(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        edge_service = Service(executable_path=r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe")
        #options.headless = False
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--remote-allow-origins=*")
        cls.driver = webdriver.Edge(service=edge_service, options=options)
        cls.driver = webdriver.Edge(options=options)
        cls.read_data = ReadData()
        cls.url = "https://sendform.nicepage.io/?version=13efcba7-1a49-45a5-9967-c2da8ebdd189&uid=f7bd60f0-34c8-40e3-8e2c-06cc19fcb730"
    
    def test_homme(self):
        client = self.read_data.read_data_from_json("Client1")
        driver = self.driver
        driver.get(self.url)
     #   import pdb; pdb.set_trace()
        driver.find_element(By.XPATH, "//*[@id=\"field-2688\"]").click()
        Select(driver.find_element(By.XPATH, "//*[@id=\"select-9648\"]")).select_by_visible_text("France")
        driver.find_element(By.XPATH, "//*[@id=\"name-c6a3\"]").send_keys(client.name)
        driver.find_element(By.XPATH, "//*[@id=\"email-c6a3\"]").send_keys(client.email)
        driver.find_element(By.XPATH, "//*[@id=\"phone-84d9\"]").send_keys(client.phone)
        driver.find_element(By.XPATH, "//*[@id=\"address-be2d\"]").send_keys(client.adresse)
        driver.find_element(By.XPATH, "//*[@id=\"message-c6a3\"]").send_keys(client.message)
        Select(driver.find_element(By.XPATH, "//*[@id=\"select-c283\"]")).select_by_visible_text(client.produit)
        driver.find_element(By.XPATH, "//*[@id=\"checkbox-8214\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"carousel_1853\"]/div/div/div/div/form/div[12]/a").submit()

    def test_femme(self):
        client = self.read_data.read_data_from_json("Client2")
        driver = self.driver
        driver.get(self.url)
       # import pdb; pdb.set_trace()
        driver.find_element(By.XPATH, "//*[@id=\"field-aa6c\"]").click()
        Select(driver.find_element(By.XPATH, "//*[@id=\"select-9648\"]")).select_by_visible_text("Espagne")
        driver.find_element(By.XPATH, "//*[@id=\"name-c6a3\"]").send_keys(client.name)
        driver.find_element(By.XPATH, "//*[@id=\"email-c6a3\"]").send_keys(client.email)
        driver.find_element(By.XPATH, "//*[@id=\"phone-84d9\"]").send_keys(client.phone)
        driver.find_element(By.XPATH, "//*[@id=\"address-be2d\"]").send_keys(client.adresse)
        driver.find_element(By.XPATH, "//*[@id=\"message-c6a3\"]").send_keys(client.message)
        Select(driver.find_element(By.XPATH, "//*[@id=\"select-c283\"]")).select_by_visible_text("Voiture")
        driver.find_element(By.XPATH, "//*[@id=\"carousel_1853\"]/div/div/div/div/form/div[10]/label").click()
        driver.find_element(By.XPATH, "//*[@id=\"carousel_1853\"]/div/div/div/div/form/div[12]/a").submit()

    def test_homme_condition(self):
        client = self.read_data.read_data_from_json("Client3")
        driver = self.driver
        driver.get(self.url)
        #import pdb; pdb.set_trace()
        genre = driver.find_element(By.ID, "field-2688")
        genre.click()
        select = Select(driver.find_element(By.ID, "select-9648"))
        select.select_by_visible_text("Italie")
        genre_value = genre.get_attribute("value")
        driver.find_element(By.XPATH, "//*[@id=\"name-c6a3\"]").send_keys(client.name)
        driver.find_element(By.XPATH, "//*[@id=\"email-c6a3\"]").send_keys(client.email)
        driver.find_element(By.XPATH, "//*[@id=\"phone-84d9\"]").send_keys(client.phone)
        driver.find_element(By.XPATH, "//*[@id=\"address-be2d\"]").send_keys(client.adresse)
        driver.find_element(By.XPATH, "//*[@id=\"message-c6a3\"]").send_keys(client.message)
        driver.execute_script("window.scrollBy(0, 300);")

        if genre_value == "man" and select.first_selected_option.text == "France":
            Select(driver.find_element(By.XPATH, "//*[@id=\"select-c283\"]")).select_by_visible_text("Moto")
            driver.find_element(By.XPATH, "//*[@id=\"checkbox-8214\"]").click()
        else:
            Select(driver.find_element(By.XPATH, "//*[@id=\"select-c283\"]")).select_by_visible_text("Vélo")
            driver.find_element(By.XPATH, "//*[@id=\"checkbox-1848\"]").click()

        driver.find_element(By.XPATH, "//*[@id='carousel_1853']/div/div/div/div/form/div[12]/a").submit()

    def test_femme_condition(self):
        client = self.read_data.read_data_from_json("Client4")
        driver = self.driver
        driver.get(self.url)
        #import pdb; pdb.set_trace()
        genre = driver.find_element(By.ID, "field-aa6c")
        genre.click()
        select = Select(driver.find_element(By.ID, "select-9648"))
        select.select_by_visible_text("France")
        genre_value = genre.get_attribute("value")
        driver.find_element(By.XPATH, "//*[@id=\"name-c6a3\"]").send_keys(client.name)
        driver.find_element(By.XPATH, "//*[@id=\"email-c6a3\"]").send_keys(client.email)
        driver.find_element(By.XPATH, "//*[@id=\"phone-84d9\"]").send_keys(client.phone)
        driver.find_element(By.XPATH, "//*[@id=\"address-be2d\"]").send_keys(client.adresse)
        driver.find_element(By.XPATH, "//*[@id=\"message-c6a3\"]").send_keys(client.message)

        if genre_value == "women" and select.first_selected_option.text == "Italie":
            Select(driver.find_element(By.XPATH, "//*[@id=\"select-c283\"]")).select_by_visible_text("Vélo")
            driver.find_element(By.XPATH, "//*[@id=\"checkbox-1848\"]").click()
        else:
            Select(driver.find_element(By.XPATH, "//*[@id=\"select-c283\"]")).select_by_visible_text("Moto")
            driver.find_element(By.XPATH, "//*[@id=\"checkbox-3250\"]").click()

        driver.find_element(By.XPATH, "//*[@id='carousel_1853']/div/div/div/div/form/div[12]/a").submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()