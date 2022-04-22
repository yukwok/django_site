from django.shortcuts import render

# it is the application of blog app

posts = [
    {
        'author': 'Billy ng',
        'title': 'Blog 1',
        'content': 'this is the first blog',
        'createdBy': '22-4-2022'
    }, {
        'author': 'Jovi ng',
        'title': 'Blog 2',
        'content': 'this is the second blog',
        'createdBy': '23-4-2022'
    }, {
        'author': 'jankin ng',
        'title': 'Blog 3',
        'content': 'this is the third blog',
        'createdBy': '24-4-2022'
    },
    {
        'author': 'Billy yukwok ng',
        'title': 'Blog 4',
        'content': 'this is the 4 blog',
        'createdBy': '25-4-2022'
    }, {
        'author': 'Wyjun ng',
        'title': 'Blog 5',
        'content': 'this is the fifth blog',
        'createdBy': '23-4-2022'
    }, {
        'author': 'jankin wytin ng',
        'title': 'Blog 6',
        'content': 'this is the sixth blog',
        'createdBy': '29-4-2022'
    }



]


def home(request):
    context = {
        'posts': posts,
        'title': 'Posts'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})
