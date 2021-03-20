function Ver-PerfilStatus
{  
    param([string]$perfil)
    while($perfil -ne "Public" -and $perfil -ne "Private")
    {
        Write-Host "ERROR! dato no valido"
        Write-Host "Para continuar, debe escribir ya sea el perfil Public o Private"
        $perfil=Read-Host -Prompt "Introduzca cual perfil desea ver su status"
    }
    Write-Host "Perfil:" $perfil  
    $status = Get-NetFirewallProfile -Name $perfil   
    if($status.enabled){  
        Write-Host "Status: Activado"  
    } else{  
        Write-Host "Status: Desactivado"  
    }  
}


Write-Host "Script para ver el status del perfil Publico o Privado"
$perfil = Read-Host -Prompt "Introduzca cual perfil desea ver su status"
Ver-PerfilStatus($perfil)