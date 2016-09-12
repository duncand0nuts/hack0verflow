import re
import requests
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)
browser.open('https://stackoverflow.com/users/login?ssrc=head&returnurl=http%3a%2f%2fstackoverflow.com%2f')

login_form = browser.get_form(id='login-form')

login_form['email'].value = 'USERNAME'
login_form['password'].value = 'PASSWORD'

login_form.serialize()

browser.submit_form(login_form)
