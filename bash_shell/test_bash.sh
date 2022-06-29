#!/usr/bin/bash
# -*- coding: utf-8 -*-

# 실행된 스크립트 이름
# $1~  => 인자의 순서대로 번호 부여. 10부터는 {}를 감싸줘야한다.
echo $0
echo ${0}

echo $1
echo $2

# 전체 인자의 값  => "$1 $2"
echo $* 

# 전체 인자값($*과 동일하지만 ""로 묶으면 다른 결과 나옴) => "$1" "$2"
echo $@

# 매개 변수의 총 개수
echo $#

# 현재 스크립트의 pid
echo $$

# 최근에 실행된 명령어, 함수, 스크립트 자식의 종료 상태
echo $?

# var for test
string="abc-efg-123-abc"

# $변수 ${변수}
echo $string
echo ${string}
