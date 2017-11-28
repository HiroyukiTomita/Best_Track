#Best Track#  
---  
a command line tool to read RSMC Best track data  
 
#Data#   
RSMC Tokyo Typhoon center :  
http://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html  
To get data file  
`wget http://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/Besttracks/bst_all.zip`  
`unzip bst_all.zip`  

#Usage#  
`USAGE:  ./best_track.py  [ VAR | GRADE | HEADER | DATA ]  [ TCID | YY | ALL ] [sep]`  
  
#Parameter Description#  
#argv1: Command#  
-VAR              : list variables in data  
-GRADE              : list grade (2-9)   
-HEADER              : list header informaion  
-DATA              : list data for all variables  
-DATA:var1,var2... : list data for specific variables  
   
#argv2: Target typhoon#  
-TCID: tropical cyclon number ID (TCID)  
-YY: 2digit year (YY)   
-ALL: All tropical cyclones (default)  
   
#argv3: Separator for output#  
-' ': space (default)  
-',': comma  
  
#Example#  
To list header for tyhoons in 2010  
`./best_track.py HEADER 10`  
   
To list data for all variables for typhoon 1013 (Megi)  
`./best_track.py DATA 1013` 
  
To list time and pressure data for tyhoon 1013 (Megi)  
`./best_track.py DATA:time,p 1013`  
