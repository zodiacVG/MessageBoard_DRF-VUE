# 环境配置特殊点
# 1.后端/backend/api中有两个app，需分别makemigrations
#### 2.引入了elementUI组件库
#### 3.引入了djoser库


# 实现功能

#### 1. 注册，登录与注销 
使用django自带用户系统，使用djoser库
登录和注册均只需用户名和密码
#### 2. 留言发布 
未登录时以游客身份发布，登陆后以该用户发布
提交后即时刷新留言组件，无需手动刷新
#### 3. 点赞与点踩
赞和踩分开计算，每人限制点赞/点踩各一次
数据库实时更新

# 配置docker环境

打开你的命令行界面，找到一个目录位置，拉取仓库

```bash
git clone https://se.jisuanke.com/course/python38.git
```

拉取完成后进入目录

```bash
cd python38
```

进行构建（注意最后一个表示当前位置的 `.` 不能丢了）

```bash
docker build -t "python:38" .
```

## 进入环境

首次进入：

```bash
docker run -it -p 8000:8000 --name python38 python:38
```

之后进入

```bash
docker start python38
docker exec -it python38 /bin/bash
```

# backend
## 1. 搭建环境
进入docker虚拟环境
### 引入如下库（见/backend/pipfile） 
#### pipenv install 以下：
```
	django
	djangorestframework
	mysqlclient
	django-cors-headers
	djoser
```
## 2. 数据库配置
#### 1.修改settings.py中的数据库为你的数据库信息
#### 2.在/backend/api文件夹下运行：
```
./manage.py makemigrations messageboard
./manage.py migrate
./manage.py makemigrations authapp
./manage.py migrate
```
## 3.启动后台程序
	./manage.py runserver 0:8001

# frontend

## Project setup
```
npm install
```
### Import ElementUI
```
npm i element-ui -S
```
### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).






