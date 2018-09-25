# crawlDoctor

#### 项目介绍
爬虫获取医院医生信息

#### 软件架构
软件架构说明


#### 安装教程

1. xxxx
2. xxxx
3. xxxx

#### 使用说明

1. 安装python、scrapy、PyMySQL
2. mysql建表：
DROP TABLE IF EXISTS `t_doctor`;
CREATE TABLE `t_doctor` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `hospitalname` varchar(100) DEFAULT NULL COMMENT '医院名称',
  `bigdept` varchar(100) DEFAULT NULL COMMENT '大科室',
  `smalldept` varchar(100) DEFAULT NULL COMMENT '小科室',
  `name` varchar(100) DEFAULT NULL COMMENT '姓名',
  `title` varchar(100) DEFAULT NULL COMMENT '职称',
  `introduction` varchar(5000) DEFAULT NULL COMMENT '简介',
  `deptlink` varchar(1000) DEFAULT NULL COMMENT '科室链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
3. cd crawlDoctor/
4. python3 begin.py

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request
