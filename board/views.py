from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import *
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def main(request):
    return render(request,'board/main.html')

# 게시판 목록
def index(request):
    author =request.session.get('login_session', request.user.get_username())
    now_page = int(request.GET.get('page',1))
    boards = Board.objects.order_by('-id')
    p = Paginator(boards,11 )
    info = p.page(now_page) # info = p.get_page(now_page)
    start_page = ((now_page - 1) // 10) * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    context = {
    "info":info,
    "boards":boards,
    "author":author,
    'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'board/list.html', context)

# 게시판 글쓰기
def post(request):
    if request.method == "POST":
        author = request.session['user_id']
        # print(author)
        title = request.POST['title']
        content = request.POST['content']
        # null값이 없어야함
        if author and title and content:
            board = Board(author=author, title=title, content=content)
            board.save()
            return redirect('/index')
        else:
            messages.warning(request,"공란이 없게 해주세요")
            return redirect('/post/')
    else:
        return render(request,'board/post.html')

# 게시판 상세보기 + session
def detail(request, id):
    login_session =request.session.get('login_session', request.user.get_username())
    context = {'login_session':login_session}
    board = get_object_or_404(Board, pk=id)
    context['board'] = board
    print(board.author)
    print(login_session)
    print(context)
    if board.author == login_session:
        context['author'] = True
    else:
        context['author'] = False
    return render(request, 'board/detail.html',context)


# 게시판 삭제
def board_delete(request,id):
    board =get_object_or_404(Board, pk=id)
    board.delete()
    return redirect('/index')

# 게시판 수정
def board_edit(request,id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.author = request.session['user_id']
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.board = Board(title=board.title, content=board.content)
        board.save()
        return redirect('/post/'+str(board.id))
    else:
        return render(request,'board/update.html',{'board':board})

def cancel(request,id):
    board = Board.objects.get(pk=id)
    if request.method == "POST":
        return redirect('/index')
    else:
        return render(request,'board/post.html',{"board":board})
    






############### 기존 코드
'''def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'board/detail.html', {'board': board})'''
