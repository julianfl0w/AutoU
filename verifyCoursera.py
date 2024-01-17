from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

@app.route('/verify', methods=['POST'])  # Change to POST
def verify_url():
    # Read the list of URLs from the JSON payload
    data = request.json
    urls = data.get('urls')
    if not urls or not isinstance(urls, list):
        return jsonify({'error': 'Missing or invalid URL list'}), 400

    results = []
    for url in urls:
        try:
            # Navigate to the page
            driver.get(url)

            # Wait for the element to be loaded
            name_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3.cds-119 strong"))
            )
            name = name_element.text if name_element else "Name not found"

            # Find the element containing the course name
            course_name_element = driver.find_element(By.CSS_SELECTOR, "h2.course-name")
            # Extract the text content from the element
            course_name = course_name_element.text
            print(course_name)

            results.append({'name': name, 'course_name':course_name})
        except Exception as e:
            results.append({'error': str(e)})

    # Close the driver after processing all URLs
    driver.quit()

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
