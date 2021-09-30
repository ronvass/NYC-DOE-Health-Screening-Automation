# NYC-DOE-Health-Screening-Automation
Filling out the same form every morning can get quite annoying... which is why I have harnessed the power of Selenium and Chrome Webdriver to automate it — in seconds!

WHAT IS THIS: This is a python script to automate filling out the DOE health screen web form when your information is the same. Your name, email and school are unlikely to change day-to-day and so this script will allow you to fill them in once and automate the rest. 

DISCLAIMER: The goal of this script is to automate filling fields that do not change over time. If your information changes in any way (e.g. your vaccination status changes or you are experiencing symptoms of COVID-19) make sure that your inputs reflect the _current_ accurate set of data. **Currently, you will have to modify the presets manually within the script for any changes to take place.**

SOFTWARE REQUIREMENTS: You must have Python installed, along with pip. Use pip through your terminal to install selenium by running this in your command prompt: `pip3 install selenium`.

Then, download the chromedriver for your chrome version (your version can be checked in Chrome Settings) https://chromedriver.chromium.org/downloads. Once you download this, move the file from the zip into the same directory in your file explorer where you will run this automation script.

Here's how one would customize this for personal use:

First, in line 6, in the quotes, specify the location of where you placed your chrome webdriver download. (for example 'C:/Users/Your Name/Documents/chromedriver.exe')
Now it's time to input your information in the quotes on these lines:
In line 7, input your first name.
In line 8, input your last name.
In line 9, input your email.
In line 10, input your full school name.

And.. that's it!
Of course, this info setup is a one-time thing, which is the whole point of this automation.
You can use Windows Task Scheduler to make this run every school morning by itself locally, as long as your computer is not powered off. On Mac or Linux, you can use Cronjobs.

NOTE: line 48 (the `RadioButtonVaccination` definition) has to be altered based on vaccination status.
