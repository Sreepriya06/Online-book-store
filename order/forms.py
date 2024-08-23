from django import forms
from django.core.validators import RegexValidator
from .models import Order

class OrderCreateForm(forms.ModelForm):
    DIVISION_CHOICES = (
    ('Bengaluru', 'Bengaluru'),
    ('Mysuru', 'Mysuru'),
    ('Tumakuru', 'Tumakuru'),
    ('Chikkamagaluru', 'Chikkamagaluru'),
    ('Kolar', 'Kolar'),
)

    DISTRICT_CHOICES = (
    ('Bangalore North', 'Bangalore North'),
    ('Bangalore Rural', 'Bangalore Rural'),
    ('Bangalore Urban', 'Bangalore Urban'),
)

    PAYMENT_METHOD_CHOICES = (
        ('UPI','UPI'),
        ('Netbanking', 'Netbanking'),
        ('Credit/Debit Card', 'Credit/Debit Card'),
        ('Cash on Delivery', 'Cash on Delivery'),
    )

    division = forms.ChoiceField(choices=DIVISION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    district = forms.ChoiceField(choices=DISTRICT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

    account_no = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^\d{10,20}$',
                message='Account number must be 10 to 20 digits long.',
                code='invalid_account_no'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your account number', 'class': 'form-control'})
    )

    transaction_id = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^\d{10,20}$',
                message='Transaction ID must be 10 to 20 digits long.',
                code='invalid_transaction_id'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your transaction ID', 'class': 'form-control'})
    )

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Enter your zip code', 'class': 'form-control'}),
        }
