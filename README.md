#### scws的编译

[ref] http://www.xunsearch.com/scws/docs.php 《SCWS-1.2.3 安装说明》：

1. 取得 scws-1.2.3 的代码
wget http://www.xunsearch.com/scws/down/scws-1.2.3.tar.bz2

2. 解开压缩包
[hightman@d1 ~]$ tar xvjf scws-1.2.3.tar.bz2

3. 进入目录执行配置脚本和编译
[hightman@d1 ~]$ cd scws-1.2.3[hightman@d1 ~/scws-1.2.3]$ ./configure --prefix=/usr/local/scws ; make ; make install

* 注：这里和通用的 GNU 软件安装方式一样，具体选项参数执行 ./configure --help 查看。常用选项为：--prefix=<scws的安装目录>
4. 顺利的话已经编译并安装成功到 /usr/local/scws 中了，执行下面命令看看文件是否存在
[hightman@d1 ~/scws-1.2.3]$ ls -al /usr/local/scws/lib/libscws.la

5. 试试执行 scws-cli 文件
[hightman@d1 ~/scws-1.2.3]$ /usr/local/scws/bin/scws -h
scws (scws-cli/1.2.3)
Simple Chinese Word Segmentation - Command line usage.
Copyright (C)2007 by hightman.
...

6. cp -r libscws.so libscws.so.1 libscws.so.1.1.0 /usr/lib/

7. sudo ldconfig

#### run
choice .so file and ref to "python_scws_util.py" usage
