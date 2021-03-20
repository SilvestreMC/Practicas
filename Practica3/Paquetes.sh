#!/bin/bash
function menu
{
    echo "Scripts de paquetes"
    echo "1.- Buscar actualizaciones"
    echo "2.- Instalar actualizaciones"
    echo "3.- Borrar paquetes obsoletos"
    echo "4.- Salir"
    echo -n "Introduce una opcion"
    read opc
    while [ $opc -ne "1" -a $opc -ne "2" -a $opc -ne "3" -a $opc -ne "4" ]
    do
        clear
        echo "ERROR! Opcion no valida"
        echo "Scripts de paquetes"
        echo "1.- Buscar actualizaciones"
        echo "2.- Instalar actualizaciones"
        echo "3.- Borrar paquetes obsoletos"
        echo "4.- Salir"
        echo -n "Introduce una opcion"
        read opc
    done
}
function paquete
{
    if [ $opc -eq "1" ]; then
        sudo apt update
    elif [ $opc -eq "2" ]; then
        sudo apt upgrade
    elif [ $opc -eq "3" ]; then
        sudo apt autoremove
    fi
}
menu
paquete $opc
while [ $opc -ne 4 ]
do
    menu
    paquete $opc
done