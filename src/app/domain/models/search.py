class Search:
    
    def __init__(self, id, price, img_url, analyze):
        self.id = id
        self.price = price
        self.img_url = img_url
        self.analyze = analyze

    def __repr__(self):
        return f'<Search {self.id}>'

    def as_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'img_url': self.img_url,
            'analyze': self.analyze
        }
