from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element("id", "searchInput")
        search.send_keys(query)
        search.submit()
        input("Press Enter to close the browser...")
        self.driver.quit()