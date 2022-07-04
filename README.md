# otomoto_olx-scraper

![](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-blue)

>Scrape car offers from OTOMOTO․pl & OLX․pl and run IFTTT automation (eg. send email; add a to-do task) when new car(s) matching search criteria is found. With support for native macOS & Windows 10 notifications. 

<!-- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cumanos sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. -->

## Screenshots

![Windows](https://user-images.githubusercontent.com/6877391/111393389-f952f500-86b8-11eb-92d7-096ce4964b48.png)
![macOS](https://user-images.githubusercontent.com/6877391/111393391-f9eb8b80-86b8-11eb-98a3-4e908790656d.png)

## How to use

<i>Note: There are 2 scripts for OTOMOTO — they're the same except for the URL. Using both files (or creating `otomoto3.py`, `otomoto4.py`, etc.) is useful when looking for a car in different location or using different search criteria altogether. Same applies for OLX.</i> 

### macOS 
How to chain the scripts:
```sh
# automate.sh
cd "PATH/otomoto_olx-scraper/otomoto1"
python3 otomoto1.py
cd ..
cd otomoto2
python3 otomoto2.py
cd .. 
cd olx1
python3 olx1.py
cd .. 
cd olx2
python3 olx2.py
```
Add ^ to Automator, export as Application and then run in the background via Script Editor.

<!-- ## Roadmap

- lorem ipsum -->

## Release History

- 0.15: Updated the `otomoto1.py` & `otomoto2.py` scripts to handle first run properly — create folders, empty variables. 
- 0.14: Updated the URLs and BeautifulSoup's selectors so the script works again for OTOMOTO.
- 0.13: Two files per each platform to support searches in two different locations; improved pagination support on OLX; improved regex; more data sent to IFTTT.
- 0.12.4: Fixed a bug that prevented the script from running because there was only one OTOMOTO subpage to scrape.
- 0.12.3: Disabled the option to open browser with search results page; changed URLs.
- 0.12.2: Added date as 2nd parameter to IFTTT automation. 
- 0.12.1: Tiny bug fix around certificate issue on macOS when requesting a URL.
- 0.12: Added OLX․pl support 🎉
- 0.11.1: Replaced old `win10toast` module with `win10toast-click`.
- 0.11: Improved Windows 10 notifications to open URL on-click using [win10toast-click](https://github.com/vardecab/win10toast-click); added URL shortening module; renamed a few variables; cleaned up project structure.
- 0.10: Pagination support - script will scrape only the # of pages that are available for certain search query instead of relying on hard-coded value. Also: turned off notifications when there are no new cars; fixed a bug that prevented adding more than 32 cars to the file.
- 0.9: Cleaned the code - renamed variables & function, reduced number of `.txt` files used; fixed a bug that was causing false positivies because of empty lines, `\n` characters and duplicates; *broke* keyword-search functionality which is not being utilized right now anyway. 
- 0.8: Changed URL; attempt to hide API key; changes to notifications.
- 0.7: Notifications (Windows & macOS; showing script's run time in seconds; improved regex formula to remove IDs at the end of URLs. 
- 0.6: Sending email via IFTTT if new car is found.
- 0.5: Disabled user input once again - hardcoded values; implemented file diff; files & folders are created with unique ID.
- 0.4: Re-enabled user input; minor tweak to URL params; improved compatibility with macOS.
- 0.3: Disabled user input; improved compatibility with macOS.
- 0.2: Opening URLs from search results. Windows 10 notification when opening URLs; delaying crawling; renamed some variables for better clarity.
- 0.1: Initial release.

## Versioning

Using [SemVer](http://semver.org/).

## License

![](https://img.shields.io/github/license/vardecab/otomoto_olx-scraper)
<!-- GNU General Public License v3.0, see [LICENSE.md](https://github.com/vardecab/PROJECT/blob/master/LICENSE). -->

## Acknowledgements

### Modules
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [alive-progress](https://github.com/rsalmei/alive-progress)
- [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- [win10toast-persist](https://github.com/tnthieding/Windows-10-Toast-Notifications)
- [win10toast-click](https://github.com/vardecab/win10toast-click)
- [pync](https://github.com/SeTeM/pync)
- [GD Shortener](https://github.com/torre76/gd_shortener)
<!-- - [termcolor](https://pypi.org/project/termcolor/) -->

### Stack Overflow
- [certificate issue fix](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)
- [click Windows 10 notification to open URL](https://stackoverflow.com/questions/63867448/interactive-notification-windows-10-using-python)

### Other
- [Flaticon / Freepik](https://www.flaticon.com/)
- [IFTTT](https://ifttt.com/)
- [Connect a Python Script to IFTTT by Enrico Bergamini](https://medium.com/mai-piu-senza/connect-a-python-script-to-ifttt-8ee0240bb3aa)
- [Use IFTTT web requests to send email alerts by Anthony Hartup](https://anthscomputercave.com/tutorials/ifttt/using_ifttt_web_request_email.html)

## Contributing

![](https://img.shields.io/github/issues/vardecab/otomoto_olx-scraper)

If you found a bug or want to propose a feature, feel free to visit [the Issues page](https://github.com/vardecab/otomoto_olx-scraper/issues).