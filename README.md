careHealth
===========

Health service application

Objective:
=========
1. User registration
2. SNS
3. forum
4. Hospital and disease data crawling
5. Storage
6. Data analyse
7. UI


TODO:
====

1. Build a website
2. Optimize backend algorithm
3. Data crawling
4. UI beautifing

Dependency:
==========
python 2.7
django 1.7

Strcuture:
=========
1. careHealth是一个django程序
2. web文件夹内保存的是web网页的访问接口，在url中以web开头，这里一般直接render_to_response一个template即可
3. api文件夹内保存的是api事件处理接口，在url中以api开头，这里一般处理具体事宜，处理完毕后返回json数据
4. earth文件夹内保存的是封装好的rest架构的基础类，在api中添加新的resource时，只需要按照格式相应继承，调用即可。
5. 在web或者api文件夹内增加新的app时，需要更新相应位置的urls.py，同时，在api文件夹内增加新的app时，需要在settings.py文件中指定对应的API_ID
6. 新增一个web的app时，需要指定其views.py, urls.py, templates，具体格式参见index这个实例
7. 新增一个api的app时，需要制定其action, api, models.py，具体格式参见example这个实例
8. 将具体的事物处理与网页渲染分离开来，便于扩展，哪怕是新增手机客户端，也有接口直接调用
9. 网页渲染返回后，网页并没有实际数据，因此，目测大部分需要用ajax异步请求数据，当然也可以考虑在渲染网页时直接带数据过去。
10.push test
