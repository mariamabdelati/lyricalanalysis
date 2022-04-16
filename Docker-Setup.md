## Docker Setup

This file details how to set up docker and create a hive server on linux/mac

Navigate to the root folder where the needed files are located (3_Hadoop in this case). 

Start up the terminal from within this folder or simply navigate to it from terminal using 
``` console
$ cd /path/to/folder/3_Hadoop
```

Next execute the following command:
``` console
$ docker-compose up
```

After it has finished execution, in a new terminal (also from within 3_Hadoop), execute the following commands to access the hive-server
``` console
$ docker exec -it hive-server /bin/bash
```

Navigate to the *all_tracks* directory on the hive-server container
``` console
ls
```
``` console
cd ..
```
``` console
ls
```
``` console
cd all_tracks/
```

To create the all_tracks table, execute the all_tracks_table.hql file using the following command:
``` console
hive -f all_tracks_table.hql
```

To add data from the all_tracks.csv file to the table that was just created, the following command is executed
``` console
hadoop fs -put all_tracks.csv hdfs://namenode:8020/user/hive/warehouse/testdb.db/all_tracks
```

To view the data on the server, the following commands are executed
``` console
hive
```

HQL queries:
``` console
show databases;
```
``` console
use testdb;
```
``` console
select * from all_tracks limit 10;
```