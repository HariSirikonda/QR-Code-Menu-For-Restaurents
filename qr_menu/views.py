from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurent_name']
            url = form.cleaned_data['URL']
            
            #Generate QR Code
            qr = qrcode.make(url)
            fileName = res_name.replace(" ","_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, fileName)
            qr.save(file_path)

            #create Image URL
            qr_url = os.path.join(settings.MEDIA_URL, fileName)


            context = {
                'res_name' : res_name,
                'qr_url' : qr_url,
                'file_name' : fileName
            }
            return render(request, 'qr_result.html', context) 
    else:
        form = QRCodeForm()
        context = { 'form' : form}
        return render(request, 'generate_qr_code.html', context)
