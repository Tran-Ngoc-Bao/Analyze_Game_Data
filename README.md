# IT4931 - Big data Storage and Processing - SOICT - HUST

## Introduction
<ul>
  <li>Name of project: Storing and processing video game data from App store and Google play</li>
  <li>Project objective:
    <ul>
      <li>Collecting game data on Google play and App store weekly</li>
      <li>Store, analyze, and process the collected data</li>
      <li>Present the obtained results in the form of charts</li>
    </ul>
  </li>
</ul>

## Data flow
  <img src="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/pictures/design/DataFlow.png">

## Deploy system
#### 1. Start system
```sh
docker compose up -d
```

#### 2. Start DAG on Airflow cluster
  
#### 3. Visualize data on Superset with SQLalchemy uri
```
postgresql://datawarehouse:datawarehouse@data-warehouse:5432/datawarehouse
```

## Demo
### Data flow in Airflow
<img style="width:80%" src="https://github.com/Tran-Ngoc-Bao/Analyze_Game_Data/blob/master/pictures/screenshot/airflow.jpeg">

### Data lake in HDFS
<img style="width:80%" src="https://github.com/Tran-Ngoc-Bao/Analyze_Game_Data/blob/master/pictures/screenshot/hdfs.jpeg">

### Top review company Google play
<img style="width:75%" src="https://github.com/Tran-Ngoc-Bao/Analyze_Game_Data/blob/master/pictures/output/reviews-company-google-play-tablet-09092024-2024-09-10T15-44-59.913Z.jpg">

### Top game genre App store
<img style="width:75%" src="https://github.com/Tran-Ngoc-Bao/Analyze_Game_Data/blob/master/pictures/output/classify-app-store-09092024-2024-09-10T15-37-01.306Z.jpg">

## Old version
<ul>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/report.pdf">Report</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/slide.pptx">Slide</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/system-flow.png">Data flow</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/VirtualMachine.png">System architecture</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/screen-shots/">Output</a></li>
</ul>
