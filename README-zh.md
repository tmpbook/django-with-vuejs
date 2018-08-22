# django-with-vuejs

Fast & Clear in DevOps.

[English README.md](/README-zh.md)

> 为什么 [Django Project](/examples/django-auth-with-react/backend) 目录和 [Frontend](/examples/django-auth-with-react/frontend) 目录均是在同级的 [example/django-auth-with-react](/examples/django-auth-with-react) 中，但是在 [project](/project) 目录中不是这样?

这是因为 django-auth-with-react 项目是真正的前后端分离的，而 project 是 Django 去读取 index.html 的，并非真正的前后端分离。见 [#16](https://github.com/tmpbook/django-with-vuejs/issues/15)

项目是最简版

---

### Step 1: 装前端依赖

```
cd django-with-vuejs/my_project/vue2_frontend
npm install
```

### Step 2: 构建前端

在 vue2_frontend 目录构建前端页面

```
npm run build
```

### Step 3: 通过 Django 自带 server 启动项目

In the directory where manage.py is located

```
pip install -r requirements.txt
python manage runserver
```

---

## 更详细的教程

这里: https://zhuanlan.zhihu.com/p/24893786

## 与前端结合的原理

前端构建完成就下面这两个资源

- index.html
- static/\*

让我们看看如何处理这两个资源

### 第一个. index.html

使用 [django template engines](https://docs.djangoproject.com/en/dev/topics/templates/) 去处理 `index.html` 文件

在 `settings.py` 中

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': ['vue2_frontend/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

我们改变 `TEMPLATES.DIRS` 从而让 Django 能够找到 `index.html` 文件在哪。

### 第二个. static/\*

同样是在 `settings.py` 中

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "vue2_frontend/dist/static"),
]
```

我们添加 `STATICFILES_DIRS` 配置，这个配置可以让 Django 找以下资源的时候：

```html
<script type=text/javascript src=/static/js/vendor.677ef0c9485c32b4f6a9.js></script>
```

在 _vue2_frontend/dist/static_ 这个目录寻找，但是需要注意的是，这只在 django 的开发模式下才生效。

## 生产环境

我们在生产环境使用 Nginx 处理前端页面

- index.html
- static/\*

使用 Django 来开发 API，JSON 来传输数据。

有任何问题 [New issues](https://github.com/tmpbook/django-with-vuejs/issues/new)

### About me

知乎：[临书](https://www.zhihu.com/people/tmpbook/activities)

微信（WeChat）：

<div align=center>
    <img width="150" height="150" src="https://github.com/tmpbook/Django-with-ElasticSearch/blob/master/Wechat.jpeg"/>
</div>

<div align=right>谢谢阅读</div>
<div align=right>Thanks for watching</div>
