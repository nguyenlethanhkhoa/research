from rest_framework.renderers import JSONRenderer


class ApiRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = {
            'status': 1,
            'data': data
        }

        return super().render(data, accepted_media_type, renderer_context)
