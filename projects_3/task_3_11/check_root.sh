#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Предупреждение: Скрипт запущен не от root"
        exit 1
    fi
}

check_root
echo "Скрипт выполняется от root"
