Get-ExecutionPolicy -Scope CurrentUser

if its restricted then use 

Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser


you will be able to create virual environemnts now