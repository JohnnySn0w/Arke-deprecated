'''
spawn modules
class takes type argument, generates a tk Frame with attribs
specific to that module
'''


class MakeModule:
    def __init__(self, *args, **kwargs):
        self.attribs = {**kwargs}