class Search:
    
    def __init__(self, id, price, imgUrl, ClassName):
        self.id = id
        self.price = price
        self.imgUrl = imgUrl
        self.className = ClassName

    def __repr__(self):
        return f'<Search {self.id}>'
    
    def as_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'img_url': self.imgUrl,
            'class_name': self.className
        }
