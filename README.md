# ECG Monitor

### Disclaimer
This app provides only information for educational purposes. This App is not medical or treatment advice, professional diagnosis, opinion, or services – and may not be treated as such by the user. As such, this App may not be relied upon for the purposes of medical diagnosis or as a recommendation for medical care or treatment. The information provided by this App is not a substitute for professional medical advice, diagnosis or treatment.

### General
Simple script for displaying electrocardiography data collected before into csv formatted file. 

### Usage
Datasource should be csv file with 2 columns - first column with time, second one with ecg sampled values

```
positional arguments:
  fname                 File path

options:
  -h, --help              show this help message and exit
  -fs FS                  Sampling frequency; default 1000Hz
  --delimiter DELIMITER   Columns delimiter; default ','
  -tstart TSTART          Signal recording start time in seconds; default 0
  -tstop TSTOP            Signal recording stop time in seconds; default signal duration time
  --lowcut LOWCUT         Butterworth filter lowcut frequency [Hz]; default 0.5Hz
  --highcut HIGHCUT       Butterworth filter highcut frequency [Hz]; default 150Hz
  -dt DT                  Displaying window width as time in seconds; default 5s
```

### Demo
```python ecg_monitor.py 'ecg.csv' -tstart 100```
![](./demo-gif/lowcut-filtration.gif)

Too low filter lowcut value - low frequencies components (breathing chest movements) causes signal floating.
```python ecg_monitor.py 'ecg.csv' -tstart 100 --lowcut 0.1```
![](./demo-gif/no-lowcut-filtration.gif)
