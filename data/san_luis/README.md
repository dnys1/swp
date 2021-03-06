# San Luis Reservoir/O'Neill Forebay/Los Banos Reservoir

![San Luis Watershed Boundary](images/san_luis_watershed_boundary.jpg)

## Data Sources

Because San Luis is an artificial lake which water is pumped to, there is no upstream data. Nor are there any gauges for the O'Neill Forebay. The markers shown below in the reservoir are not generating real-time data.

![San Luis USGS Map](images/san_luis_usgs_map.png)

The following NOAA gauge was selected for Temperature/Precipitation data.

![San Luis NOAA Map](images/san_luis_noaa_map.png)

## Data Files

| Filename                                                     | Type                             | Source/Site no.                                                                                        | Start Date | End Date   |
| ------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------- | ---------- |
| [noaa_USC00045119.csv](noaa_USC00045119.csv)                 | Temperature/Precipitation        | [NOAA USC00045119](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00045119/detail) | 1932-09-01 | 2018-05-31 |
| [cdec_SNL_elevation_daily.csv](cdec_SNL_elevation_daily.csv) | Reservoir Elevation (ft) - Daily | [CDEC SNL](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=SNL)                                 | 1988-01-04 | 2018-07-28 |
| [cdec_SNL_daily.csv](cdec_SNL_daily.csv)                     | Reservoir Storage (af) - Daily   | [CDEC SNL](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=SNL)                                 | 1988-01-04 | 2018-07-28 |
| [cdec_SNL_monthly.csv](cdec_SNL_monthly.csv)                 | Reservoir Storage (af) - Monthly | [CDEC SNL](http://cdec.water.ca.gov/dynamicapp/staMeta?station_id=SNL)                                 | 1968-10-01 | 2018-07-01 |