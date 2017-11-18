from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Post
from comments.forms import CommentForm
from .models import Comment
from .forms import CommentForm
import markdown

def post_comment(request, post_pk):

    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来
    # 这里我们使用了Django提供的一个快捷函数 get_object_or_404 页面给用户
    # 这个函数的作用是当前获取的文章（post）存在时，则获取；否则返回404页面给用户
    post = get_object_or_404(Post, pk=post_pk)
    # HTTP 请求有get和POST两种，一般用户通过表单提交数据都是通过post请求

    if request.method == 'POST':
        # 用户提交的数据存在request.POST中，这是一个类字典对象
        form =  CommentForm(request.POST)
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来。
            comment.post = post
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)

        else:
            # 使用 post.comment_set.all() 反向查询全部评论。
            comment_list = post.comment_set.all()
            return render(request,'detail.html', locals())
        return redirect(post)

def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                    extensions =[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.condehilite',
                                      'markdown.extensions.toc'
                                  ])
    form = CommentForm()
    # 获取这篇post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给detail.html模板，以便渲染相应数据
    return render(request,'blog_app/detail.html', locals())



