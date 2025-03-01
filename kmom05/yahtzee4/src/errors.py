class MissingIndex(Exception):
    """
    undantag om index saknas
    """
    def __init__(self, message="Index saknas"):
        self.message = message
        super().__init__(self.message)

class MissingValue(Exception):
    """
    undantag om värde saknas
    """
    def __init__(self, message="Värde saknas"):
        self.message = message
        super().__init__(self.message)