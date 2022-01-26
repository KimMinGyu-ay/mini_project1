from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import *
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

# 게시판 목록
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'board/list.html', boards)

# 게시판 글쓰기
def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        # null값이 없어야함
        if author and title and content:
            board = Board(author=author, title=title, content=content)
            board.save()
            return redirect('/index')

        # null값이면 post계속하기(alert추가해야함)
        else:
            return redirect('/post/')
    else:
        return render(request,'board/post.html')
def cancel(request):
    if request.method == "POST":
        return redirect('/index')
    else:
        return render(request,'board/post.html')
# 게시판 상세보기
def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'board/detail.html', {'board': board})

# 게시판 삭제
def board_delete(request,id):
    board =get_object_or_404(Board, pk=id)
    board.delete()
    return redirect('/index')


#게시판 수정
def board_update(request,id):
    board =get_object_or_404(Board, pk=id)
    if request.method == 'POST':
        # board.author = request.POST['author']
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.board = Board( title=board.title, content=board.content)
        board.save()
        return redirect('/post/'+str(board.id))
    else:
        return render(request,'board/update.html',{'board':board})
