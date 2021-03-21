#Script para comprobar que los archivos tengan SHA256


Get-FileHash fcfm.png -Algorithm SHA256
Write-Host "fcfm.png"

Get-FileHash mystery_img1.txt -Algorithm SHA256
Write-Host "mystery_img1.txt"

Get-FileHash mystery_img2.txt -Algorithm SHA256
Write-Host "mystery_img2.txt"

Get-FileHash msg.txt -Algorithm SHA256
Write-Host "msg.txt"