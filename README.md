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
#### 1. You should pull and build images in file docker-compose.yaml before

#### 2. Move to clone project and Start system
  
```sh
docker compose up -d
```

#### 3. Install java on airflow-webserve

```sh
docker exec -it -u root airflow-webserver /bin/bash
apt update && apt install default-jdk
```

#### 4. After start system, all port website of containers in <a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/port.txt">here</a>
#### 5. Start DAG in Airflow cluster
#### 6. Move to folder superset and run

```sh
bash bootstrap-superset.sh
```
  
#### 7. Visualize data in Superset website on local


## Demo


## Old version
<ul>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/report.pdf">Report</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/slide.pptx">Slide</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/system-flow.png">Data flow</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/VirtualMachine.png">System architecture</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Analyze_Game_data/blob/master/old_version/report/screen-shots/">Output</a></li>
</ul>
