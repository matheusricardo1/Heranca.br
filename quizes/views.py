from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {
        'obj': quiz,
    })


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for quest in quiz.get_questions():
        answers = []
        for ans in quest.get_answers():
            answers.append(ans.text)
        questions.append({str(quest): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, pk):
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    data = request.POST
    questions = []
    data_ = dict(data.lists())
    data_.pop('csrfmiddlewaretoken')

    for k in data_.keys():
        question = Question.objects.get(text=k)
        questions.append(question)
    user = request.user
    quiz = Quiz.objects.get(pk=pk)

    score = 0
    multiplier = 100 / quiz.number_of_questions
    results = []
    for q in questions:
        a_selected = request.POST.get(q.text)
        correct_answer = None
        if a_selected:
            question_answers = Answer.objects.filter(question=q)
            for a in question_answers:
                if a_selected == a.text:
                    if a.correct:
                        score += 1
                        correct_answer = a.text
                else:
                    if a.correct:
                        correct_answer = a.text
                            
            results.append({str(q): {
                'correct_answer': correct_answer,
                'answered': a_selected,
                }})
        else:
            results.append({str(q): 'Not answered!'})
    score_ = score * multiplier
    Result.objects.create(quiz=quiz, user=user, score=score_)
    if score_ >= quiz.required_score_to_pass:
        return JsonResponse({
            'passed': True,
            'score': score_,
            'results': results,
        })
    else:
        return JsonResponse({
            'passed': False,
            'score': score_,
            'results': results,
        })
