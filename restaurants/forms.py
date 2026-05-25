from django import forms
from .hotpepper import get_genre_list
from .hotpepper import get_budget_list

class SearchForm(forms.Form):
    range = forms.ChoiceField(
        label='検索範囲',
        choices=[
            ('1', '300m'),
            ('2', '500m'),
            ('3', '1000m'),
            ('4', '2000m'),
            ('5', '3000m'),
        ],
        initial='3',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'range',
        }),
    )
    keyword = forms.CharField(
        label='キーワード',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'keyword',
            'placeholder': '例: ランチ, 店名 など',
        }),
    )
    genre = forms.ChoiceField(
        label='ジャンルを選択',
        required=False,
        choices=[
            ('', '選択してください'),
        ] + [(genre['code'], genre['name']) for genre in get_genre_list()],
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'genre',
        }),
    )
    budget = forms.ChoiceField(
        label='予算を選択',
        required=False,
        choices=[
            ('', '選択してください'),
        ] + [(budget['code'], budget['name']) for budget in get_budget_list()],

        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'budget',
        }),
    )