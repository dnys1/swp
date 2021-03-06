# Thermalito Afterbay

- [Thermalito Afterbay](#thermalito-afterbay)
    - [Data Sources](#data-sources)
    - [Data Files](#data-files)

The Thermalito Afterbay directly follows Lake Oroville in the State Water Project.

**Operating Agency**: CA Dept of Water Resources

![Thermalito Watershed Boundary](images/thermalito_watershed_boundary.jpg)

## Data Sources

![Thermalio Afterbay Map](images/thermalito_usgs_map.png)

Discharge data was collected for the following sites:

| #   | Site Info                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------- |
| 1   | **Site Number:** [11406810](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11406810) |
| 2   | **Site Number:** [11407000](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11407000) |

Storage data was most prevalently available. To convert into elevation data, Area-Storage-Elevation curves were acquired [here](http://wdl.water.ca.gov/orovillerelicensing/docs/app_ferc_license_2005/Vol_I_Exhibit%20B.pdf).

## Data Files

| Filename                                                     | Type                             | Source/Site no.                                                                              | Start Date | End Date   |
| ------------------------------------------------------------ | -------------------------------- | -------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [usgs_11406810.csv](usgs_11406810.csv)                       | Discharge                        | [USGS 11406810](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11406810) | 1968-10-01 | 2017-09-30 |
| [usgs_11407000.csv](usgs_11407000.csv)                       | Discharge                        | [USGS 11407000](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=11407000) | 1901-10-01 | 2017-09-30 |
| [cdec_TAB_monthly.csv](cdec_TAB_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC TAB](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=TAB)                       | 1967-10-01 | 2018-07-01 |
| [cdec_TAB_daily.csv](cdec_TAB_daily.csv)                     | Reservoir Storage (af) - Daily   | [CDEC TAB](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=TAB)                       | 1985-01-01 | 2018-07-28 |
| [cdec_TAB_elevation_daily.csv](cdec_TAB_elevation_daily.csv) | Reservoir Level (ft) - Daily     | [CDEC TAB](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=TAB)                       | 2008-01-01 | 2018-07-28 |
| [cdec_TFR_monthly.csv](cdec_TFR_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC TFR](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=TFR)                       | 1969-10-01 | 2018-07-01 |