![](https://raw.githubusercontent.com/NoDataFound/RiskIQ.SunBurst.Hunter/master/images/Main.png)

SunBurst Hunter 
===================

![](https://img.shields.io/badge/@CoryKennedy-SunBurst%7CResearch-blue)

Introduction
------------


**The Purpose of this research tool** is to provide a Python client into RiskIQ API
services. This tool currently provides support for the following services:

- SSL Certificates (search and details)
  - Search by keyword or hostname
  - File upload of list of hostnames
- SSL Certificates history (SHA, IP, etc..)
- Component History ("Windows Remote Desktop" for example)


Installation
------------



    $ pip install -r requirements.txt



Setup
-----

First-time setup requires configuring your API token and private key for authentication:

    $ mv sample_secrets.py secrets.py

Complete required fields

*Note: values can be found at: https://community.riskiq.com/settings*

    EMAIL = 'riskiq.com email'
    APIKEY = 'API Key'



Usage

-----
All menu selections provide addtional instruction.  
     *File uploads require just a name 'file.txt'*  

    $  python RiskIQ.Sunburst.Hunter.py

      +----------------------------------------------------------------+
      |   .______       __       _______. __  ___  __    ______        |
      |   |   _  \     |  |     /       ||  |/  / |  |  /  __  \       |
      |   |  |_)  |    |  |    |   (----`|  '  /  |  | |  |  |  |      |
      |   |      /     |  |     \   \    |    <   |  | |  |  |  |      |
      |   |  |\  \----.|  | .----)   |   |  .  \  |  | |  `--'  '--.   |
      |   | _| `._____||__| |_______/    |__|\__\ |__|  \_____\_API_|  |
      |                                               SunBURST Hunter  |
      |⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿MENU⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿|
      ⣿ ° SunBURSTHunter                                               ⣿
      ⣿                                                                ⣿
    1 ⣿    [Keyword] - SSL Certificate Keyword or Hostname Search      ⣿
    2 ⣿    [File Upload] - Upload list of hostnames to search          ⣿
      ⣿                                                                ⣿
      ⣿ ° SSL Certficate Extras                                        ⣿
      ⣿                                                                ⣿
    3 ⣿    [Fieldname] - SSL Certificate Fieldname Search              ⣿
      ⣿                                                                ⣿
    Q ⣿ ° Quit                                                         ⣿
      ⣿                                                                ⣿
      +⣿⣿⣿| Search History[5] |⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿+
             my.searches

    [MENU] Enter Menu Selection >>


# Sample Output
![](https://raw.githubusercontent.com/NoDataFound/RiskIQ.SunBurst.Hunter/master/images/find_from_dga.png)


# Useage Examples

### Hostname search

![](https://raw.githubusercontent.com/NoDataFound/RiskIQ.SunBurst.Hunter/master/images/Hostname_Search.gif)

### File Upload

![](https://raw.githubusercontent.com/NoDataFound/RiskIQ.SunBurst.Hunter/master/images/File_Search.gif)

### Fieldname Search
![](https://raw.githubusercontent.com/NoDataFound/RiskIQ.SunBurst.Hunter/master/images/Fieldname_Search.gif)

#### Legal disclaimer:
Usage of RiskIQ.Sunburst.Hunter.py is at your own risk. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.
