class News:
    # category = ''
    # title = ''
    # description = ''
    # locations = []
    # link = ''
    # summery = ''
    # date_time= ''

    def __init__(self,title, description,summary,link,category,date_time):
        self.category = category
        self.title = title
        self.description = description
        self.summary = summary
        self.link = link
        self.date_time = date_time


    def print_test(self):
        print(self.title)

    def add_locations(self,locations):
        self.locations = locations
