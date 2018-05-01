# 新浪微博数据分析网站

#### 原理

- 使用django+scrapy搭建,可对微博、评论及粉丝数据进行抓取
- 爬虫调度使用scrapyd提供的api
- 数据化展示使用echart.js
- 数据存储在redis数据库
- ajax轮询，画图结果实时展示在前端

#### 使用

所有数据的抓取都需要提供cookie(手机端或电脑端)，如下所示
![](https://raw.githubusercontent.com/Neilai/seusina/master/img/5.png)

- 单人微博数据分析结果（输入手机端cookie）和用户id(注意这个id不是用户名，而是微博主页url的最后一串字母或数字)

  ![](https://raw.githubusercontent.com/Neilai/seusina/master/img/1.png)

  ​

- 单条微博转发时间分析结果，极坐标角度代表分钟，半径代表小时

  ![](https://raw.githubusercontent.com/Neilai/seusina/master/img/2.png)

  ​

- 个人粉丝分布图（颜色越深的地方粉丝越多）

  ![](https://raw.githubusercontent.com/Neilai/seusina/master/img/3.png)

- 个人人际关系网，以自己为中心，按关注扩展三层

  ![](https://raw.githubusercontent.com/Neilai/seusina/master/img/4.png)

  ​

  ​