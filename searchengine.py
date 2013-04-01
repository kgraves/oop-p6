from film import Film
from periodical import Periodical
from book import Book
from video import Video

class SearchEngine(object):
    def __init__(self, books_path, periodic_path, video_path, film_path):
        '''Reads and parses all of the specified files and stores the objects in a list'''
        self.__media = list()
        self.__read_books(books_path)
        self.__read_periodics(periodic_path)
        self.__read_videos(video_path)
        self.__read_films(film_path)

    def __read_books(self, path):
        '''calls private read_file func and creates obj'''
        lines = self.__read_file(path)
        for line in lines:
            self.__media.append(Book(line))

    def __read_periodics(self, path):
        '''calls private read_file func and creates obj'''
        lines = self.__read_file(path)
        for line in lines:
            self.__media.append(Periodical(line))

    def __read_videos(self, path):
        '''calls private read_file func and creates obj'''
        lines = self.__read_file(path)
        for line in lines:
            self.__media.append(Video(line))

    def __read_films(self, path):
        '''calls private read_file func and creates obj'''
        lines = self.__read_file(path)
        for line in lines:
            self.__media.append(Film(line))

    def __read_file(self, path):
        '''open and read file, then split each piece of data in line
        returns a list of lists, each contained list represents a line'''
        data = list()
        for line in open(path, 'r'):
            data.append(line.strip('\n').split('|'))
        return data

    def search_by_title(self, title):
        '''searches through all records and checks for match based on supplied data
        returns a list of objects that match the supplied criteria
        '''
        matches = list()
        for record in self.__media:
            if record.compare_title(title):
                matches.append(record)

        return matches

    def search_by_call_number(self, call_number):
        '''searches through all records and checks for match based on supplied data
        returns a list of objects that match the supplied criteria
        '''
        matches = list()
        for record in self.__media:
            if record.compare_title(call_number):
                matches.append(record)

        return matches

    def search_by_subjects(self, subjects):
        '''searches through all records and checks for match based on supplied data
        returns a list of objects that match the supplied criteria
        '''
        matches = list()
        for record in self.__media:
            if record.compare_title(subjects):
                matches.append(record)

        return matches

    def search_by_other(self, field, data):
        '''searches through all records and checks for match based on supplied data
        returns a list of objects that match the supplied criteria
        '''
        matches = list()
        for record in self.__media:
            if record.compare_other(field, data):
                matches.append(record)

        return matches

