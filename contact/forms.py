from django import forms
from .models import ContactMessage
from home.models import ProductLine

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name', 'email', 'company', 'designation', 'address', 'phone',
            'city', 'country', 'hear_about_us', 'product_interest', 'message', 'captcha'
        ]
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'company': 'Company Name',
            'designation': 'Your Designation',
            'address': 'Your Address',
            'phone': 'Phone No',
            'city': 'City',
            'country': 'Country',
            'hear_about_us': 'How Did You Hear About Us',
            'product_interest': 'Product Interested In',
            'message': 'Message',
            'captcha': '10 + 5?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # সাধারণ ফিল্ডগুলির জন্য স্টাইল যোগ করা
        for field_name, field in self.fields.items():
            if field_name not in ['hear_about_us', 'product_interest']:
                field.widget.attrs.update({'class': 'form-control', 'placeholder': self.Meta.labels.get(field_name, '')})

    # CheckboxSelectMultiple ফিল্ডগুলির জন্য স্টাইল যোগ করা
    hear_about_us = forms.MultipleChoiceField(
        choices=[
            ('search_engine', 'Search Engine'),
            ('trade_fair', 'Trade Fair'),
            ('referral', 'Referral'),
            ('other', 'Other')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    product_interest = forms.ModelMultipleChoiceField(
        queryset=ProductLine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )