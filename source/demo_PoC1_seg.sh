#! /bin/bash
### stop NFD from the previous run 
nfd-stop
### stop DTN from the previous run 
ps -ef | grep dtnd | grep -v grep | awk '{print $2}' | xargs kill
### stop python script from the previous run 
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill
### stop all running docker containers 
docker rm -f $(docker ps -a -q)
### remove the docker image file (kebapp)
rm /home/pirate/PiGeon/source/modules/ServiceExecution/SEG_repository/kebapp.tar.gz
### restart dtn by ponting to configuration file 
dtnd -v -i wlan0 -c /home/pirate/umobile/ibr-dtn/demo-icn17-ibr.conf &
sleep 10s 
### restart NFD  
nfd-start
### create DTN face
nfdc create dtn://umobile-pi-1/nfd
### add NFD routing info to FIB by using DTN face
nfdc register /picasso/service_deployment_pull dtn://umobile-pi-1/nfd

## For testing ### 
#nfdc create tcp://192.168.0.150
#nfdc register /picasso/service_deployment_pull tcp://192.168.0.150