#!/usr/bin/env python
# -*- coding: utf-8 -*-

#RiskIQ script to interact with the passivetotal API to hunt for hosts impacted by Sunburst
#API Documentation: https://api.riskiq.net/api/
#author__ = 'Cory Kennedy (cory@riskiq.com)'
#version__ = '1.0.0'
import requests
import json
import os
import time
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

class style():
    BLINK = "\033[5m"
    BLACK = '\033[30m'
    FAIL = '\033[91m'
    LRED='\033[93m'
    BRED = '\033[1;31m'
    RED = '\033[0;31m'
    ORANGE = '\033[0;33m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    HACKER='\033[0;100m'
    BCYAN='\033[1;36m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    On_Black='\033[40m'       # Black
    On_Red='\033[41m'         # Red
    On_Green='\033[42m'       # Green
    On_Yellow='\033[43m'      # Yellow
    BACKBLUE='\033[44m'        # Blue
    On_Purple='\033[45m'      # Purple
    On_Cyan='\033[46m'        # Cyan
    On_White='\033[47m'       # White



class RiskIQ_Sunburst_Finder():
    def __init__(self,username, key ):
        self.username = username
        self.key = key
        self.headers = {'Content-Type': 'application/json'}
        
         
    def show_menu(self): 
        print (style.CYAN+'''  
                                                                                                                               
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
     /Nm-:syyyyyyyyd:   hMMMMNy:` -sMMMMMN/   `/y++NMo   /Mh:`     `.:/:sd.''')     
        print (style.MAGENTA+'''    +Nm-        `.o+   .mMMmo-   `sNMMMMm:    ``  -md`   ss`    :shmNmo:/mm-    
   /MN:   ://+sydmy++--hNd+.   `/dNMMMMm-       `-sdo+:-oh`   `sNMMMMMm. :mm.   
  -NN:   /NMMMMMN+` `/ho-`     .::::sMm-     `-+hNy. `-dMo    sMMMmy+dM+  :Nd`  
 `mN+   /NMMMMMM+   `o.             .d-   `  `hMMh`   /NMy    yMMy`  .y.  -NMs  
 oMo   :mMMMMMMm`  `sMs...-::-`   `/h:   oy`  :NM:   /NMMN/   `+hh.   `  .dMMM-''') 
        print (style.RED+"`NN.  :mMMMMMMM+  `yMMMNmNms-  `-odN/  `oMMh`  yh   +NMMMMN+`    .`     :dMMMMh") 
        print (style.RED+"+Mh  /NMMMMMMMMo `hMMMMMNs-  .+hNMMo  `sMMMMo` -h. +NMMMMMMMdo-.`````  `hMMMMMM.")
        print (style.RED+"hMM++NMMMMMMMMMM+yMMMMms-  -smMMMMo  `yMMMMMMm+-hyoNMMMMMMMMMMMmddddd- `hMMMMMM/")
        print (style.RED+"NMMMMMMMMMMMMMMMMMMMMy. `:yNMMMMMd  .hMMMMMMMMMdhMMMMMMMMMMMMMMMMMMMMm/sMMMMMMMs")
        print (style.RED+"+                     ``-:          ./")
        print (style.RED+"+ooooooooooooooooooo-`.+oooooooooo/.ooooooooooooooooooooooooooooooooooooooooooo/")
        print (style.CYAN+'+----------------+:.:+--------------------------------------------------------+')   
        print (style.BCYAN+"|"+style.BOLD+style.MAGENTA+"         ██████╗ ██╗███████╗██╗  ██╗██╗ ██████╗       "+style.BCYAN+ style.YELLOW+"Sun"+style.FAIL+"BURST "+style.WHITE+"Hunter"+style.BCYAN+"        |"+style.RESET)
        print (style.BCYAN+"|"+style.BOLD+style.MAGENTA+"         ██╔══██╗██║██╔════╝██║ ██╔╝██║██╔═══██╗   "+style.BCYAN+"         ________         |"+style.RESET)
        print (style.BCYAN+"|"+style.BLUE+"         ██████╔╝██║███████╗█████╔╝ ██║██║   ██║  "+style.BCYAN+"    ___  _\_____  \        |"+style.RESET)
        print (style.BCYAN+"|"+style.BLUE+"         ██╔══██╗██║╚════██║██╔═██╗ ██║██║▄▄ ██║  "+style.BCYAN+"    \  \/ //  ____/        |"+style.RESET)  
        print (style.BCYAN+"|"+style.CYAN+"         ██║  ██║██║███████║██║  ██╗██║╚██API█╔╝ "+style.BCYAN+"      \   //       \        |"+style.RESET)
        print (style.BCYAN+"|"+style.CYAN+"         ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚══▀▀═╝ "+style.RESET+style.BCYAN+"        \_/ \_______ \       |"+style.RESET)
        print (style.BCYAN+"|"+style.BCYAN+"                                                                    \/       |"+style.RESET)                         
        print (style.RESET+style.BLUE+"|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█"+style.RESET+style.WHITE+" MENU "+style.BLUE+"█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|")
        print (style.RESET+style.BLUE+"⣿"+style.UNDERLINE+style.YELLOW+" ° Sun"+style.FAIL+"BURST"+style.WHITE+"Hunter"+style.BLUE+style.UNDERLINE+"                                                            "+style.RESET+style.BLUE+"⣿")    
        print (style.RESET+style.BLUE+"⣿                                                                             ⣿")
        print (style.BOLD+style.GREEN+"①"+style.BLUE +" ", style.RESET+style.BLUE+"   ["+style.GREEN+"Keyword"+style.RESET+style.BLUE+"]", style.RESET+style.WHITE+"- SSL Certificate Keyword or Hostname Search "+style.BLUE+   "                 ⣿")
        print (style.RESET+style.BOLD+style.GREEN+"②"+style.RESET+style.BLUE+ " ", "   ["+style.GREEN+"File Upload"+style.RESET+style.BLUE+"]", style.RESET+style.WHITE+"- Upload list of hostnames to search "+style.RESET   +style.BLUE+ "                     ⣿")
        print (style.RESET+style.BLUE+"⣿                                                                             ⣿")
        print (style.RESET+style.BLUE+"⣿"+style.UNDERLINE+style.CYAN+" ° SSL Certficate Extras"+"                                                     "+style.RESET+style.BLUE+"⣿")
        print (style.RESET+style.BLUE+"⣿                                                                             ⣿")
        print (style.BOLD+style.CYAN+"③"+style.BLUE +" ", style.RESET+style.BLUE+"   ["+style.CYAN+"Fieldname"+style.RESET+style.BLUE+"]", style.RESET+style.WHITE+"- SSL Certificate Fieldname Search "+style.BLUE+   "                         ⣿")
        print (style.RESET+style.BLUE+"⣿                                                                             ⣿")
        print (style.RESET+style.BLUE+"⣿"+style.UNDERLINE+style.GREEN+" RiskIQ SunBurst Threat Intelligence"+"                                         "+style.RESET+style.BLUE+"⣿")
        print (style.RESET+style.BLUE+"⣿   https://community.riskiq.com/article/b5b13e5d                             ⣿")
        print (style.RESET+style.BLUE+"⣿   https://community.riskiq.com/article/c98949a2                             ⣿")
        print (style.RESET+style.BLUE+"⣿   https://community.riskiq.com/article/a786a113                             ⣿")
        print (style.RESET+style.BLUE+"⣿   https://community.riskiq.com/article/a58a63e9                             ⣿")
        print (style.RESET+style.BLUE+"⣿                                                                             ⣿")
        print (style.YELLOW+"Ⓠ"+style.RESET+style.BLUE+ " ", style.RESET+style.YELLOW+"° Q"+style.RESET+style.WHITE+"uit"+style.RESET+style.BLUE+ "                                                                     ⣿")
        print (style.BLUE+"⣿   "+style.CYAN+style.UNDERLINE+"                     "+style.RESET+style.BLUE+"                                                     ⣿")
        print (style.BLUE+"+▒▓█"+style.CYAN+style.UNDERLINE+"► Search History[5] ◄"+style.RESET+style.BLUE+"█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░+")
        for root, dirs, files in os.walk("output/"):
            for dirs in dirs[:5]:
                print (style.RESET+style.CYAN+"   "+dirs)

    
    def sunburst_field(self):
        field = WordCompleter(['issuerSurname', 'subjectOrganizationName', 'issuerCountry', 'issuerOrganizationUnitName', 'fingerprint', 'subjectOrganizationUnitName', 'serialNumber', 'subjectEmailAddress', 'subjectCountry', 'issuerGivenName', 'subjectCommonName', 'issuerCommonName', 'issuerStateOrProvinceName', 'issuerProvince', 'subjectStateOrProvinceName', 'sha1', 'subjectStreetAddress', 'subjectSerialNumber', 'issuerOrganizationName', 'subjectSurname', 'subjectLocalityName', 'issuerStreetAddress', 'issuerLocalityName', 'subjectGivenName', 'subjectProvince', 'issuerSerialNumber', 'issuerEmailAddress', 'name', 'issuerAlternativeName', 'subjectAlternativeName'])
        fields = prompt('1 [SSL Certificate Fields] -  Enter Field to search: (press tab to show list) ' , completer=field).strip('\n')
        search = search = input(style.RESET+style.CYAN+'1 [SSL Certificate query]'+style.RESET+style.CYAN+' Enter search terms: '+style.WHITE).strip('\n')
        data = {"field": fields, "query": search}
        url = ('https://api.passivetotal.org/v2/ssl-certificate/search')
        r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
        response = json.loads(r.text)
        
        os.makedirs("output/"+search, exist_ok=True)
        jsonout = open("output/"+search+"/"+search+".json", "w")
        jsonout.write(json.dumps(response, indent=4, sort_keys=True))
        #print(style.WHITE+json.dumps(response, indent=4, sort_keys=True)+"\n")
        print(style.YELLOW+"NOTE: Please wait output is been saved to " + ".output/"+search+"/"+search +".json'\n")
        print(style.CYAN+'You searched for:',style.WHITE+"Certificate Field: "+fields +style.YELLOW+" & "+style.WHITE+search+'\n')
        print(style.CYAN+'    Sample Results for query:',style.WHITE+fields+","+search+'\n')
        print(style.GREEN+"Still Processing... Please hold\n")
        for sha in response['results']:
            search2 = sha['sha1']
            for line in search2:
                data = {"query": search2}
                url = ('https://api.passivetotal.org/v2/ssl-certificate/history?sort=firstSeen&order=asc')
                r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
                response = json.loads(r.text)
            for hip in response['results'][0]['ipAddresses']:
                jsonout = open("output/"+search+"/"+search+".json", "a")
                jsonout.write(json.dumps(response, indent=4, sort_keys=True))
        print(style.GREEN+"     Here is a sample of what we found!")    
        print("         "+style.WHITE+json.dumps(response, indent=4, sort_keys=True))
        print(style.RESET) 


    def sunburst_key(self):
        search = input(style.RESET+style.CYAN+'[SSL|Keyword]'+style.RESET+style.CYAN+' Enter search terms: '+style.WHITE).strip('\n')
        data = {"query": search}
        whitelist = open('whitelists/whitelist.txt', 'r')
        sunlist = open('whitelists/sunlist.txt', 'r')
        url = ('https://api.passivetotal.org/v2/ssl-certificate/search/keyword?sort=firstSeen&order=asc')
        r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
        response = json.loads(r.text)
        os.makedirs("output/"+search, exist_ok=True)
        string = '''
                                *Processing Search*

                                       RiskIQ
                               //THREAT*INTELLIGENCE''                                         
                            *###############%%##%%%%%%%%#                          
                          (###########/       /%%%%%%%%%%%#              
                        ((######/*                 (%%%%%%###             
                       ((((##//    ,((((((((#####*    %%%###((            
                      (((((//%%%%%%%%%%(((((############((#((((           
                     ((((///#%%%%%%%%%%%%%%%%%############%////(          
                   %%(((////##%%%%*               /######%%%%(((//        
                 %%%%((/////                             (%%%%%((((/      
               %%%%%%(/////*                             ////%%%#(((((    
              %%%%%%%((((((/                             //////%%(####(   
             %%%%%%%# ((((((*                           (((((((,%%((#(##  
             %%%%%%*  ((((((**                         ######**  %((((((  
            %%%%%%%*   (((((/**                       %%%%%***   #(((((/  
             %%%%%**    (((((***                     %%%%****    #(((((*  
             #%%%%**     *((((****                 ###/*****     (((((**  
             .####***      ((((*****             ##//*****      ((((***.  
              ,####****      ((/****//*       /#/////***      ((((****,   
                ####***//,     (/***////// (/////////*     *(((/*****     
                  ((#**//////**  (**//**////////////  ((///////////       
                    /((///////(((((@corykennedy*/**//////////////         
                        ((////(((((((((((CS((**********///////" 
                           '''          
        for char in string:
            print(style.BLUE+char, end='')
            time.sleep(.0025)
        print('\n')     
        print(style.GREEN+"Still Processing... Please hold")
        print('\n')    
        print(style.YELLOW+"    NOTE: Full results have been saved to " + ".output/"+search+"/"+search +".json'\n")       
        print('\n')
        for focus in response['results']:
            search2 = focus['focusPoint']
            #for line in search2:
            data = {"query": search2}
            url = ('https://api.passivetotal.org/v2/ssl-certificate?sort=firstSeen&order=asc')
            r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
            response = json.loads(r.text)
            jsonout = open("output/"+search+"/"+search+".json", "a")
            jsonout.write('{')
            jsonout.write('\n')
            jsonout.write('     "ssl-certificate": [')
            jsonout.write('\n')
            jsonout.write(json.dumps(response, indent=4, sort_keys=True))
            jsonout.write("],")
            for sha in response['results']:
                search3 = sha['sha1']
                data = {"query": search3}
                url = ('https://api.passivetotal.org/v2/ssl-certificate/history?sort=firstSeen&order=asc')
                r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
                response = json.loads(r.text)
                jsonout = open("output/"+search+"/"+search+".json", "a")
                jsonout.write('\n')
                jsonout.write('     "ssl-certificate-history": [')
                jsonout.write('\n')
                jsonout.write(json.dumps(response, indent=4, sort_keys=True))
                jsonout.write("],")
            for ip in response['results']:
                with open('whitelists/whitelist.txt', 'r') as f:
                    iocline = [line.rstrip() for line in f]
                    match = ip['ipAddresses']
                    if ip not in iocline:
                        for value in match:
                            data = {"query": value}
                            url = ('https://api.passivetotal.org/v2/host-attributes/components')
                            r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
                            response = json.loads(r.text)
                            jsonout = open("output/"+search+"/"+search+".json", "a")
                            jsonout.write('\n')
                            jsonout.write(  '"components": [')
                            jsonout.write('\n')
                            jsonout.write(json.dumps(response, indent=4, sort_keys=True))
                            jsonout.write("],")
                        for sunmatch in response['results']:
                            with open('whitelists/sunlist.txt', 'r') as f:
                                sunline = [line.rstrip() for line in f]
                                suncomp = sunmatch['label']
                                sunaddress = sunmatch['address']
                                if suncomp in sunline:
                                    print(style.UNDERLINE+style.CYAN+'!!!Potential SolarWinds Orion Sunburst item found!!! Logging to results.')
                                    print(style.RESET+style.GREEN+'[IP] '+style.WHITE+ sunaddress+style.GREEN+' [Component] '+style.FAIL+suncomp+style.RESET )
                                    jsonout = open("output/"+search+"/"+search+".json", "a")
                                    jsonout.write('\n')
                                    jsonout.write('Potential SolarWinds Orion Sunburst item found!')
                                    

        print(style.GREEN+"     Here is a sample of what we found!")    
        print("         "+style.WHITE+json.dumps(response, indent=4, sort_keys=True))
        print(style.RESET)        
        
        
            
    def sunburst_file(self):
        whitelist = open('whitelists/whitelist.txt', 'r')
        sunlist = open('whitelists/sunlist.txt', 'r')
        fupload = input(style.RESET+style.CYAN+'[File Upload]'+style.RESET+style.CYAN+' Enter filename: '+style.WHITE).strip('\n')
        with open(fupload) as f:
            line = [line.rstrip() for line in f]
            file = open(fupload,"r")
            Counter = 0
            Content = file.read() 
            CoList = Content.split("\n")
            for i in CoList: 
                if i: 
                    Counter += 1
            print(style.GREEN+"     Found:",Counter,"values in file",fupload) 
            print(style.CYAN+"     Searching using the following: ")
            for lined in line:
                print(style.WHITE+"                                   "+lined) 
        for search in line:
            data = {"query": search}
            url = ('https://api.passivetotal.org/v2/ssl-certificate/search/keyword')
            r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
            response = json.loads(r.text)
            os.makedirs("output/"+search, exist_ok=True)        
            print(style.YELLOW+"    NOTE: Full results have been saved to " + style.UNDERLINE+style.CYAN+".output/"+search+"/"+search +".json'"+style.RESET)
            print('\n')       
            for focus in response['results']:
                search2 = focus['focusPoint']
                #for line in search2:
                data = {"query": search2}
                url = ('https://api.passivetotal.org/v2/ssl-certificate?sort=firstSeen&order=asc')
                r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
                response = json.loads(r.text)
                jsonout = open("output/"+search+"/"+search+".json", "a")
                jsonout.write('{')
                jsonout.write('\n')
                jsonout.write('     "ssl-certificate": [')
                jsonout.write('\n')
                jsonout.write(json.dumps(response, indent=4, sort_keys=True))
                jsonout.write("],")
                for sha in response['results']:
                    search3 = sha['sha1']
                    data = {"query": search3}
                    url = ('https://api.passivetotal.org/v2/ssl-certificate/history?sort=firstSeen&order=asc')
                    r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
                    response = json.loads(r.text)
                    jsonout = open("output/"+search+"/"+search+".json", "a")
                    jsonout.write('\n')
                    jsonout.write('     "ssl-certificate-history": [')
                    jsonout.write('\n')
                    jsonout.write(json.dumps(response, indent=4, sort_keys=True))
                    jsonout.write("],")
                for ip in response['results']:
                    with open('whitelists/whitelist.txt', 'r') as f:
                        iocline = [line.rstrip() for line in f]
                        match = ip['ipAddresses']
                        if ip not in iocline:
                            for value in match:
                                data = {"query": value}
                                url = ('https://api.passivetotal.org/v2/host-attributes/components')
                                r = requests.get(url,  headers=self.headers, auth=(self.username, self.key), data=json.dumps(data))
                                response = json.loads(r.text)
                                jsonout = open("output/"+search+"/"+search+".json", "a")
                                jsonout.write('\n')
                                jsonout.write(  '"components": [')
                                jsonout.write('\n')
                                jsonout.write(json.dumps(response, indent=4, sort_keys=True))
                                jsonout.write("],")
                            for sunmatch in response['results']:
                                with open('whitelists/sunlist.txt', 'r') as f:
                                    sunline = [line.rstrip() for line in f]
                                    suncomp = sunmatch['label']
                                    sunaddress = sunmatch['address']
                                    if suncomp in sunline:
                                        print(style.UNDERLINE+style.CYAN+'!!!Potential SolarWinds Orion Sunburst item found!!! Logging to results.')
                                        print(style.RESET+style.GREEN+'[IP] '+style.WHITE+ sunaddress+style.GREEN+' [Component] '+style.FAIL+suncomp+style.RESET )
                                        jsonout = open("output/"+search+"/"+search+".json", "a")
                                        jsonout.write('\n')
                                        jsonout.write('Potential SolarWinds Orion Sunburst item found!')
        print(style.RESET)        

            
def menu():
    try:
        from secrets import EMAIL, APIKEY
        sunburst_finder = RiskIQ_Sunburst_Finder(EMAIL, APIKEY)

    except:
        print("")
        print(style.YELLOW+"Note: Below values can be found here: https://community.riskiq.com/settings")
        print (style.BLACK+"----------------------------------------------------------------")
        username = input(style.GREEN+'Enter your https://community.riskiq.com email address: ')
        key = input(style.CYAN+'Enter your https://community.riskiq.com API key: ')
        sunburst_finder = RiskIQ_Sunburst_Finder(username, key)

    while True:
        
        sunburst_finder.show_menu()
        print ('\n')
        choice = input(style.RESET+style.CYAN+'[MENU]'+style.RESET+style.BLUE+style.BOLD+' Enter Menu Selection' +style.RESET+style.BOLD+style.CYAN+' ▶ '+style.RESET).lower()
        print ('\n')
        if choice == '1':
            sunburst_finder.sunburst_key()
        elif choice == '2':
            sunburst_finder.sunburst_file()
        elif choice == '3':
            sunburst_finder.sunburst_field()   
        elif choice == 'q':
            return
        else:
            print(f'Hmmm: <{choice}>,try again, or dont. Whatever')
 
if __name__ == '__main__':
    menu()
