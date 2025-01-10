#!/bin/bash

# 安装依赖
pip install -r requirements.txt

# 创建上传目录
mkdir -p uploads

# 启动应用
python -m flask run 