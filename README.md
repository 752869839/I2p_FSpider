### author LiZhi Chen

项目简介: 此项目为针对i2p的暗网全网web数据分布式采集、分析、存储
项目架构: tor通道 + scrapy_redis + scrapyd + scrapydweb + redis + mysql +  elasticsearch + seaweedfs + docker
环境依赖: 服务器n台操作系统不限、 docker版本不限、 mysql 5.7.32、 redis 6.0.8、 elasticsearch 7.8.1、 seaweedfs文件服务器、 i2p通道n个

上传项目到目标服务器,系统防火墙需开放5000、6800、6801端口,并安装docker服务
cd /i2p_whole_spider/docker
修改 scrapyd.conf、scrapyd_monitor.sh  相关配置为你部署服务器地址
docker build -t wholescrapyd:latest .      镜像构建时间可能较长耐心等待
将 /i2p_whole_spider/docker/crontab.txt  内容输入crontab -e 设定定时任务
修改 /i2p_whole_spider/i2p_spider/settings.py  相关配置
修改 /i2p_whole_spider/schedule/config.py  相关配置

创建mapping
cd /i2p_whole_spider/schedule/mapping  查看mapping说明按说明执行即可,ip修改为es地址即可
访问你部署ip:5000端口  x.x.x.x:5000 scrapydweb接口,将项目压缩.zip包或.rar包 上传运行即可
多台机器重复上述步骤即分布式部署完成

分布式部署成功后,运行schedule中lpush_task.py  推送任务到redis,分布式任务即可获取到redis中待采集任务
在找一台cpu配置高的机器后台运行 data_export.py  64进程数据从redis实时写入es即可
