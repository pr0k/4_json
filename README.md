# Prettify JSON

The script converts a text file in JSON format and displays it on the command line in a pretty form

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
{
    "geometry": {
        "coordinates": [
            37.59317706430676,
            55.89772236936797
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "улица Лескова, дом 6",
            "AdmArea": "Северо-Восточный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Бибирево",
            "IsNetObject": "да",
            "Name": "Массандра в Алтуфьево",
            "OperatingCompany": "Массандра",
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 909-40-08"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "10:00-22:00"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "10:00-22:00"
                }
            ],
            "global_id": 14934782
        },
        "DatasetId": 1854,
        "ReleaseNumber": 2,
        "RowId": "1bd07c21-05de-4015-b015-d22657168ded",
        "VersionNumber": 1
    },
    "type": "Feature"
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
