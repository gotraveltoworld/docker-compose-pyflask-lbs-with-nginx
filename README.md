# docker-compose-pyflask-lbs-with-nginx
Use docker-compose to build a simple flask cluster with Nginx.

## Run
```shell
# Run and build.
docker-compose up -build
# Run
docker-compose up
# Rmove the volumes and containers.
docker-compose down -v
```
After completet the building you can open the browser to access 'http://localhost:18088/'.
You can see the node's name nad the PID number(JSON format).

## Env
You can set some env parameters in the `.env` file.


## 重點紀錄
本專案只為了練習設定`.env`檔案和`docekr-compose`的連動方式，有部分地方仍然保留一些相關設定(註解)。
1. 模板方式帶入到uwsgi.ini需要另外用環境變數的方式生成。
2. 目前路徑變數的帶入仍然會有問題，需要另外處理。
3. Nginx的設定變數需要用一隻shell script生成，注意生成方式和語法，可以上網找資料參考。
4. 多利用`docker-compose config`觀看設定結果，可以比對一下實際帶入的資料。
