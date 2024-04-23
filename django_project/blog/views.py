from django.shortcuts import render

posts = [
    {
        'author' : 'Jane Doe',
        'title' : 'Times of India',
        'content' : 'First post content',
        'date_posted' : 'April 10, 2024'
    },
    {
        'author' : 'John Connor',
        'title' : 'The Mint',
        'content' : 'Second post content',
        'date_posted' : 'April 12, 2024'
    },
    {
        'author' : 'Michael Kentucky',
        'title' : 'London Times',
        'content' : 'Third post content',
        'date_posted' : 'April 12, 2024'
    }
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title' : 'About'})