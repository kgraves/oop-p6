from media import Media

class Video(Media):
    fields = ['call_number', 'title', 'subjects', 'description', 'distributor', 'notes', 'series', 'label']

    def __init__(self, line):
        '''zips and stores fields and line data together into dictionary'''
        self.__data = dict(zip(Video.fields, line))
        super(Video, self).__init__(self.__data['call_number'], self.__data['title'], self.__data['subjects'], self.__data['notes'])

    def display(self):
        '''prints all of the line data'''
        for v in self.__data.values():
            if (not v == ''):
                print v
        print ''

    def compare_other(self, field, data):
        '''searches by supplied field name and data
        returns True if field exists and data matches, False otherwise
        '''
        return self.__data.has_key(field) and data in self.__data[field]

