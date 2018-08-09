#!/bin/bash
types='ppt tmin tmax tmean'
base_url='http://services.nacse.org/prism/data/public/4km/'
year=1990

while [ $year -le 2015 ]
do
    month=1
    while [ $month -le 12 ]
    do
        month_str=$month
        # Pad with 0 if necessary
        if [ $month -lt 10 ]
        then
            month_str="0$month"
        fi

        # Download all types
        for type in $types
        do
            download_url="$base_url$type/$year$month_str"
            curl -JLO $download_url
        done

        ((month++))
    done
    ((year++))
done