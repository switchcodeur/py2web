from typing import Tuple


class Style:
    def __init__(self, *args: Tuple[tuple]):
        self.args = args
    
    def __str__(self):
        args = []
        for arg in self.args:
            args.append(":".join(arg))
        
        return ";".join(args)
    