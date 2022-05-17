# Cloud.gov Audit Events

This repository contains a [run script](scripts/run) that can be used to export cloud.gov audit events and create an Audit Report of the events in an MS Excel document.

## Background

The Cloud Foundry instance we're using, cloud.gov, is only setup to retain [Cloud Foundry Audit Events](https://docs.cloudfoundry.org/running/managing-cf/audit-events.html) for 31 days. Based on this, we needed a way to export and audit events elsewhere before they expired. The [get events script](scripts/get_events.py) is used to export cloud.gov audit events ([see Cloud Foundry Audit Events](https://docs.cloudfoundry.org/running/managing-cf/audit-events.html)). The [audit event reporter script](scripts/audit_event_reporter.py) is used to create an MS Excel document based on data from the [get events script](scripts/get_events.py).

The [get events script](scripts/get_events.py) is smart enough to know when it last ran to make sure all events are captured and not duplicated. Other users can easily adjust these scripts to suit their needs. For example, a past iteration of this project used GitHub Actions to run the [get events script](scripts/get_events.py) every 24 hours.

## Setup
 1. Clone repository to your local machine
 2. pip install requirements.txt (i.e., pip install -r requirements.txt)
 3. Update the [get events script](scripts/get_events.py) cf.exe version to your local cf version (e.g., cf7.exe), as needed
 4. Update the [run script](scripts/run):
      - CF_ORG="INSERT-ORG-NAME"
      - CF_SPACE="INSERT-SPACE-NAME"
      - YYYYMM="YEAR-MM"

## Get Events and Audit Report (i.e., MS Excel document)

 Navigate to the scripts folder and execute the [run script](scripts/run). If setup correctly, a:
 - YYYY-MM.json will be created in the data > organization-name folder and
 - MS Excel document will be created in the location of the audit event reporter script's output filename path (e.g., final-AuditReport-2022-05.xlsx)

```
bash run
```

## Get Events from the Past 31 days 

To get events from the past 31 days, create a status_data.json file to the date *before* you would like the data pulled.

1. In the scripts folder, create a data folder.
2. In the data folder, create a folder named after your cloud.gov organization (e.g., org-name)
3. In the org-name folder, copy the [status_data.json](./scripts/example-data/org-name/status_data.json) file and modify the status_data.json file to meet your event needs.

If you would like to obtain event data starting 05-04-2022, then you would set the status_data.json date to 2022-05-03 (see below). 

```
{
    "last_date_of_events_extracted": "2022-05-03",
    "last_date_time_events_extracted": "2022-05-03T00:00:00.000000Z"
}
```

### Disclaimer

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use.  EPA has relinquished control of the information and no longer has responsibility to protect the integrity , confidentiality, or availability of the information.  Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA.  The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
