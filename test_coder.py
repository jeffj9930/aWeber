#############################################################################################################################
# Author:	Jeff Jozwiak
# Creation: 08/10/2021
# Last Updated:	08/15/2021
# Pytest test suite to execute testing of webpage WordPress.com My Profile
#############################################################################################################################
import re
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_name = 'jeffj9930'
passwd = 'DaHgXxj9rx5nncQ'

driver = webdriver.Chrome('/home/jeff/code/chromedriver_linux64/chromedriver')

def open_my_profile():
	regex_myprofile = 'My Profile.+WordPress.com'
	regex_login = 'Log In.+WordPress.com'
	driver.get('https://wordpress.com/me')
	driver.implicitly_wait(10)
	driver.maximize_window()
	hndl = driver.window_handles[0]
	current_title = driver.title
	assert re.match(regex_login, current_title)
	username_box = driver.find_element_by_xpath('//*[@id="usernameOrEmail"]')
	username_box.send_keys(user_name)
	username_box.submit()
	time.sleep(1)
	pswd_box = driver.find_element_by_xpath('//*[@id="password"]')
	pswd_box.send_keys(passwd)
	#driver.find_element_by_name('Log In').click()
	driver.find_element_by_xpath('//*[@id="primary"]/div/main/div/div/form/div[1]/div[2]/button').click()
	time.sleep(1)
	profile_title = driver.title
	assert re.match(regex_myprofile, profile_title)
	return hndl

hndl = open_my_profile()


#############################################################################################################################
# Start of test case suite
# Testing of WordPress Profile Page
#############################################################################################################################



def test_wp_input_first_name():
	firstname = 'Timothy'
	firstname_box = driver.find_element_by_xpath('//*[@id="first_name"]')
	firstname_box.send_keys(firstname)
	save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
	save_details_btn.click()
	input_check = firstname_box.get_attribute('value')
	assert firstname == input_check

def test_wp_input_last_name():
	lastname = 'Schultz'
	lastname_box = driver.find_element_by_xpath('//*[@id="last_name"]')
	lastname_box.send_keys(lastname)
	save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
	save_details_btn.click()
	input_check = lastname_box.get_attribute('value')
	assert lastname == input_check
	
def test_wp_public_display_name():
	displayname = user_name
	driver.maximize_window()
	displayname_box = driver.find_element_by_xpath('//*[@id="display_name"]')
	save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
	save_details_btn.click()
	input_check = displayname_box.get_attribute('value')
	assert displayname == input_check	
	
def test_wp_alter_public_display_name():
	displayname = user_name
	driver.maximize_window()
	displayname_box = driver.find_element_by_xpath('//*[@id="display_name"]')
	displayname_box.clear()
	new_name = 'new_user_name'
	displayname_box.send_keys(new_name)
	save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
	save_details_btn.click()
	new_input_check = displayname_box.get_attribute('value')
	assert new_name == new_input_check	
	time.sleep(1)
	displayname_box.clear()
	displayname_box.send_keys(user_name)
	save_details_btn.click()
	input_check = displayname_box.get_attribute('value')
	assert displayname == input_check	
	
def test_wp_input_about_me_info():
	text_str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+=:;{}[]<>?/\\|0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+=:;{}[]<>?/\\|0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+=:;{}[]<>?/\\|0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+=:;{}[]<>?/\\|'
	driver.maximize_window()
	aboutme_box = driver.find_element_by_xpath('//*[@id="description"]')
	aboutme_box.send_keys(text_str)
	save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
	save_details_btn.click()
	input_check = aboutme_box.get_attribute('value')
	assert text_str == input_check

def test_wp_toggle_hide_gravatar_flip():
	driver.maximize_window()
	gravatar = driver.find_element_by_xpath('//*[@id="inspector-toggle-control-0"]')
	if gravatar.is_selected():
		gravatar.click()
		assert gravatar.is_selected() is False
		gravatar.click()
		assert gravatar.is_selected() is True	
	else:
		gravatar.click()
		assert gravatar.is_selected() is True	
		gravatar.click()
		assert gravatar.is_selected() is False	
		
def test_wp_toggle_hide_gravatar_saved_notice():
	driver.maximize_window()
	gravatar = driver.find_element_by_xpath('//*[@id="inspector-toggle-control-0"]')
	if gravatar.is_selected() is True:
		gravatar.click()
	assert gravatar.is_selected() is False
	save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
	save_details_btn.click()
	time.sleep(2)
	saved_notice = driver.find_element_by_xpath('//*[@id="notices"]/div/span[2]/span').text
	assert saved_notice == 'Settings saved successfully!'
	gravatar.click()
	assert gravatar.is_selected() is True	
	save_details_btn.click()
	time.sleep(2)
	saved_notice = driver.find_element_by_xpath('//*[@id="notices"]/div/span[2]/span').text
	assert saved_notice == 'Settings saved successfully!'
	
def test_wp_gravatar_profile_not_hidden():
	driver.maximize_window()
	gravatar = driver.find_element_by_xpath('//*[@id="inspector-toggle-control-0"]')
	if gravatar.is_selected() is True:
		gravatar.click()
		save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
		save_details_btn.click()
		time.sleep(2)
	assert gravatar.is_selected() is False
	gravatar_profile = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/fieldset[5]/div/div/label/span/a[1]')
	gravatar_profile.click()
	driver.switch_to.window(driver.window_handles[1])
	user = driver.find_element_by_xpath('//*[@id="profile"]/div[2]/div[1]/h2/a').text
	driver.switch_to.window(driver.window_handles[0])
	assert  user == user_name

def test_wp_gravatar_profile_hidden():
	driver.maximize_window()
	time.sleep(4)
	gravatar = driver.find_element_by_xpath('//*[@id="inspector-toggle-control-0"]')
	if gravatar.is_selected() is False:
		gravatar.click()
		save_details_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/p/button')
		save_details_btn.click()
		time.sleep(2)
	assert gravatar.is_selected() is True
	gravatar_profile = driver.find_element_by_xpath('//*[@id="primary"]/main/div[2]/form/fieldset[5]/div/div/label/span/a[1]')
	gravatar_profile.click()
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(2)
	assertion = False
	try:
		user = driver.find_element_by_xpath('//*[@id="profile"]/div[2]/div[1]/h2/a').text
	except:
		assertion = True
	driver.switch_to.window(driver.window_handles[0])
	assert assertion
	
def test_wp_reader_button():
	driver.maximize_window()
	driver.implicitly_wait(20)
	reader_btn = driver.find_element_by_xpath('//*[@id="header"]/a[2]/span')
	reader_btn.click()
	try:
		search_box = driver.find_element_by_xpath("//*[starts-with(@id, 'search-component')]")
		found = True
		back_to_profile = driver.find_element_by_xpath('//*[@id="header"]/a[3]/span/img')
		back_to_profile.click()
	except:
		found = False
	assert found

def test_wp_add_to_profile_links():
	driver.maximize_window()
	url_link = 'github.com/jeffj9930'
	desc_text = 'This is a test string for description box'
	add_link_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[3]/div[2]/button')
	add_link_btn.click()
	add_url_selector = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/button[2]')
	add_url_selector.click()
	url_box = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/input[1]')
	url_box.send_keys(url_link)
	desc_box = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/input[2]')
	desc_box.send_keys(desc_text)
	time.sleep(1)
	add_site_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/button[1]')
	add_site_btn.click()
	time.sleep(2)
	profile_link_url = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/div/ul/li/a[2]/span[2]')
	url_input = profile_link_url.text
	assert url_link == url_input
	
def test_wp_add_bad_url_to_profile_links():
	driver.maximize_window()
	bad_url_link = 'githubcom/jeffj9930/bad/link'
	desc_text = 'This is a test string for description box on using bad URL'
	add_link_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[3]/div[2]/button')
	add_link_btn.click()
	add_url_selector = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/button[2]')
	add_url_selector.click()
	url_box = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/input[1]')
	url_box.send_keys(bad_url_link)
	desc_box = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/input[2]')
	desc_box.send_keys(desc_text)
	time.sleep(1)
	add_site_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/button[1]')
	if not add_site_btn.is_enabled():
		assert True
		cancel_btn = driver.find_element_by_xpath('//*[@id="primary"]/main/div[4]/form/fieldset/button[2]')
		cancel_btn.click()
	else:
		assert False

	
def test_wp_logout():
	logout_btn = driver.find_element_by_xpath('//*[@id="secondary"]/ul/li/div[2]/button')
	logout_btn.click()
	time.sleep(2)
	regex_myprofile = 'WordPress.com'
	current_title = driver.title
	assert re.match(regex_myprofile, current_title)
	
"""

"""