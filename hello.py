from os import path 

print('hello')
print ("model exist:"+str(path.exists('/app/RiboVsPoly.sav')))
print ("model exist:"+str(path.exists('RiboVsPoly.sav')))
print ("hello exists:" + str(path.exists('hello.py')))
print ("RF exists:" + str(path.exists('RF_deploy.py')))
print ("RF exists:" + str(path.exists('/app/RF_deploy.py')))
