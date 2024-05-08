from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" +query)
        search = self.driver.find_element("id", "title-wrapper")
        search.click()
        input("Press Enter to close the browser...")
        self.driver.quit()