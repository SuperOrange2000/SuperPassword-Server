# SuperPassword-Server

这里是SuperPassword的服务端实现。

<!-- more -->

## 安装

```sh
git clone https://github.com/SuperOrange2000/SuperPassword-Server.git
pip install -r requirements.txt
```


## 配置

首先，使用**django**创建项目。本篇以**config**为配置目录的名称。

```sh
django-admin startproject config
```

此时**config**文件夹下应该有**settings.py**文件，这是配置的主要文件；还有**urls.py**文件，这里声明URL。

在**config/settings.py**文件中，你应该主要配置以下几个选项：
- INSTALLED_APPS

  必须将目录下的应用加载到django服务中。添加'**api.apps.ApiConfig**'和'**login.apps.LoginConfig**'到列表尾部即可。

- DATABASES

  这里配置了所使用的数据库，包括地址、用户名、密码等。推荐使用**MYSQL**。更多数据库配置请查看[DATABASES配置](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#databases)。

- ALLOWED_HOSTS

  如果你的服务使用域名或IP访问，你应该在这里指定使用的域名或IP。例如'**password.examplle.com**'或'**192.168.0.1**'。

- CSRF_TRUSTED_ORIGINS

  如果启用了CSRF验证，应该配置此项。配置方法同**ALLOWED_HOSTS**。

  

更多配置参见[django配置](https://docs.djangoproject.com/zh-hans/5.0/ref/settings/#settings)。

设置路由：

将项目目录下的**urls.py**覆盖**config/urls.py**即可。

## 激活模型

现在可以将需要的模型应用到数据库，生成相应的表了。

```sh
python manage.py makemigrations
python manage.py migrate
```

## 运行

现在可以启动服务了。

```sh
python manage.py runserver 127.0.0.1:8000
```

这条命令会监听**127.0.0.1**的8000端口，你可以改为自己的域名或IP。或者改为**0.0.0.0**，这样就会监听来自所有IP的请求了。