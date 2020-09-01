from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.db.models import F
import operator


# 메인화면 & tester 입력 받기
def main(request):
    if request.GET:
        tester = Tester()
        tester.name = request.GET['tester_name']
        tester.save()
        return redirect("Test:test", tester.id)

    return render(request, "Test/main.html")


# 테스트페이지 // 3번, 4번 6번
def test_page(request, pk):
    tester = get_object_or_404(Tester, pk=pk)
    global num
    num = 1

    if request.POST:
        num = int(request.POST['question_id'])
        score = request.POST.get('score')
        # Question1
        if num == 1:
            if request.POST.get('answer1'):
                tester.Bada += int(score)
                tester.Antiseptic += int(score)
                tester.Jangma += int(score)
            elif request.POST.get('answer2'):
                tester.Sobolo += int(score)
                tester.Blackleaf += int(score)
                tester.Small += int(score)
                tester.Station += int(score)
            elif request.POST.get('answer3'):
                tester.Lofi += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Fifteen += int(score)
                tester.Love += int(score)
                tester.Meehee += int(score)
            elif request.POST.get('answer4'):
                tester.Nowrite += int(score)
                tester.Possible += int(score)
                tester.Because += int(score)
            tester.save()

        # Question2
        if num == 2:
            if request.POST.get('answer1'):
                tester.Bada += int(score)
                tester.Jangma += int(score)
            elif request.POST.get('answer2'):
                tester.Antiseptic += int(score)
                tester.Sobolo += int(score)
                tester.Small += int(score)
                tester.Meehee += int(score)
            elif request.POST.get('answer3'):
                tester.Station += int(score)
                tester.Blackleaf += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Fifteen += int(score)
            elif request.POST.get('answer4'):
                tester.Lofi += int(score)
                tester.Love += int(score)
                tester.Nowrite += int(score)
                tester.Possible += int(score)
                tester.Because += int(score)
            tester.save()

        # Question3
        if num == 3:
            if request.POST.get('answer1'):
                tester.Lofi += int(score)
                tester.Fifteen += int(score)
            elif request.POST.get('answer2'):
                tester.Antiseptic += int(score)
                tester.Meehee += int(score)
            elif request.POST.get('answer3'):
                tester.Love += int(score)
                tester.Nowrite += int(score)
                tester.Possible += int(score)
                tester.Because += int(score)
                tester.Blackleaf += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Sobolo += int(score)
                tester.Small += int(score)
            elif request.POST.get('answer4'):
                tester.Bada += int(score)
                tester.Jangma += int(score)
                tester.Station += int(score)
            tester.save()

        # Question4
        if num == 4:
            if request.POST.get('answer1'):
                tester.Fifteen += int(score)
                tester.Nowrite += int(score)
                tester.Because += int(score)
                tester.Possible += int(score)
                tester.Small += int(score)
                tester.Station += int(score)
                tester.Meehee += int(score)
            elif request.POST.get('answer2'):
                tester.Lofi += int(score)
                tester.Sobolo += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Blackleaf += int(score)
                tester.Love += int(score)
                tester.Antiseptic += int(score)
                tester.Bada += int(score)
                tester.Jangma += int(score)
            tester.save()

        # Question5
        if num == 5:
            if request.POST.get('answer1'):
                tester.Lofi += int(score)
                tester.Sobolo += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Blackleaf += int(score)
                tester.Bada += int(score)
                tester.Jangma += int(score)
                tester.Because += int(score)
                tester.Station += int(score)

            elif request.POST.get('answer2'):
                tester.Fifteen += int(score)
                tester.Love += int(score)
                tester.Nowrite += int(score)
                tester.Possible += int(score)
                tester.Small += int(score)
                tester.Antiseptic += int(score)
                tester.Meehee += int(score)
            tester.save()

        # Question6
        if num == 6:
            if request.POST.get('answer1'):
                tester.Lofi += int(score)
                tester.Blackleaf += int(score)
                tester.Fifteen += int(score)
                tester.Because += int(score)
            elif request.POST.get('answer2'):
                tester.Kind += int(score)
                tester.Sobolo += int(score)
                tester.Small += int(score)
                tester.Possible += int(score)
            elif request.POST.get('answer3'):
                tester.Love += int(score)
                tester.Nowrite += int(score)
                tester.Math += int(score)
                tester.Station += int(score)
            elif request.POST.get('answer4'):
                tester.Bada += int(score)
                tester.Jangma += int(score)
            elif request.POST.get('answer5'):
                tester.Antiseptic += int(score)
                tester.Meehee += int(score)
            tester.save()

        # Question7
        if num == 7:
            if request.POST.get('answer1'):
                tester.Sobolo += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Nowrite += int(score)
                tester.Possible += int(score)
                tester.Bada += int(score)
            elif request.POST.get('answer2'):
                tester.Jangma += int(score)
                tester.Small += int(score)
                tester.Antiseptic += int(score)
                tester.Meehee += int(score)
            elif request.POST.get('answer3'):
                tester.Lofi += int(score)
                tester.Love += int(score)
                tester.Because += int(score)
                tester.Station += int(score)
            elif request.POST.get('answer4'):
                tester.Fifteen += int(score)
                tester.Blackleaf += int(score)
            tester.save()

        # Question8
        if num == 8:
            if request.POST.get('answer1'):
                tester.Lofi += int(score)
                tester.Sobolo += int(score)
                tester.Blackleaf += int(score)
                tester.Small += int(score)
                tester.Bada += int(score)
                tester.Jangma += int(score)
                tester.Meehee += int(score)
            elif request.POST.get('answer2'):
                tester.Because += int(score)
                tester.Station += int(score)
                tester.Math += int(score)
                tester.Kind += int(score)
                tester.Fifteen += int(score)
                tester.Love += int(score)
                tester.Nowrite += int(score)
                tester.Possible += int(score)
                tester.Antiseptic += int(score)
            tester.save()

        # 다음 문제로 넘어가는 로직
        num = int(request.POST['question_id']) + 1

        # 만약 8번까지 다 입력하면 결과창 넘어감
        if num > 8:
            return redirect("Test:loading", pk)

    question = get_object_or_404(Question, id=num)
    return render(request, "Test/testpage.html", {'question': question, 'bar':8*num})


def loading(request, pk):
    tester = get_object_or_404(Tester, pk=pk)
    tester_score = [tester.Bada, tester.Possible, tester.Love, tester.Sobolo, tester.Small,
                    tester.Math, tester.Meehee, tester.Antiseptic, tester.Because, tester.Jangma, tester.Lofi,
                    tester.Blackleaf, tester.Fifteen, tester.Kind, tester.Station, tester.Nowrite]

    best_book = max(tester_score)

    for index, ts in enumerate(tester_score):
        if ts == best_book:
            book = Book.objects.get(id=index+1)

    return render(request, "Test/loading.html", {'book': book, 'tester':tester})

# 결과도출화면01
def result_01(request, pk):
    tester = get_object_or_404(Tester, pk=pk)
    tester_score = [tester.Bada, tester.Possible, tester.Love, tester.Sobolo, tester.Small,
                    tester.Math, tester.Meehee, tester.Antiseptic, tester.Because, tester.Jangma, tester.Lofi,
                    tester.Blackleaf, tester.Fifteen, tester.Kind, tester.Station, tester.Nowrite]

    best_book = max(tester_score)

    for index, ts in enumerate(tester_score):
        if ts == best_book:
            book = Book.objects.get(id=index+1)

    return render(request, "Test/result1.html", {'book': book, 'tester':tester})


# 결과도출화면02(시전문)
def result_02(request, pk):
    tester = get_object_or_404(Tester, pk=pk)
    tester_score = [tester.Bada, tester.Possible, tester.Love, tester.Sobolo, tester.Small,
                    tester.Math, tester.Meehee, tester.Antiseptic, tester.Because, tester.Jangma, tester.Lofi,
                    tester.Blackleaf, tester.Fifteen, tester.Kind, tester.Station, tester.Nowrite]

    best_book = max(tester_score)

    for index, ts in enumerate(tester_score):
        if ts == best_book:
            book = Book.objects.get(id=index+1)

    return render(request, "Test/result2.html", {'book': book, 'tester': tester})
