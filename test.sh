#!/usr/bin/bash

# 현재경로
CURRENT_PATH=$(pwd)

# config file 경로
CONFIG_FILE=${CURRENT_PATH}/test2.conf

A=$(awk '/^test/{print $3}' ${CONFIG_FILE})
echo ${A}
