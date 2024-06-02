# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class Inflow():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def get_info(self, query):
#         self.query = query
#         self.driver.get("https://www.wikipedia.org/")
#         try:
          
#             search = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.ID, "searchInput"))
#             )
#             search.click()
#             search.send_keys(query)
            
          
#             enter = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/form/fieldset/button'))
#             )
#             enter.click()

         
#             WebDriverWait(self.driver, 10).until(
#                 EC.url_contains("Special:Search")
#             )

            
#         except Exception as e:
#             print("An error occurred:", e)
#         finally:
           
#             self.driver.quit()

# assist = Inflow()
# assist.get_info("neutron star")





# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class Inflow():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def get_info(self, query):
#         self.query = query
#         self.driver.get("https://www.wikipedia.org/")
#         try:
#             search = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.ID, "searchInput"))
#             )
#             search.click()
#             search.send_keys(query)
            
#             enter = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/form/fieldset/button'))
#             )
#             enter.click()

#             WebDriverWait(self.driver, 10).until(
#                 EC.url_contains("Special:Search")
#             )

#             # Code will pause here until the user manually closes the browser window

#             while True:
                
#                 if keyboard.is_pressed('q'):
#                     break
#                 time.sleep(1)


#         except Exception as e:
#             print("An error occurred:", e)
#         finally:
#             # Do not close the browser window automatically
#             pass

# assist = Inflow()
# assist.get_info("neutron star")




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import keyboard
# import time


# class Inflow():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def get_info(self, query):
#         self.query = query
#         self.driver.get("https://www.wikipedia.org/")
#         try:
#             search = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.ID, "searchInput"))
#             )
#             search.click()
#             search.send_keys(query)

#             enter = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/form/fieldset/button'))
#             )
#             enter.click()

#             WebDriverWait(self.driver, 10).until(
#                 EC.url_contains("Special:Search")
#             )

#             while True:
#                 if keyboard.is_pressed('q'):
#                     break
#                 time.sleep(1)

#         except Exception as e:
#             print("An error occurred:", e)
#         finally:
#             self.driver.quit()



# # Example usage
# assist = Inflow()
# assist.get_info("neutron star")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import keyboard
# import time

# class Inflow():
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def get_info(self, query):
#         self.query = query
#         self.driver.get("https://www.wikipedia.org/")
#         try:
#             search = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.ID, "searchInput"))
#             )
#             search.click()
#             search.send_keys(query)

#             enter = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/form/fieldset/button'))
#             )
#             enter.click()

#             WebDriverWait(self.driver, 10).until(
#                 EC.url_contains("Special:Search")
#             )

#             while True:
#                 time.sleep(300000)
#                 if keyboard.is_pressed('q'):
#                     self.driver.quit()  # Close the browser window when 'q' is pressed
#                     break
#                 time.sleep(1)

#         except Exception as e:
#             print("An error occurred:", e)

# # Example usage
# assist = Inflow()
# assist.get_info("neutron star")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Inflow():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('executable_path=C:/Users/bansa/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")
        try:
            search = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "searchInput"))
            )
            search.click()
            search.send_keys(query)

            enter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/form/fieldset/button'))
            )
            enter.click()

            WebDriverWait(self.driver, 10).until(
                EC.url_contains("Special:Search")
            )

            self.driver.maximize_window()  # Maximize window for better user experience

            # Keep the script running until the user manually closes the browser window
            while True:
                if not self.driver.current_window_handle:
                    break
                time.sleep(1)

        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.driver.quit()  # Close the browser window when done

# Example usage
# assist = Inflow()
# assist.get_info("neutron star")
