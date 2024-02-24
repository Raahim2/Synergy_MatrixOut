from rest_framework.response import Response
from rest_framework.views import APIView
import subprocess

class RunScanView(APIView):
    def get(self, request):
        target_url = request.query_params.get('url', 'https://example.com')

        zap_command = f"zap-cli quick-scan --self-contained -t {target_url}"
        zap_process = subprocess.Popen(zap_command.split(), stdout=subprocess.PIPE)
        zap_output, _ = zap_process.communicate()

        scan_results = {
            "zap": zap_output.decode(),
        }

        return Response(scan_results)