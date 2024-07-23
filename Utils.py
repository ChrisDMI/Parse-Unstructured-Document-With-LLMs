import os
import sys
from dotenv import load_dotenv, find_dotenv
import panel as pn
pn.extension()
class Utils:
    def __init__(self):
        load_dotenv(find_dotenv())
    
    def get_dlai_api_key(self):
        return os.getenv("DLAI_API_KEY")
    
    def get_dlai_url(self):
        return os.getenv("DLAI_API_URL")
     
    def get_llmwhisperer_api_key(self):
        return os.getenv("LLMWHISPERER_API_KEY")
    
    def get_llmwhisperer_api_url(self):
        return os.getenv("LLMWHISPERER_API_URL")
    
    def get_openai_api_key(self):
        return os.getenv("OPENAI_API_KEY")

class UpldFile:
    def __init__(self):
      
        self.widget_file_upload = pn.widgets.FileInput(accept='.pdf,.ppt,.png,.html', multiple=False)
        self.widget_file_upload.param.watch(self.save_filename, 'filename')
    
    def save_filename(self, _):
        if len(self.widget_file_upload.value) > 2e6:
            print("File too large. 2 MB limit.")
        else:
            self.widget_file_upload.save('./docs/' + self.widget_file_upload.filename)