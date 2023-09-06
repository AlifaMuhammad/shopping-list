from django.shortcuts import render

"""merupakan deklarasi fungsi show_main, yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai."""
def show_main(request):
    context = {
        'name': 'Alifa M Hafidz',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
