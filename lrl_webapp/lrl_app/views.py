from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

def index(request):
    if request.method == "POST":
        # You can process consent here if needed
        return redirect('question', number=1)  # 'success' is the name of the URL pattern to redirect to
    return render(request, "lrl_app/index.html")

def question(request, number):

    with open('lrl_app/data/translations.json', 'r') as f:
        questions = json.load(f)['sentences']

    if request.method == "POST":
        answers = request.session.get('answers', {})
        selected = request.POST.get('selected_translation')
        custom = request.POST.get('custom_translation', '').strip()
        if selected == "__custom__" and custom:
            answer = custom
        else:
            answer = selected or ""
        answers[str(number)] = answer
        request.session['answers'] = answers
        if number < len(questions):
            return redirect('question', number=number+1)
        else:
            return redirect('success')

    item = questions[number-1]
    text = item['text']
    translations = item['translations']
    if 'translation_scores' in item:
        translation_scores = item['translation_scores']
    else:
        translation_scores = [0.9, 0.8, 0.7] # Example fallback
    translation_pairs = list(zip(translations, translation_scores))
    wbw = item['word_by_word']
    return render(request, "lrl_app/question.html", {
        'question_number': number,
        'text': text,
        'translation_pairs': translation_pairs,
        'wbw': wbw,
        'total_questions': len(questions)
    })

def success(request):
    answers = request.session.get('answers', {})
    # Load questions to display the text
    with open('lrl_app/data/translations.json', 'r') as f:
        questions = json.load(f)['sentences']

    results = []
    for i, item in enumerate(questions, start=1):
        answer = answers.get(str(i), "")
        results.append({
            'question': item['text'],
            'answer': answer
        })

    return render(request, "lrl_app/success.html", {'results': results})