# someones_fucking_graduate_project
someone's fucking graduate project

总得来说， 要分成如下几个主文件和文件夹

build_data.sh
作用:构建数据 ， 生成在data文件夹下

sh build_data.sh src_dir

==================================

build_offline_user.sh
作用：生成离线用户的信息， 生成在user_info文件夹下

sh build_offline_user.sh data/

==================================

sh predict_user.sh
作用：测试用户信息

sh predict_user.sh data/ user_info/

==================================

sh server.sh
作用：启动server， 开始演示程序

==================================

dir:rec_lib

推荐的文件夹， 用来保存一些用户推荐的代码

==================================

dir:data_lib

数据基本定义的lib， 读入输出数据怎么搞的

==================================

dir:run_lib

基本跑程序的脚本

==================================

dir:util
基本功能函数







