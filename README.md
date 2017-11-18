# Blog_Django
- 开发环境的系统平台为 Windows 10 （64 位），Python 版本为 3.5.2 （64 位），Django 版本为 1.11.5。

│  manage.py
├─blog
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│          
├─blog_app
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_auto_20171117_2004.py
│  │  │  __init__.py
│  │          
│  ├─templatetags
│  │  blog_tags.py
│  │  __init__.py

│          
├─comments
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  __init__.py
│          
├─static
│  ├─css
│  │  │  bootstrap.min.css
│  │  │  custom.css
│  │  │  pace.css
│  │  │  
│  │  └─highlights
│  │          autumn.css
│  │          borland.css
│  │          bw.css
│  │          colorful.css
│  │          default.css
│  │          emacs.css
│  │          friendly.css
│  │          fruity.css
│  │          github.css
│  │          manni.css
│  │          monokai.css
│  │          murphy.css
│  │          native.css
│  │          pastie.css
│  │          perldoc.css
│  │          tango.css
│  │          trac.css
│  │          vim.css
│  │          vs.css
│  │          zenburn.css
│  │          
│  ├─img
│  │      me.jpg
│  │      
│  └─js
│          bootstrap.min.js
│          jquery-2.1.3.min.js
│          modernizr.custom.js
│          pace.min.js
│          script.js
│          
└─templates
    │  about.html
    │  contact.html
    │  detail.html
    │  full-width.html
    │  index.html
    │  
    └─common
            base.html
