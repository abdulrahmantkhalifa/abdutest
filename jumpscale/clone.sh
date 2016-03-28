 #!/bin/bash/

cd /tmp
git clone --depth=1  $1 

REPONAME=` echo  $1 | cut -d"/" -f5 | cut -d "." -f1 `
cd /tmp/$REPONAME
if [ -z `ls|grep -Fxqio "readme"` ];
then 
    cd ..
    rm -rf $REPONAME
    echo "readme found in $REPONAME"
fi
    
