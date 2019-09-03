from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        # marquinhos heard about some to-do list app on a website. So he opens chrome browser
        self.browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")
        # self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # He types the adress
        self.browser.get('http://localhost:8000')

        # On the page title mentions the to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail("finish test!")

        # He receives the input to enter a to-do item right away

        # He types "Buy Big fan" into a text box (Marquinhos's hobby is collecting fans)

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy Big fan" as an item in a to-do list
        # There is still a text box inviting him to add another item. He
        # enters "Use Big fan to make me fly" (Marquinhos is very excentric)
        # The page updates again, and now shows both items on his list
        # Maquinhos wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.
        # He visits that URL - his to-do list is still there.
        # Satisfied, he goes back to his fan

if __name__ == '__main__':
    unittest.main(warnings='ignore')
