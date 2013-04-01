class Media(object):
    def __init__(self, call_number, title, subjects, notes):
        self.__call_number = call_number
        self.__title = title
        self.__subjects = subjects
        self.__notes = notes

    def compare_call_number(self, call_number):
        '''compares internal data to supplied data'''
        return call_number in self.__call_number

    def compare_title(self, title):
        '''compares internal data to supplied data'''
        return title in self.__title

    def compare_subjects(self, subjects):
        '''compares internal data to supplied data'''
        return subjects in self.__subjects

