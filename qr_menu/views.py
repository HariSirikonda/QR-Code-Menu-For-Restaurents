from django.shortcuts import render
from .forms import QRCodeForm
import qrcode

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurent_name']
            url = form.cleaned_data['URL']
            
            #Generate QR Code
            qr = qrcode.make(url)
            fileName = res_name.replace(" ","").lower() + "_menu.png"
            qr.save(fileName)    
    else:
        form = QRCodeForm()
        context = { 'form' : form}
        return render(request, 'generate_qr_code.html', context)
