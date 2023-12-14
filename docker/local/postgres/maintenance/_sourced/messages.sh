#!/usr/bin/env bash

message_newline(){
    echo
}

message_debug(){
    echo -e "DEBUG: ${@}"
}

message_welcome(){
    echo -e "\e[1m${@}\e[0m" #displaying the message in bold
}

message_warning(){
    echo -e "\e[33mWARNING\e[0m: ${@}" #33 is orange/brown.... 0;33 or 1;33 for a lighter colour- yellow
}

message_error(){
    echo -e "\e[31mERROR\e[0m: ${@}" #31 is red
}

message_info(){
    echo -e "\e[37mINFO\e[0m: ${@}" #37 is Light grey or white 1;33
}

message_suggestion(){
    echo -e "\e[33mSUGGESTION\e[0m: ${@}" 
}

message_success(){
    echo -e "\e[32mSUCCESS\e[0m: ${@}" #32 is green
}






