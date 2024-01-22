#!/bin/bash

# 获取当前日期和时间
current_time=$(date "+%m.%d-%H.%M")

# 运行Python脚本并将输出重定向到一个文件中
python -u src/request_api.py > ./logs/output_${current_time}.txt 2>&1   | tee ./logs/output_${current_time}.txt
