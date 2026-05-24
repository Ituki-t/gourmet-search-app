from django import forms

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
            'placeholder': '例: ランチ',
        }),
    )