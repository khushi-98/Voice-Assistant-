# from selenium import webdriver 

# class music():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def play(self_,query):
#         self.query=query
#         self.driver.get(url="https://www.youtube.com/results?search_query=",+ query)
#         video=self.driver.find_element_by_xpath('//[@id="dismissable"]')
#         video.click()

# assist=music()
# assist.play('lover by taylor')

# from selenium import webdriver 

# class Music():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def play(self, query):
#         self.query = query
#         self.driver.get("https://www.youtube.com/results?search_query=" + query)
#         video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
#         video.click()

# assist = Music()
# assist.play('lover by taylor')



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class Music():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def play(self, query):
#         self.query = query
#         self.driver.get("https://www.youtube.com/results?search_query=" + query)

#         try:
#             # Wait for the first video element to be present
#             wait = WebDriverWait(self.driver, 10)
#             video = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-video-renderer a[href^="/watch?"]')))

#             # Open the video in a new tab or window
#             video.click()
#             self.driver.switch_to.window(self.driver.window_handles[-1])

#             # Wait for the video player to load and start playing
#             player = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.html5-video-player')))

#             # Play the video
#             play_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-play-button')))
#             play_button.click()

#             # Switch to full-screen mode
#             full_screen_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-fullscreen-button')))
#             full_screen_button.click()

#             # Wait for 3 minutes (180 seconds)
#             time.sleep(180)

#         except Exception as e:
#             print("An error occurred:", e)
#         finally:
#             # Do not close the browser
#             pass

# assist = Music()
# assist.play('lover by taylor')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard

class Music():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options)

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)

        try:
            # Wait for the first video element to be present
            wait = WebDriverWait(self.driver, 10)
            video = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-video-renderer a[href^="/watch?"]')))

            # Open the video in a new tab or window
            video.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Wait for the video player to load and start playing
            player = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.html5-video-player')))

            # Play the video
            play_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-play-button')))
            play_button.click()

            # # Switch to full-screen mode
            # full_screen_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-fullscreen-button')))
            # full_screen_button.click()

            # Wait until the user presses 'q' or the video ends (3 minutes)
            start_time = time.time()
            while True:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 180 or keyboard.is_pressed('q'):
                    break
                time.sleep(1)

        except Exception as e:
            print("An error occurred:", e)
        finally:
            # Do not close the browser
            pass

# assist = Music()
# assist.play('lover by taylor')



