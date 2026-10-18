from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Blog, Category

def index(request):
    print("Index関数を使ってTOP画面を表示します！")
    return render(request, 'blog/index.html')

class IndexView(TemplateView):
    # print("IndexViewを使ってTOP画面を表示します！") # 表示されない
    template_name = 'blog/index.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("IndexViewを使ってTOP画面を表示します！")
        return self.render_to_response(context)

class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
