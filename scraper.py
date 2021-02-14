# === libs ===

import pickle  # store date
from datetime import datetime
import os  # create new folders
from urllib.request import urlopen  # open URLs
from bs4 import BeautifulSoup  # BeautifulSoup; parsing HTML
import re  # regex; extract substrings
from datetime import datetime  # calculate script's run time
from alive_progress import alive_bar  # progress bar
import time  # delay execution; https://stackoverflow.com/questions/3327775/can-the-execution-of-statements-in-python-be-delayed
import webbrowser  # open browser
import sys  # exit()
import ssl  # fix certificate issue: https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate
import certifi  # fix certificate issue: https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate
from sys import platform  # check platform (Windows/Linux/macOS)
if platform == 'win32':
    from win10toast_persist import ToastNotifier  # Windows 10 notifications
    toaster = ToastNotifier()  # initialize win10toast
    from termcolor import colored  # colored input/output in terminal

# === start + run time ===

print("Starting...")
start = datetime.now()  # run time

# === have current date in exported files' names ===
# https://www.w3schools.com/python/python_datetime.asp
today_date = datetime.strftime(datetime.now(), '%y%m%d_%f') # YYMMDD_microsecond

# create new YYMMDD_microsecond folder
if not os.path.isdir("/output/" + today_date):
    os.mkdir("output/" + today_date)
    print("Folder created: " + today_date)

filename = 'date.pk'
try:  # might crash on first run
    # load your data back to memory so we can save new value; NOTE: b = binary
    with open(filename, 'rb') as file:
        previous_date = pickle.load(file)
        print("Prev date:", previous_date)
except IOError:
    print("First run - no file exists.")

try:
    with open(filename, 'wb') as file:  # open pickle file
        pickle.dump(today_date, file)  # dump your data into the file
        print("Today date: ", today_date)
except IOError:
    print("File doesn't exist.")

# === URLs to scrape ===

# BMW, 140+ KM, AT, PDC, AC, CC, Xen, Pb/On, 15k
page_url = "https://www.otomoto.pl/osobowe/bmw/?search%5Bfilter_float_price%3Ato%5D=15000&search%5Bfilter_enum_fuel_type%5D%5B0%5D=petrol&search%5Bfilter_enum_fuel_type%5D%5B1%5D=diesel&search%5Bfilter_float_engine_power%3Afrom%5D=140&search%5Bfilter_enum_gearbox%5D%5B0%5D=automatic&search%5Bfilter_enum_gearbox%5D%5B1%5D=cvt&search%5Bfilter_enum_gearbox%5D%5B2%5D=dual-clutch&search%5Bfilter_enum_gearbox%5D%5B3%5D=semi-automatic&search%5Bfilter_enum_gearbox%5D%5B4%5D=automatic-stepless-sequential&search%5Bfilter_enum_gearbox%5D%5B5%5D=automatic-stepless&search%5Bfilter_enum_gearbox%5D%5B6%5D=automatic-sequential&search%5Bfilter_enum_gearbox%5D%5B7%5D=automated-manual&search%5Bfilter_enum_gearbox%5D%5B8%5D=direct-no-gearbox&search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_features%5D%5B0%5D=rear-parking-sensors&search%5Bfilter_enum_features%5D%5B1%5D=automatic-air-conditioning&search%5Bfilter_enum_features%5D%5B2%5D=xenon-lights&search%5Bfilter_enum_features%5D%5B3%5D=cruise-control&search%5Bfilter_enum_no_accident%5D=1&search%5Border%5D=filter_float_mileage%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D="

# === function to scrape data ===

def pullData(page_url):

    # ? can't crawl too often? works better with Otomoto limits perhaps
    pause_duration = 3  # seconds to wait
    print("Waiting for", pause_duration, "seconds before opening URL...")
    with alive_bar(pause_duration, bar="circles", spinner="dots_waves") as bar:
        for second in range(0, pause_duration):
            time.sleep(1)
            bar()

    print("Opening page...")
    # print (page_url) # 🐛 debug
    page = urlopen(page_url, context=ssl.create_default_context(
        cafile=certifi.where()))  # fix certificate issue

    print("Scraping page...")
    soup = BeautifulSoup(page, 'html.parser')  # parse the page

    # local_file = r"output/bs_output.txt"

    # 'a' (append) to add lines to existing file vs overwriting
    with open(r"output/" + today_date + "/1-bs_output.txt", "a", encoding="utf-8") as bs_output:
        # print (colored("Creating local file to store URLs...", 'green'))
        counter = 0  # counter to get # of URLs/cars
        with alive_bar(bar="circles", spinner="dots_waves") as bar:  # progress bar
            for link in soup.find_all("a", {"class": "offer-title__link"}):
                bs_output.write(link.get('href'))
                counter += 1  # counter ++
                bar()  # progress bar ++
                # print ("Adding", counter, "URL to file...")
        print("Successfully added", counter, "cars to file.")
        # print ("File with URLs successfully created.")

    # return counter # so we can sum up all URLs/cars later on

# === run URLs in function ^ ===

# open(r"output/bs_output.txt", "w").close() # clean main file at start
try:
    open(r"output/" + today_date + "/1-bs_output.txt",
         "w").close()  # clean main file at start
except:  # crashes on 1st run when file is not yet created
    print("Nothing to clean, moving on...")

# number_of_pages_to_crawl = int(input("Ile podstron chcesz przejrzeć? >>> ")) # give user choice
number_of_pages_to_crawl = 2

page_number = 1  # begin at page=1
# with alive_bar(number_of_pages_to_crawl, bar="circles", spinner="dots_waves") as bar:
for page in range(1, number_of_pages_to_crawl+1):
    print("Page number:", page_number, "/",
          number_of_pages_to_crawl)  # 🐛 debug
    full_page_url = f"{page_url}{page_number}"
    pullData(full_page_url)
    # print ("Full page URL:", full_page_url) # 🐛 debug
    # bar()
    page_number += 1  # go to next page

# === make file more pretty by adding new lines ===

# open file...
with open(r"output/" + today_date + "/1-bs_output.txt", "r", encoding="utf-8") as local_file:
    print("Reading file to clean up...")
    read_local_file = local_file.read()  # ... and read it
urls_line_by_line = re.sub(
    r"#[a-zA-Z0-9]+(?!https$)://", "\n", read_local_file)  # add new lines
urls_line_by_line = urls_line_by_line.replace(
    "www", "https://www")  # make text clickable

# === remove duplicates ===

with open(r"output/" + today_date + "/2-urls_line_by_line.txt", "w", encoding="utf-8") as file_urls_line_by_line:
    print("Cleaning the file...")
    file_urls_line_by_line.write(urls_line_by_line)
lines_seen = set()  # holds lines already seen
# open(r"output/urls_line_by_line_no_dupes.txt", "w").close()
outfile = open(r"output/" + today_date +
               "/3-urls_line_by_line_no_dupes.txt", "w")
line_counter = 0
for line in open(r"output/" + today_date + "/2-urls_line_by_line.txt", "r"):
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        line_counter += 1
        lines_seen.add(line)
outfile.close()

print("File cleaned up. New lines added.")
print("There are:", line_counter, "cars.")

# === tailor the results by using a keyword: brand, model (possibly also engine size etc) ===

# regex_user_input = input("Jak chcesz zawęzić wyniki? Możesz wpisać markę (np. BMW) albo model (np. E39) >>> ") # for now using brand as quesion but user can put any one-word keyword
regex_user_input = ""
regex_user_input = regex_user_input.strip()  # strip front & back
reg = re.compile(regex_user_input)  # matches "KEYWORD" in lines
print("Opening file to search for keyword:", regex_user_input)
counter2 = 0  # another counter to get the # of search results
with open(r'output/' + today_date + '/4-search-output.txt', 'w') as output:  # open file for writing
    print("Searching for keyword...")
    with open(r'output/' + today_date + '/3-urls_line_by_line_no_dupes.txt', 'r', encoding='UTF-8') as no_dupes_file:
        with alive_bar(bar="circles", spinner="dots_waves") as bar:
            for line in no_dupes_file:  # read file line by line
                if reg.search(line):  # if there is a match anywhere in a line
                    output.write(line)  # write the line into the new file
                    counter2 += 1  # counter ++
                    bar()  # progress bar ++
                    # print ("Progress:", counter2)
        if counter2 == 1:
            print("Found", counter2, "result.")
            if platform == "win32":
                toaster.show_toast("otomoto-scraper", "Found " + str(counter2) +
                                   " result.",  icon_path="icons/www.ico", duration=None)
        else:
            print("Found", counter2, "results.")
            if platform == "win32":
                toaster.show_toast("otomoto-scraper", "Found " + str(counter2) +
                                   " results.",  icon_path="icons/www.ico", duration=None)

# === open search results in browser ===

if counter2 != 0:
    # user_choice_open_urls = input("Chcesz otworzyć linki w przeglądarce? [y/n] >>> ")
    user_choice_open_urls = 'n'
    if user_choice_open_urls == 'y':
        with open(r'" + today_date + "/4-search-output.txt', 'r', encoding='UTF-8') as search_results:
            counter3 = 0
            print("Opening URLs in browser...")
            with alive_bar(bar="circles", spinner="dots_waves") as bar:
                for line in search_results:  # go through the file
                    webbrowser.open(line)  # open URL in browser
                    counter3 += 1
                    bar()
        if counter3 != 1:  # correct grammar for multiple (URLs; them; they)
            print("Opened ", str(counter3),
                  " URLs in the browser. Go and check them before they go 404 ;)")
            if platform == "win32":
                toaster.show_toast("otomoto-scraper", "Opened " + str(counter3) +
                                   " URLs.",  icon_path="icons/www.ico", duration=None)
        else:  # correct grammar for 1 (URL; it)
            print("Opened", counter3,
                  "URL in the browser. Go and check it before it goes 404 ;)")
            if platform == "win32":
                toaster.show_toast("otomoto-scraper", "Opened " + str(counter3) +
                                   " URL.",  icon_path="icons/www.ico", duration=None)
    else:
        # print ("Ok - URLs saved in 'output/search-output.txt' anyway.")
        print("Ok - URLs saved in a file.")
        # print("Script run time:", datetime.now()-start)
        # sys.exit()
else:
    print("No search results found.")

# === compare files === 

try:
    file_previous_run = open('output/' + previous_date + '/4-search-output.txt', 'r')
    file_current_run = open('output/' + today_date + '/4-search-output.txt', 'r')

    f1 = [x for x in file_previous_run.readlines()]
    f2 = [x for x in file_current_run.readlines()]

    diff = [line for line in f1 if line not in f2] # lines present only in f1
    diff1 = [line for line in f2 if line not in f1] # lines present only in f2

    # print (diff1) # debug

    # with open('output/' + today_date + '/diff.txt', 'w') as w:
    with open('diff/diff-' + today_date + '.txt', 'w') as w:
        for item in diff1: 
            w.write(item)
            # *NOTE file2 must be > file1

    # file_previous_run.close()
    # file_current_run.close()

except IOError:
    print("First run. Can't diff.")

# === run time ===

print("Script run time:", datetime.now()-start)