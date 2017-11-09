class AdminIPRestrictor(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)

        if not response and self.get_response:
            response = self.get_response(request)

        return response

    def process_request(self, request):
        return None