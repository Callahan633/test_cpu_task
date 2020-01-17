#!/bin/bash

while true; do

CPU_USAGE=$(top -b -n2 -p 1 | fgrep "Cpu(s)" | tail -1 | awk -F'id,' -v prefix="$prefix" '{ split($1, vs, ","); v=vs[length(vs)]; sub("%", "", v); printf "%s%.1f\n", prefix, 100 - v }')

DATE=$(date "+%Y-%m-%d %H:%M:%S")

txt='{"record_datetime":"'$DATE'", "record_cpu_data":"'$CPU_USAGE'"}'
if [ -z $0 ] && [ -z $1 ]
then
curl -X POST -H "Content-Type:application/json" -d "$txt" "http://$0:$1/save_record/"
else
curl -X POST -H "Content-Type:application/json" -d "$txt" "http://127.0.0.1:8001/save_record/"
fi
sleep 10
done
