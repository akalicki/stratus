"""
    stratus // dbox.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

import names, random, string
import dropbox
import db
from selenium import webdriver
from config import config

DROPBOX_URL = "http://dropbox.com"
EMAIL_SUFFIX = "@maildrop.cc"

def account_space(access_token):
    """Gets amount of free space in the given account"""
    client = dropbox.client.DropboxClient(access_token)
    account_info = client.account_info()
    quota_info = account_info["quota_info"]
    total = quota_info["quota"]
    used = quota_info["normal"] + quota_info["shared"]
    return total - used

def generate_account():
    """Creates and authorizes a new dropbox account"""
    print "Adding space to stratus account..."
    driver = webdriver.PhantomJS()
    email, password = create_account(driver)
    access_token, user_id = authorize_account(driver, email, password)
    driver.quit()
    db.add_account(user_id, access_token)

def create_account(driver):
    """Generates a new dropbox account, returns account email + password"""
    fname = names.get_first_name()
    lname = names.get_last_name()
    email = random_string(10) + EMAIL_SUFFIX
    password = random_string(20)
    signup_js = """
            document.getElementById('fname').value = '%s';
            document.getElementById('lname').value = '%s';
            document.getElementById('email').value = '%s';
            document.getElementById('password').value = '%s';
            document.getElementById('tos_agree').checked = true;
            document.getElementById('signup-form').submit();
        """ % (fname, lname, email, password)
    driver.implicitly_wait(10)
    driver.get(DROPBOX_URL)
    driver.execute_script(signup_js)
    return email, password

def authorize_account(driver, email, password):
    """Authorizes account to take requests from app, returns access token"""
    app_key = config["app_key"]
    app_secret = config["app_secret"]
    auth_flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    auth_url = auth_flow.start()
    login_js = """
            document.getElementById('login_email').value = '%s';
            document.getElementById('login_password').value = '%s';
        """ % (email, password)
    driver.implicitly_wait(10)
    driver.get(auth_url)
    driver.execute_script(login_js)
    driver.find_element_by_id('login_submit').click()
    driver.find_element_by_name('allow_access').click()
    auth_code = driver.find_element_by_class_name('auth-code').text
    access_token, user_id = auth_flow.finish(auth_code)
    return access_token, user_id

def random_string(length):
    """Returns a pseudorandom ASCII letter + digit string of size 'length'"""
    allowed_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(allowed_chars) for x in range(length))