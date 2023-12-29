#!/usr/bin/env bash

yes_no(){
    declare desc="Prompt for confirmation. \$\"\{1\}\": confirmation message" #description desc is for documentation purposes only

    local arg1="${1}"

    local response= read -r -p "${arg1} (y/[n])? " response

    if [[ "${response}" =~ ^[Yy]$ ]] #checking if the response is yes i.e Y or y
    
    then
        exit 0 #success
    else
        exit 1 #failure
    fi # to end our if block
}
