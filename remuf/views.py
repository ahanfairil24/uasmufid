from django.shortcuts import render, redirect
from .models import remuf
from .forms import remufform

# Create your views here.

def remufviews(request):
    remuf_form = remufform(request.POST or None)
    if request.method == 'POST':
        if remufform.is_valid:
            simpan_data = remuf.objects.create(
                Buku = remuf_form.cleaned_data.get('Buku'),
                Penulis = remuf_form.cleaned_data.get('Penulis'),
                Penerbit = remuf_form.cleaned_data.get('Penerbit'),
                Jumlah = remuf_form.cleaned_data.get('Jumlah'),
            )
            return redirect('remuf:remufList')
    context = {
        'form':remuf_form
    }
    return render(request, 'remuf.html', context)
