from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def forum(request):
    '''
    forum 목록 출력
    '''
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'community/forum.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'community/forum_detail.html', context)


def answer_create(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user # author 적용
            answer.save()
            return redirect('community:detail', question_id=question.id)

    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'community/forum_detail.html', context)


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('/community')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'community/forum_question_form.html', context)

def question_modify(request, question_id):
    '''
    community 질문 수정
    '''

    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('community:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('community:detail', question_id=question.id)

    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'community/forum_question_form.html', context=context)
