#!/usr/bin/env python2
#
# read_bst_all
#----------------------------------------------------------------------- 
import sys

def list_data(n1,num):
    n2 = n1 + int(num)
    count = n1 
    while count < n2:
      print bst_all_lines[count].strip()
      count += 1

def usage():
    name = sys.argv[0]
    print "----------------------------------------------"
    print "USAGE: ", name, " [ VAR | GRADE | HEADER | DATA ]  [ TCID | YY | ALL ] [sep]"
    print ""
    print "       argv1: Command:"
    print "                   VAR              : list variables in data"
    print "                 GRADE              : list grade (2-9) "
    print "                HEADER              : list HEADER info"
    print "                  DATA              : list data for all variables"
    print "                  DATA:var1,var2... : list data for specific variables"
    print " "
    print "       argv2: Target typhoon"
    print "                  TCID: tropical cyclon number ID (TCID)"
    print "                    YY: 2digit year (YY) "
    print "                   ALL: All tropical cyclones (default)"
    print " "
    print "       argv3: Separator for output"
    print "                   ' ': space (default)"
    print "                   ',': comma"
    print ""
    print "----------------------------------------------"
    sys.exit()

def variables():
    print "----------------------------------------------"
    print " VARIABLES:"
    print "   time: Time of analysis (yymmddhh)"
    print "  grade: 2-9 (see doc for detail)"
    print "    lat: Latitude of the center (0.1deg.)"
    print "    lon: Longitude of the center (0.1deg.)"
    print "      p: Central pressure (hPa)"
    print "     ws: Maximum sustained wind speed (kt)"
    print "----------------------------------------------"
    sys.exit()

def grades():
    print "----------------------------------------------"
    print " GRADES:"
    print "   1: Not used"
    print "   2: Tropical Depression (TD)"
    print "   3: Tropical Storm (TS)"
    print "   4: Severe Tropical Storm (STS)"
    print "   5: Extra-tropical Cyclone (L)"
    print "   7: Just entering into the responsible area of"
    print "      Japan Meteorological Agency (JMA)"
    print "   8: Not used" 
    print "   9: Tropical Cyclone of TS intensity of higher"
    print "----------------------------------------------"
    sys.exit()

def header(bst_all_lines, ityid):
    n=0
    for line in bst_all_lines:
     if line.find('66666') >= 0:
       hline = line.strip()
       col = hline.split()
       tyid = col[1]
       num_data_line = col[2]
       yy = tyid[0:2]
       nstart = n + 1
       if (ityid == tyid):
         print hline
       elif (ityid == "ALL"):
         print hline
       elif (ityid == "NONE") and (iyy == yy):
        print hline
     n += 1

def data(bst_all_lines, ityid):
    sw = 0
    nd = 0
    for line in bst_all_lines:
     if sw == 0:
      if line.find('6666') >= 0:
       hline = line.strip()
       col = hline.split()
       tyid = col[1]
       num_data_line = int(col[2])
       yy = tyid[0:2]
       if (ityid == tyid):
         print hline
         sw = 1
       elif (ityid == "ALL"):
         print hline
         sw = 1
       elif (ityid == "NONE") and (iyy == yy):
         print hline
         sw = 1
     elif sw == 1:
       if (ityid == tyid):
        if nd <= num_data_line-1:
         dline = line.strip()
         print dline
         nd += 1
        else:
         break
       elif (ityid == "ALL"):
        if nd <= num_data_line-1:
         dline = line.strip()
         print dline
         nd += 1
       elif (ityid == "NONE") and (iyy == yy):
        if nd <= num_data_line-1:
         dline = line.strip()
         print dline
         nd += 1
        else:
         sw=0
         nd=0

def data_vars(bst_all_lines, ityid, var_list, sep):
    sw = 0
    nd = 0
    for line in bst_all_lines:
     if sw == 0:
      if line.find('6666') >= 0:
       hline = line.strip()
       col = hline.split()
       tyid = col[1]
       num_data_line = int(col[2])
       yy = tyid[0:2]
       if (ityid == tyid):
         print hline
         sw = 1
       elif (ityid == "ALL"):
         print hline
         sw = 1
       elif (ityid == "NONE") and (iyy == yy):
         print hline
         sw = 1
     elif sw == 1:
       if (ityid == tyid):
        if nd <= num_data_line-1:
         dline = line.strip()
         dline_var = dline.split()
         out_list=[]
         out_list =  make_out_list(dline_var,var_list, out_list)
         out = sep.join(out_list)
         print out
         nd += 1
        else:
         break
       elif (ityid == "ALL"):
        if nd <= num_data_line-1:
         dline = line.strip()
         print dline
         nd += 1
       elif (ityid == "NONE") and (iyy == yy):
        if nd <= num_data_line-1:
         dline = line.strip()
         print dline
         nd += 1
        else:
         sw=0
         nd=0

def make_out_list(dline_var,var_list, out_list):
    for var in var_list:
       if var == 'time':
         out_list.append(dline_var[0])
       elif var == 'grade':
         out_list.append(dline_var[2])
       elif var == 'lat':
         out_list.append(dline_var[3])
       elif var == 'lon':
         out_list.append(dline_var[4])
       elif var == 'p':
         out_list.append(dline_var[5])
       elif var == 'ws':
         out_list.append(dline_var[6])
    return(out_list)

def get_var_list():
#    print 'GET VAR LIST'
    tmp = icommand.split(':')[1]
    var_list = tmp.split(',')
    return(var_list)

command = 'none'
nargv = len(sys.argv)

# Get arg
if nargv == 4:
  icommand = sys.argv[1]
  itarget = sys.argv[2]
  sep = sys.argv[3]
elif nargv == 3:
  icommand = sys.argv[1]
  itarget = sys.argv[2]
  sep = " "
elif nargv == 2:
  icommand = sys.argv[1]
  itarget = 'ALL'
  sep = " "
elif nargv == 1:
  usage()

# Some setting
if itarget == 'ALL':
 ityid = 'ALL'
 iyy = 'ALL'
else:
 ityid = itarget
 iyy = ityid[0:2]
 if (len(ityid) == 2):
   ityid = "NONE"

#Debug
#print ityid
#print iyy
#print icommand

f = open('../ORG/bst_all.txt', 'rt')
bst_all_lines = f.readlines()
f.close()

# Command
if (icommand == "VAR"):
  variables()
elif (icommand == "GRADE"):
  grades()
elif (icommand == "HEADER"):
  header(bst_all_lines, ityid)
elif (icommand == "DATA"):
  data(bst_all_lines, ityid)
elif (icommand.split(':')[0] == "DATA"):
  var_list = get_var_list()
  data_vars(bst_all_lines, ityid, var_list, sep)
  
