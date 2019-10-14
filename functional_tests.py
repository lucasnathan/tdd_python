from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # marquinhos heard about some to-do list app on a website. So he opens chrome browser
        self.browser = webdriver.Chrome(
            executable_path="chromedriver_linux64/chromedriver")
        # self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # He types the adress
        self.browser.get('http://localhost:8000')

        # On the page title mentions the to-do list
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your To-Do list', header_text)

        # He receives the input to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
        'Enter a to-do item')
        # He types "Buy peacock feathers" into a text box (Marquinhos's hobby is
        # collecting peacock feathers)
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        
        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make me fly" (Marquinhos is very excentric)
        # The page updates again, and now shows both items on his list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )
        
        # Maquinhos wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.
        # He visits that URL - his to-do list is still there.
        # Satisfied, he goes back to his peacock feathers
        self.fail("finish test!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
