![](https://github.com/NoDataFound/RiskIQ.SunBurst.Hunter/blob/master/images/Main.png)
![](https://github.com/NoDataFound/RiskIQ.SunBurst.Hunter/blob/master/images/SunburstNotification.png)

SunBurst Hunter 
===================

![](https://img.shields.io/badge/@CoryKennedy-SunBurst%7CResearch-blue)

In the news!
------------
Original Tweet - https://twitter.com/CoryKennedy/status/1339707931235856384

- https://www.bleepingcomputer.com/news/security/the-solarwinds-cyberattack-the-hack-the-victims-and-what-we-know/
- https://www.securityweek.com/continuous-updates-everything-you-need-know-about-solarwinds-attack

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
    misp_url = 'https://your.misp'
    misp_key = 'enter your MISP user API key'
    misp_verifycert = False


Usage

-----
All menu selections provide addtional instruction.  
     *File uploads require just a name 'file.txt'*  

    $  python RiskIQ.Sunburst.Hunter.py
```
                                   `.-----..`
                          `-/oydmNMMMMMMMMMMMNNmhso/.
                      -+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/.
                  .+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNms:`
               .+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMNy:
             -yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.:odMMMMMMMMMMMMmo.
           :hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`   hMMMMMMMMMMMMMMNs.
         -hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy`   /NMMMMMMMMMMMMMMMMNo`
       `sNMMMMMMMMMMMm+mMMMMMMMMMMNdMMMMMMMMo`   /NMMMMohMMMMMMMNmmdmNm/
      -dNNMMMMMMMMMMN: .dMMMMMMMd+-sMMMMMMMo    +NMMMMo `sMMNds:..```.:ss`
     /Nm-:syyyyyyyyd:   hMMMMNy:` -sMMMMMN/   `/y++NMo   /Mh:`     `.:/:sd.
    +Nm-        `.o+   .mMMmo-   `sNMMMMm:    ``  -md`   ss`    :shmNmo:/mm-
   /MN:   ://+sydmy++--hNd+.   `/dNMMMMm-       `-sdo+:-oh`   `sNMMMMMm. :mm.
  -NN:   /NMMMMMN+` `/ho-`     .::::sMm-     `-+hNy. `-dMo    sMMMmy+dM+  :Nd`
 `mN+   /NMMMMMM+   `o.             .d-   `  `hMMh`   /NMy    yMMy`  .y.  -NMs
 oMo   :mMMMMMMm`  `sMs...-::-`   `/h:   oy`  :NM:   /NMMN/   `+hh.   `  .dMMM-
`NN.  :mMMMMMMM+  `yMMMNmNms-  `-odN/  `oMMh`  yh   +NMMMMN+`    .`     :dMMMMh
+Mh  /NMMMMMMMMo `hMMMMMNs-  .+hNMMo  `sMMMMo` -h. +NMMMMMMMdo-.`````  `hMMMMMM.
hMM++NMMMMMMMMMM+yMMMMms-  -smMMMMo  `yMMMMMMm+-hyoNMMMMMMMMMMMmddddd- `hMMMMMM/
NMMMMMMMMMMMMMMMMMMMMy. `:yNMMMMMd  .hMMMMMMMMMdhMMMMMMMMMMMMMMMMMMMMm/sMMMMMMMs
+                     ``-:          ./
+ooooooooooooooooooo-`.+oooooooooo/.ooooooooooooooooooooooooooooooooooooooooooo/
+----------------+:.:+--------------------------------------------------------+
|         ██████╗ ██╗███████╗██╗  ██╗██╗ ██████╗       SunBURST Hunter        |
|         ██╔══██╗██║██╔════╝██║ ██╔╝██║██╔═══██╗            ________         |
|         ██████╔╝██║███████╗█████╔╝ ██║██║   ██║      ___  _\_____  \        |
|         ██╔══██╗██║╚════██║██╔═██╗ ██║██║▄▄ ██║      \  \/ //  ____/        |
|         ██║  ██║██║███████║██║  ██╗██║╚██API█╔╝       \   //       \        |
|         ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚══▀▀═╝         \_/ \_______ \       |
|                                                                    \/       |
|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█ MENU █▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|
⣿ ° SunBURSTHunter                                                            ⣿
⣿                                                                             ⣿
①     [Keyword] - SSL Certificate Keyword or Hostname Search                  ⣿
②     [File Upload] - Upload list of hostnames to search                      ⣿
⣿                                                                             ⣿
⣿ ° SSL Certficate Extras                                                     ⣿
⣿                                                                             ⣿
③     [Fieldname] - SSL Certificate Fieldname Search                          ⣿
⣿                                                                             ⣿
⣿ RiskIQ SunBurst Threat Intelligence                                         ⣿
⣿   https://community.riskiq.com/article/b5b13e5d                             ⣿
⣿   https://community.riskiq.com/article/c98949a2                             ⣿
⣿   https://community.riskiq.com/article/a786a113                             ⣿
⣿   https://community.riskiq.com/article/a58a63e9                             ⣿
⣿                                                                             ⣿
Ⓠ  ° Quit                                                                     ⣿
⣿                                                                             ⣿
+▒▓█► Search History[5] ◄█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░+


[MENU] Enter Menu Selection ▶
```

# Sample Output
![](https://github.com/NoDataFound/RiskIQ.SunBurst.Hunter/blob/master/images/find_from_dga.png)


# Useage Examples

### Hostname search

![](https://github.com/NoDataFound/RiskIQ.SunBurst.Hunter/blob/master/images/Hostname_Search.gif)

### File Upload

![](https://github.com/NoDataFound/RiskIQ.SunBurst.Hunter/blob/master/images/File_Search.gif)

### Fieldname Search
![](https://github.com/NoDataFound/RiskIQ.SunBurst.Hunter/blob/master/images/Fieldname_Search.gif)

#### Legal disclaimer:
Usage of RiskIQ.Sunburst.Hunter.py is at your own risk. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.
