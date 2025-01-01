import anthropic

class ClaudeService:
    def __init__(self, api_key):
        self.client = anthropic.Client(api_key=api_key)

    async def analyze_image(self, image_data, prompt):
        """Analyze image using Claude"""
        try:
            response = self.client.messages.create(
                model='claude-3-opus-20240229',
                max_tokens=4096,
                messages=[{
                    'role': 'user',
                    'content': [
                        {
                            'type': 'text',
                            'text': prompt
                        },
                        {
                            'type': 'image',
                            'source': {
                                'type': 'base64',
                                'media_type': 'image/jpeg',
                                'data': image_data
                            }
                        }
                    ]
                }]
            )
            return response.content[0].text
        except Exception as e:
            print(f'Analysis error: {e}')
            return None

    async def generate_script(self, prompt):
        """Generate script using Claude"""
        try:
            response = self.client.messages.create(
                model='claude-3-opus-20240229',
                max_tokens=4096,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            return response.content[0].text
        except Exception as e:
            print(f'Script generation error: {e}')
            return None