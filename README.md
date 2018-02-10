# OpenCellId scripts
Bunch of scripts to request [opencellid](http://opencellid.org/).

## area.py
This is a quick & dirty script to get radio cells in a square area with around
a coordinate.

The requests are limited to 5000 requests per day (free api key).

### Parameters
* -h, --help: prints help
* -k, --key: your opencellid api-key
  Format: id<int>, required: yes.
* -p, --position: coordinates of position in center of ara. 
  Format: lat<float>,lon<float>, required: yes.
* -a, --area: size of the areai in km². This is limited to 400,000 ft² by 
  opencellid.
  Format: area<float>, required: no, default: 0.1 km².

### Example

```bash
$ ./area.py -p 51.0824,13.7255 -a 0.1 -k SCRTKEY
25 Stations Found
  cellid  |   lat    ,    lon    |  lac  | mcc |mnc| radio
----------+----------------------+-------+-----+---+------
    64492 | 51.081174, 13.724188 | 35077 | 262 | 1 | GSM
134555761 | 51.081325, 13.727417 | 40053 | 262 | 3 | UMTS
     9761 | 51.082741, 13.726536 |   350 | 262 | 2 | GSM
 27086850 | 51.082926, 13.725547 | 18000 | 262 | 1 | LTE
    63123 | 51.083102, 13.726052 |   773 | 262 | 3 | GSM
   213574 | 51.083130, 13.726318 | 35221 | 262 | 1 | UMTS
 48156731 | 51.083296, 13.725373 | 21634 | 262 | 7 | UMTS
  1079656 | 51.083343, 13.727417 | 35221 | 262 | 1 | UMTS
 48146731 | 51.083413, 13.727417 | 21634 | 262 | 7 | UMTS
  1065542 | 51.083554, 13.727417 | 35221 | 262 | 1 | UMTS
       24 | 51.083679, 13.727417 | 35992 | 262 | 1 | GSM
       28 | 51.083679, 13.727417 | 35813 | 262 | 1 | GSM
    64492 | 51.083679, 13.727417 | 35077 | 262 | 3 | GSM
     3976 | 51.083679, 13.727417 | 35082 | 262 | 3 | GSM
       41 | 51.083679, 13.727417 |  3108 | 262 | 2 | GSM
 48764797 | 51.083679, 13.727417 | 21609 | 262 | 7 | UMTS
    43307 | 51.083679, 13.727417 | 21634 | 262 | 7 | GSM
    27312 | 51.083679, 13.727417 |   350 | 262 | 1 | GSM
  7831809 | 51.083679, 13.727417 | 50022 | 262 | 3 | LTE
 48116824 | 51.083679, 13.727417 | 21634 | 262 | 7 | UMTS
 48139428 | 51.083679, 13.727417 | 21634 | 262 | 7 | UMTS
 79305830 | 51.083679, 13.727417 |  1350 | 262 | 2 | UMTS
  7758593 | 51.083679, 13.727417 | 21634 | 262 | 7 | UMTS
134564141 | 51.083679, 13.727417 | 21634 | 262 | 7 | UMTS
   200085 | 51.083679, 13.727417 | 35221 | 262 | 1 | UMTS
```
