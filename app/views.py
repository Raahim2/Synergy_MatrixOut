from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        web = request.POST.get('text')
        return render(request , 'index.html'  , {'web':web})
    return render(request , 'index.html'  )

from rest_framework.response import Response
from rest_framework.views import APIView
import subprocess

class RunScanView(APIView):
    def get(self, request):
        # Extract the target URL from the request
        target_url = request.query_params.get('url', 'https://example.com')

        # Example command to run Nmap scan
        nmap_command = f"nmap -p   80,443 {target_url}"
        nmap_process = subprocess.Popen(nmap_command.split(), stdout=subprocess.PIPE)
        nmap_output, _ = nmap_process.communicate()

        # Example command to run ZAP scan
        zap_command = f"zap-cli quick-scan --self-contained -t {target_url}"
        zap_process = subprocess.Popen(zap_command.split(), stdout=subprocess.PIPE)
        zap_output, _ = zap_process.communicate()

        # Combine outputs for response
        scan_results = {
            "nmap": nmap_output.decode(),
            "zap": zap_output.decode(),
        }

        return Response(scan_results)