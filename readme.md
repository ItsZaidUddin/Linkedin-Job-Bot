# 🤖 LinkedIn Auto-Apply Bot

I built this Python script to automate the most repetitive parts of job hunting. Instead of manually clicking through hundreds of listings, this bot automatically finds "Easy Apply" positions on LinkedIn and submits the applications for me.

### 🛠️ What I Used & Learned

* Automating web browsers using Python and Selenium.
* Selecting and interacting with dynamic website elements using CSS Selectors.
* Handling multi-step web forms and error handling for complex applications.

### 🚀 How It Works

Under the hood, this script uses the **Selenium library** — specifically the `webdriver` module—to create a Chrome browser object. Once launched, this object logs into my account, navigates to a target search URL, and handles all the button clicks and form inputs required to submit an application. 

### ⚠️ A Quick Note on Web Scraping

LinkedIn updates its website structure and class names pretty constantly. The CSS selectors used in this code work for the current UI, but they might need a quick tweak if LinkedIn pushes a layout update!
