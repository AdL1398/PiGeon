#! /bin/bash
### stop NFD from the previous run 
nfd-stop
### stop DTN from the previous run 
ps -ef | grep dtnd | grep -v grep | awk '{print $2}' | xargs kill
### stop python script from the previous run 
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill
### restart dtn by ponting to configuration file 
dtnd -v -i wlan0 -c /home/pirate/umobile/ibr-dtn/demo-icn17-ibr.conf &
sleep 10s 
### restart NFD  
nfd-start
### create DTN face 
nfdc create dtn://umobile-pi-2/nfd
nfdc register  /picasso/service_deployment_push/SEG_1 dtn://umobile-pi-2/nfd

## For testing 
#nfdc create tcp://192.168.0.248
#nfdc register  /picasso/service_deployment_push/SEG_1 tcp://192.168.0.248
