#!/bin/bash

read -p "Введите массу (кг): " weight
read -p "Введите рост (м): " height
bmi=$(echo "$weight / ($height * $height)" | bc)
echo "Ваш ИМТ: $bmi"
