import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Put your details here
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_password"
MY_PHONE = "1234567890"

# 2. Open the browser and go to the LinkedIn jobs page
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=Analytic%20Recruiting%20Inc&location=Canada")
time.sleep(3) # Wait 3 seconds for the page to load

# 3. Click the "Sign in" button
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(3)

# 4. Type in the email and password
email_box = driver.find_element(By.ID, "username")
email_box.send_keys(MY_EMAIL)

password_box = driver.find_element(By.ID, "password")
password_box.send_keys(MY_PASSWORD)

# 5. Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5) # Wait 5 seconds to log in completely

# 6. Find all the jobs listed on the left side of the screen
jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print("Found", len(jobs), "jobs.")

# 7. Go through each job one by one
for job in jobs:
    print("Clicking a new job...")
    job.click()
    time.sleep(2)
    
    try:
        # Try to find and click the "Easy Apply" button
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()
        time.sleep(2)
        
        # Type the phone number
        phone_box = driver.find_element(By.CSS_SELECTOR, "input[class*='fb-single-line-text']")
        phone_box.send_keys(MY_PHONE)
        
        # Click the "Next" or "Submit" buttons at the bottom
        next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        next_button.click()
        time.sleep(2)
        
        review_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Review your application']")
        review_button.click()
        time.sleep(2)
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Submit application']")
        submit_button.click()
        time.sleep(2)
        
        print("Job applied successfully!")
        
    except:
        # If the application has too many steps or questions, it fails here and skips to the next job
        print("Could not apply to this job automatically. Skipping...")

print("All done!")
driver.quit()