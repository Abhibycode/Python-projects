from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = "abhishekongari@gmail.com"
ACCOUNT_PASSWORD = "Mach@2025"
PHONE = "8983356442"

# Set up Chrome options for a persistent browser session
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keep browser open after script finishes

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()  # Maximize window for better element visibility


# --- Function to handle application abortion (e.g., when a complex form appears) ---
def abort_application():
    try:
        print("Attempting to abort current application (modal).")

        # Try to find and click the close button of the modal
        close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-modal__dismiss")))
        close_button.click()
        print("Modal close button clicked.")

        # Wait for the discard/confirm dialog to appear and click discard
        discard_buttons = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[contains(@class, 'artdeco-modal__confirm-dialog-btn')]"))
        )

        if len(discard_buttons) >= 2:
            discard_buttons[1].click()  # Click the "Discard" button
            print("Discard button clicked.")
        elif len(discard_buttons) == 1:
            print("Only one discard/confirm button found. Clicking it.")
            discard_buttons[0].click()
        else:
            print("No discard/confirm buttons found after closing initial modal.")

        time.sleep(2)

    except TimeoutException:
        print("Timeout: Close or discard button not found. Modal may not be open or already dismissed.")
    except NoSuchElementException:
        print("No such element: Close or discard button not found. Modal may not be open or already dismissed.")
    except Exception as e:
        print(f"An unexpected error occurred during abort_application: {e}")


# --- NEW FUNCTION: To handle any general modal overlay ---
def close_any_modal_overlay():
    try:
        print("Checking for and attempting to close any general modal overlay...")

        # Look for the common modal dismiss button or overlay that blocks interaction
        # LinkedIn often uses a dismiss button with a specific class for overlays
        # or sometimes hitting ESCAPE key works.

        # Try finding the generic dismiss button for modals
        close_modal_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__dismiss > span[aria-hidden='true']"))
            # More specific to the 'X' icon
        )
        close_modal_button.click()
        print("General modal overlay dismissed.")
        time.sleep(1)  # Give it a moment to disappear

    except TimeoutException:
        print("No general modal overlay found to close within the time limit.")
    except NoSuchElementException:
        print("No general modal overlay dismiss button found.")
    except ElementClickInterceptedException:
        print("Attempted to close modal, but click was intercepted (another overlay?). Retrying abort_application.")
        abort_application()  # Fallback to more aggressive modal closing
    except Exception as e:
        print(f"An error occurred while trying to close a general modal: {e}")


# --- Main Automation Script ---

# Navigate to the job search URL
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# --- IMPORTANT: Handle the cookie consent banner FIRST ---
try:
    print("Attempting to handle cookie consent banner...")
    wait = WebDriverWait(driver, 15)

    cookie_reject_locators = [
        (By.XPATH, "//button[contains(., 'Reject')]"),
        (By.XPATH, "//button[contains(., 'Decline')]"),
        (By.CSS_SELECTOR, 'button[aria-label*="reject"][data-test-id*="accept-btn"]'),
        (By.CSS_SELECTOR, 'button[data-tracking-control-name="reject_cookies_action"]'),
        (By.CLASS_NAME, "artdeco-button--tertiary"),
        (By.ID, "onetrust-reject-all-handler")
    ]

    found_cookie_button = False
    for locator_type, locator_value in cookie_reject_locators:
        try:
            reject_button = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            reject_button.click()
            print(f"Cookie reject button clicked using {locator_type}: {locator_value}")
            found_cookie_button = True
            break
        except (TimeoutException, NoSuchElementException):
            continue

    if not found_cookie_button:
        print("No obvious 'Reject' or 'Decline' cookie button found. Trying 'Accept' as a fallback.")
        accept_cookie_locators = [
            (By.XPATH, "//button[contains(., 'Accept')]"),
            (By.XPATH, "//button[contains(., 'Allow')]"),
            (By.ID, "onetrust-accept-btn-handler")
        ]
        for locator_type, locator_value in accept_cookie_locators:
            try:
                accept_button = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
                accept_button.click()
                print(f"Cookie accept button clicked using {locator_type}: {locator_value}")
                found_cookie_button = True
                break
            except (TimeoutException, NoSuchElementException):
                continue

    if not found_cookie_button:
        print("WARNING: Could not find any cookie consent button. Script might be blocked by it.")

    time.sleep(3)  # Give more time for the banner to fully disappear

except Exception as e:
    print(f"An error occurred while trying to handle the cookie banner: {e}")

# --- NEW STEP: After cookie handling, try to close any unexpected modals ---
close_any_modal_overlay()
time.sleep(2)  # Give a moment after trying to close any modal

# Click Sign in Button
try:
    print("Looking for 'Sign in' button...")
    # Use a more robust locator for the sign-in button if the LINK_TEXT is proving problematic
    # Given the error, the LINK_TEXT is likely fine, but an overlay is blocking it.
    # We still need to wait for it to be clickable *after* any overlays are gone.
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    sign_in_button.click()
    print("'Sign in' button clicked.")
    time.sleep(5)  # Wait for the sign-in page to load
except TimeoutException:
    print("Timeout: 'Sign in' button not found or not clickable after modal handling. Exiting.")
    driver.quit()
    exit()
except NoSuchElementException:
    print("No 'Sign in' button found after modal handling. Exiting.")
    driver.quit()
    exit()
except ElementClickInterceptedException as e:
    print(f"ERROR: ElementClickInterceptedException on 'Sign in' button even after trying to close modals: {e}")
    print("This indicates another, persistent overlay. Manual inspection might be needed.")
    driver.quit()
    exit()

# Enter credentials
try:
    print("Entering credentials...")
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
    print("Credentials entered and login attempted.")
    time.sleep(5)  # Wait for login to process and page to redirect
except TimeoutException:
    print("Timeout: Email or password fields not found on login page. Exiting.")
    driver.quit()
    exit()
except NoSuchElementException:
    print("No such element: Email or password fields not found on login page. Exiting.")
    driver.quit()
    exit()

# Wait for job listings to load after login
try:
    print("Waiting for job listings to load...")
    all_listings = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable"))
    )
    print(f"Found {len(all_listings)} job listings.")
except TimeoutException:
    print("Timeout: No job listings found after login. Exiting.")
    driver.quit()
    exit()

# Iterate through job listings
for i in range(len(all_listings)):
    try:
        # Re-find all listings inside the loop to avoid StaleElementReferenceException
        all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
        listing = all_listings[i]

        print(f"Opening Listing {i + 1}...")
        listing.click()
        time.sleep(2)

        print("Looking for apply button...")
        apply_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-s-apply button")))
        apply_button.click()
        print("Apply button clicked.")

        # --- Handle Application Form ---
        print("Handling application form...")
        time.sleep(3)

        # Check for phone number field
        try:
            phone_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[id*=phoneNumber]")))
            if phone_field.get_attribute("value") == "" or "your phone" in phone_field.get_attribute(
                    "placeholder").lower():
                phone_field.send_keys(PHONE)
                print("Phone number inserted.")
            else:
                print("Phone number already present.")
        except (TimeoutException, NoSuchElementException):
            print("Phone number field not found or not required.")

        print("Checking submit/continue button...")
        submit_or_continue_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "footer button")))

        if submit_or_continue_button.get_attribute("data-control-name") == "continue_unify":
            print("Complex application detected ('Continue' button). Aborting application.")
            abort_application()
            print("Application skipped.")
        else:
            print("Submitting job application")
            submit_or_continue_button.click()
            print("Application submitted.")
            time.sleep(2)

            try:
                close_button_success = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-modal__dismiss")))
                close_button_success.click()
                print("Success modal closed.")
            except (TimeoutException, NoSuchElementException):
                print("No success modal or close button found after submission.")

    except TimeoutException:
        print("Timeout during application process for this listing. Skipping.")
        abort_application()
        continue
    except NoSuchElementException:
        print("No application button or other required element found for this listing. Skipping.")
        abort_application()
        continue
    except ElementClickInterceptedException as e:
        print(
            f"Element click intercepted during application for listing {i + 1}: {e}. Attempting to close modal and skip.")
        abort_application()
        continue
    except Exception as e:
        print(f"An unexpected error occurred for listing {i + 1}: {e}. Skipping.")
        abort_application()
        continue

time.sleep(5)
driver.quit()
print("Script finished. Browser closed.")