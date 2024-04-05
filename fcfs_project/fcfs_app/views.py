from django.views import View
from django.http import JsonResponse
import threading
import logging
import time
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Welcome to the FCFS app!")

class FcfsHandler(View):
    def __init__(self, max_allowed=3):
        self.max_allowed = max_allowed
        self.request_queue = []
        self.lock = threading.Lock()
        self.ongoing_requests = 0
        self.logger = logging.getLogger(__name__)
        super().__init__()

    def make_llm_request(self, prompt, api_key):
        time.sleep(5)  
        return {'response': f'Response to: {prompt}'}

    def get_llm_api_key(self):
        return "YOUR_API_KEY"

    def process_request(self, prompt):
        api_key = self.get_llm_api_key()

        # Make a request to the LLM
        response = self.make_llm_request(prompt, api_key)
        self.logger.debug(f'Response from LLM: {response}')
        return response

    def get(self, request):
        prompt = request.GET.get('prompt', '')
        response_data = self.process(prompt)
        return JsonResponse(response_data, safe=False)

    def process(self, prompt):
        with self.lock:
            if self.ongoing_requests >= self.max_allowed:
                self.request_queue.append(prompt)
                return {'message': 'Request added to the queue'}

            self.ongoing_requests += 1

        # Process the request
        response_data = self.process_request(prompt)

        with self.lock:
            self.ongoing_requests -= 1
            if self.request_queue:
                next_prompt = self.request_queue.pop(0)
                threading.Thread(target=self.process, args=(next_prompt,)).start()

        return response_data