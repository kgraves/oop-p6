from searchengine import SearchEngine

def main_loop(search_engine):
    '''performs all the user input/output and searches using SearchEngine object'''
    results = list()

    command = raw_input('command? ')
    while not command == 'exit':
        if command == 'callnumber':
            callnumber = raw_input('\tcall number? ')
            results = search_engine.search_by_call_number(callnumber)
        elif command == 'title':
            title = raw_input('\ttitle? ')
            results = search_engine.search_by_title(title)
        elif command == 'subjects':
            subjects = raw_input('\tsubjects? ')
            results = search_engine.search_by_subjects(subjects)
        elif command == 'other':
            field = raw_input('\tfield? ')
            data = raw_input('\tdata? ')
            results = search_engine.search_by_other(field, data)
        elif command == 'help':
            print """ 
                list of commands
                callnumber - searches by supplied call number
                title      - searches by supplied title
                subjects   - searches by supplied subjects
                other      - searches by supplied field name and data
                exit       - exits the program
            """
        else:
            print '\tunknown command! You can type \'help\' to see a list of commands'

        # print results
        if not command == 'help':
            print '\n%d results found\n' % len(results)
            for res in results:
                res.display()

        # clear list
        if len(results) > 0:
            del results[:]

        command = raw_input('command? ')

    del results

if __name__ == '__main__':
    '''main function for the project, execution starts here'''
    se = SearchEngine('input_files/book.txt', 'input_files/periodic.txt', 'input_files/video.txt', 'input_files/film.txt')
    main_loop(se)

    del se

