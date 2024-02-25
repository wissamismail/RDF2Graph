from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

def process_text(rdf_text):
    # Open the website
    driver = webdriver.Chrome()
    driver.get("https://www.w3.org/RDF/Validator/")

    # Enter text into the RDF textarea
    textarea = driver.find_element(By.NAME, "RDF")
    textarea.clear()  # Clear pre-existing text (if allowed)
    textarea.send_keys(rdf_text)

    # Select the second item in the TRIPLES_AND_GRAPH combo box
    dropdown = driver.find_element(By.NAME, "TRIPLES_AND_GRAPH")
    selected_option = dropdown.find_elements(By.TAG_NAME, "option")[1]  # Second option
    selected_option.click()

    # Click the PARSE button
    parse_button = driver.find_element(By.NAME, "PARSE")
    parse_button.click()

    # Wait for New Page and Switch Focus
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the new window

    # Extract Data from Validation Results
    main_div = driver.find_element(By.ID,"main")
    messages_h2 = main_div.find_element(By.XPATH,"//h2[a[@id='messages']]")

    paragraph = messages_h2.find_element(By.XPATH, "./following-sibling::h3")
    validation_results = paragraph.get_attribute("textContent")
    if (validation_results!='Fatal Error Messages' ):
        paragraph = messages_h2.find_element(By.XPATH, "./following-sibling::p")
        validation_results = paragraph.get_attribute("textContent")
    else:
        #validation_results = paragraph.get_attribute("textContent")
        validation_message = get_fatal_error_lines( main_div.text)
        validation_results = validation_results  + " " + validation_message[0]
        #message = driver.find_element(By.XPATH,"//div[@id='main']/h3/following-sibling::text()")
        # message = validation_results.find_element(By.XPATH, "./following-sibling::*[1]")

    #validation_results =  driver.find_element(By.XPATH,"//div[@id='main']//h2[a[@id='messages']]/following-sibling::p")
    print(validation_results)

    #Extract Data from Table and Image
    messages_h3 = main_div.find_element(By.XPATH, "//h3[a[@id='triples']]")
    paragraph_table = messages_h3.find_element(By.XPATH, "./following-sibling::*[1]")
    table = paragraph_table.get_attribute('innerHTML')

    image = driver.find_element(By.XPATH, "//img[@alt='graph representation of RDF data']")
    image_src = image.get_attribute("src")  # Get image source URL
    print(image)
    print(image_src)
    sleep(1)

    # Close the browser
    driver.quit()

    return validation_results, image_src, table
def get_fatal_error_lines(text_or_file):
  """Extracts lines starting with "FatalError:" from the provided text or file."""
  if isinstance(text_or_file, str):
    # Handle text string
    lines = text_or_file.splitlines()
    return [line for line in lines if line.startswith("FatalError:")]
  else:
    # Handle text file
    with open(text_or_file, 'r') as f:
      return [line for line in f if line.startswith("FatalError:")]

if __name__ == "__main__":
    process_text()