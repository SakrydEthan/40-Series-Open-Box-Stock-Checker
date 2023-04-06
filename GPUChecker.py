from selenium import webdriver
from selenium.webdriver.common.by import By
import time

filename = time.asctime() + ".txt"
filename = filename.replace(" ", "-")
filename = filename.replace(":", "-")
log = open(filename, "x")
log.write("")

def parsesite(storename, storeURL):
	browser.get(storeURL)
	gpus = browser.find_elements(By.CLASS_NAME, "product_wrapper")
	stock = 0
	
	for e in gpus:
		has40series = False
		gpuname = ""
		if e.text.find("4070") != -1:
			has40series = True
			gpuname = "4070"
		if e.text.find("4080") != -1:
			has40series = True
			gpuname = "4080"
		if e.text.find("4090") != -1:
			has40series = True
			gpuname = "4090"
		if has40series == False:
			continue

		startind = e.text.find("Open Box From")
		stopind = e.text.find("SELECT OPEN BOX")
		print(storename+": "+gpuname+" "+e.text[startind:stopind])
		log.write(storename+": "+gpuname+" "+e.text[startind:stopind])
		stock += 1
	return stock

parkvilleURL = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&prt=clearance&N=4294966937&storeID=125'
rockvilleURL = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&prt=clearance&N=4294966937&storeID=085'
fairfaxURL = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&prt=clearance&N=4294966937&storeID=081'

pvstock = 0
rvstock = 0
ffstock = 0

browser = webdriver.Chrome()

pvstock = parsesite("Parkville",parkvilleURL)

time.sleep(3)

rvstock = parsesite("Rockville",rockvilleURL)

time.sleep(3)

ffstock = parsesite("Fairfax",fairfaxURL)


print("Parkville 40 Series stock: "+str(pvstock))
print("Rockville 40 Series stock: "+str(rvstock))
print("Fairfax 40 Series stock: "+str(ffstock))

log.write("\n Parkville 40 Series stock: "+str(pvstock))
log.write("\n Rockville 40 Series stock: "+str(rvstock))
log.write("\n Fairfax 40 Series stock: "+str(ffstock))
