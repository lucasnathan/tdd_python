from selenium import webdriver

# marquinhos heard about some to-do list app on a website. So he opens chrome browser
browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")
# browser = webdriver.Firefox()

# He types the adress
browser.get('http://localhost:8000')

# On the page title mentions the to-do list
assert 'To-Do' in browser.title

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

browser.quit()
