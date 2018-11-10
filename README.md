# InsightData
Problem, Approach and Run instructions sections

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

This code create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Data are in `input` directory, running the `run.sh` script should execute the main python code in src folder, and produce the results in the `output` folder with two files in txt format: top_10_occupations.txt and top_10_states.txt.



**Approach:** Each year of data can have different columns. Check **File Structure** docs before development. 


# Run instructions

This project use python3, execute h1b_DataTesting.py or run.sh should work
Code have been tested over 3 test-suites:
1. h1b_input.csv
2. Truncated 2014 (first 3000 entries)
2. Truncated 2015 (first 500 entries)


## What we are looking at
Your solution should safisfy the following requirements:
* Repo follows the required repo directory structure
* The code is well-commented
## Repo directory structure

The directory structure for your repo should look like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_DataTesting.py
      ├── input
      │   └──H1B_FY_2015_.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── H1B_FY_2014_.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── test2
              |    ├── input
              |    │   └── H1B_FY_2014_test2.csv
              |    |── output
              |    |   |   └── top_10_occupations.txt
              |    |   |   └── top_10_states.txt
              ├── test3
              |    ├── input
              |    │   └── H1B_FY_2016.csv (FILE SIZE RESTRICTION, CANT UPLOAD)
              |    |      (https://drive.google.com/open?id=1Pw7x3N8QWX6ZILPI2qw2NhQghAJ-2Eed)
              |    |── output
              |    |   |   └── top_10_occupations.txt
              |    |   |   └── top_10_states.txt

```
