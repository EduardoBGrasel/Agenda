from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q # fazer o "ou" na busca
from contact.forms import ContactForm
from django.urls import reverse


# Create your views here.
def create(request):
    form_action = reverse('contact:create')

    if (request.method == 'POST'):
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid(): # verifica se o formulario é válido
            contact = form.save() # salva o form no banco de dados
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'form': ContactForm(),
        'form_action': form_action
    }
    return render(
            request,
            'contact/create.html',
            context=context
        )


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if (request.method == 'POST'):
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid(): # verifica se o formulario é válido
            contact = form.save() # salva o form no banco de dados
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }
    return render(
            request,
            'contact/create.html',
            context=context
        )

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, show=True)
    # contact.delete()
    # return redirect('contact:index')
    confirmation = request.POST.get('confirmation', 'no')
    print(confirmation)
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )