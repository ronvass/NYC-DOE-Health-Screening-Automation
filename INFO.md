follow @ron.vass on Instagram
# NYC-DOE-Health-Screening-Automation
Filling out the same questionare every morning can get quite annoying... which is why I have utliized the power of Selenium and Chrome Webdriver to automate it — in seconds!

REQUIRED: Have Python installed, along with PIP. (Use pip through your terminal to install selenium by running this in your command prompt: pip3 install selenium

Then, download the chromedriver for your chrome version (your version can be checked in Chrome Settings) https://chromedriver.chromium.org/downloads. Once you download this, move the file from the zip into the same directory in your file explorer where you will run this automation script.

Here's how one would customize this for personal use:

First, in line 5, in the quotes, specify the location of where you placed your chrome webdriver download. (for example 'C:/Users/Your Name/Documents/chromedriver.exe')
Now it's time to input your information in the quotes on these lines:
In line 12, input your first name.
In line 16, input your last name.
In line 20, input your email.
In line 27, input your full school name.

And.. that's it!
Of course, this info setup is a one-time thing, which is the whole point of this automation.
You can use Windows Task Scheduler to make this run every school morning by itself locally, as long as your computer is not powered off. On Mac or Linux, you can use Cronjobs.

NOTE: line 46 has to be altered based on vaccination status.
