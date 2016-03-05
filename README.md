项目描述：
====
外卖系统 （支持第三方商家引入）


项目目的：
====
以复杂的业务逻辑， 训练自己对于:
<ol>
<li><h5>Python<h5></li>
<li><h5>ReactJs<h5></li>
<li><h5>Restful<h5></li>
<li><h5>DJango<h5></li>
<li><h5>MongoDB<h5></li>
<li><h5>Redis<h5></li>
<li><h5>Celery<h5></li>
<li><h5>MySQL<h5></li>
<li><h5>Coroutine<h5></li>
</ol>
等一系列知识的深入掌握


基本规范：
====
1、python编码格式采用PEP8  
2、海量价值不高、 不涉及事务的数据采用mongodb进行存储  
3、缓存使用redis  
4、所有后台需要并发处理的事件， 采用celer+redis 的消息队列方式进行处理  
5、基本的用户信息采用mysql进行存储  
6、前端统一使用grant进行打包  
7、DJango采用Fat Models, Utility Modules, Thin Views, Stupid Templates 原则  
8、服务器采用centos + nginx + uwsgi 配置 , uwsgi管理系统使用The Master FIFO（详细配置见文档） 
9、项目托管在github  
10、Django、 python 等相关PyPi使用virtualwrapper进行管理  

项目设计（详细查看doc/*.doc)
====
