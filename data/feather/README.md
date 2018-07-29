# Feather Watershed

- [Feather Watershed](#feather-watershed)
    - [Overview](#overview)
    - [Operating Agency](#operating-agency)
    - [Data Sources](#data-sources)
    - [Data Files](#data-files)
    - [Google Earth](#google-earth)

## Overview

The feather watershed is the watershed at the start of the State Water Project. It consists primarily of three lakes which feed into Lake Oroville.

![Feather Watershed Map](images/feather_watershed_boundary.jpg)

## Operating Agency

| Site           | Operating Agency               |
| -------------- | ------------------------------ |
| Antelope Lake  | CA Dept of Water Resources/O&M |
| Frenchman Lake | CA Dept of Water Resources/O&M |
| Lake Davis     | CA Dept of Water Resources/O&M |
| Oroville Dam   | CA Dept of Water Resources/O&M |

## Data Sources

Streamgage data is from USGS sites 11404500, 11396200, and 11405200.

| #   | Site Info                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------- |
| 1   | **Site Number:** [11404500](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11404500) |
| 6   | **Site Number:** [11396200](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11396200) |
| 9   | **Site Number:** [11405200](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11405200) |

![USGS Site Map](images/feather_usgs_map.png)

Temperature/Precipitation data is from NOAA site USC00047195 in the middle of the watershed near Quincy, CA.

![NOAA Site Map](images/feather_noaa_map.png)

## Data Files

| Filename                                                     | Type                             | Source/Site no.                                                                                        | Start Date | End Date   |
| ------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------- | ---------- |
| [noaa_USC00047195.csv](noaa_USC00047195.csv)                 | Temp/Precip.                     | [NOAA USC00047195](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00047195/detail) | 1895-04-01 | 2018-07-23 |
| [usgs_11404500.csv](usgs_11404500.csv)                       | Discharge                        | [USGS 11404500](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11404500)           | 1911-04-01 | 2017-09-30 |
| [usgs_11396200.csv](usgs_11396200.csv)                       | Discharge                        | [USGS 11396200](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11396200)           | 1962-09-30 | 2017-09-30 |
| [usgs_11405200.csv](usgs_11405200.csv)                       | Discharge                        | [USGS 11405200](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11405200)           | 1986-08-27 | 2017-09-30 |
| [cdec_ANT_monthly.csv](cdec_ANT_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC ANT](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ANT)                                 | 1966-09-01 | 2018-07-01 |
| [cdec_ANT_daily.csv](cdec_ANT_daily.csv)                     | Reservoir Storage (af) - Daily   | [CDEC ANT](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ANT)                                 | 1985-01-01 | 2018-07-28 |
| [cdec_ANT_precip_daily.csv](cdec_ANT_precip_daily.csv)       | Precipitation (Incremental)      | [CDEC ANT](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ANT)                                 | 1987-01-01 | 2018-07-28 |
| [cdec_ANT_elevation_daily.csv](cdec_ANT_elevation_daily.csv) | Reservoir Elevation (ft) - Daily | [CDEC ANT](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ANT)                                 | 1985-01-01 | 2018-07-28 |
| [cdec_DAV_monthly.csv](cdec_DAV_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC DAV](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=DAV)                                 | 1967-10-01 | 2018-07-01 |
| [cdec_DAV_daily.csv](cdec_DAV_daily.csv)                     | Reservoir Storage (af) - Daily   | [CDEC DAV](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=DAV)                                 | 1988-08-06 | 2018-07-28 |
| [cdec_DAV_precip_daily.csv](cdec_DAV_precip_daily.csv)       | Precipitation - Daily            | [CDEC DAV](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=DAV)                                 | 1987-01-01 | 2018-07-28 |
| [cdec_DAV_elevation_daily.csv](cdec_DAV_elevation_daily.csv) | Reservoir Elevation (ft) - Daily | [CDEC DAV](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=DAV)                                 | 1986-08-06 | 2018-07-28 |
| [cdec_FRD_monthly.csv](cdec_FRD_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC FRD](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=FRD)                                 | 1962-10-01 | 2018-07-01 |
| [cdec_FRD_daily.csv](cdec_FRD_daily.csv)                     | Reservoir Storage (af) - Daily   | [CDEC FRD](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=FRD)                                 | 1985-01-01 | 2018-07-28 |
| [cdec_FRD_elevation_daily.csv](cdec_FRD_elevation_daily.csv) | Reservoir Elevation (ft) - Daily | [CDEC FRD](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=FRD)                                 | 1985-01-01 | 2018-07-28 |
| [cdec_FRD_precip_daily.csv](cdec_FRD_precip_daily.csv)       | Precipitation - Daily            | [CDEC FRD](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=FRD)                                 | 1987-01-01 | 2018-07-28 |
| [cdec_ORO_monthly.csv](cdec_ORO_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC ORO](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ORO)                                 | 1967-10-01 | 2018-07-01 |
| [cdec_ORO_daily.csv](cdec_ORO_daily.csv)                     | Reservoir Storage (af) - Daily   | [CDEC ORO](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ORO)                                 | 1985-02-13 | 2018-07-28 |
| [cdec_ORO_elevation_daily.csv](cdec_ORO_elevation_daily.csv) | Reservoir Elevation (ft) - Daily | [CDEC ORO](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ORO)                                 | 1985-02-14 | 2018-07-28 |
| [cdec_ORO_precip_daily.csv](cdec_ORO_precip_daily.csv)       | Precipitation (Incremental)      | [CDEC ORO](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=ORO)                                 | 1987-01-01 | 2018-07-28 |

## Google Earth

- [FEA_watersheds.kml](http://hydra.ucdavis.edu/node/35) - Watershed boundary map
