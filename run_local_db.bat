setlocal

set MONGOD="C:\Program Files\MongoDB\Server\3.4\bin\mongod"

md db

%MONGOD% --dbpath db
