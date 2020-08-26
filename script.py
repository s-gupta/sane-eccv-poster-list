from html4vision import Col, imagetable

def load_file(file_name):
    ls = []
    with open(file_name) as f:
        for l in f:
            ls.append(l.rstrip())
    return ls

def load_poster_data():
    authors = load_file('authors.txt') 
    links = load_file('links2.txt') 
    titles = load_file('title.txt') 
    poster_id = load_file('id.txt')
    links = [f'https://papers.eccv2020.eu/paper/{x}/' for x in links]
    return authors, links, titles, poster_id

def load_session_posters(session):
    ls = []
    with open(session + '.list') as f:
        for l in f:
            ls.append(int(l))
    return ls

def generate_file(out_file_name, authors, links, titles, poster_id, select_ids):
    ls = []
    for i in range(len(authors)):
        if int(poster_id[i]) in select_ids:
            print(i, poster_id[i])
            ls.append(i)
    authors = [authors[x] for x in ls]
    titles = [titles[x] for x in ls]
    poster_id = [poster_id[x] for x in ls]
    links = [links[x] for x in ls]
    cols = [Col('text', 'ID', poster_id), 
            Col('text', 'Title', titles, href=links), 
            Col('text', 'Authors', authors)]
    imagetable(cols, out_file_name, sortable=True, style="td {text-align: left} table, th, td { border: 1px solid black;  border-collapse: collapse;   padding: 5px;}")

def process():
    authors, links, titles, poster_id = load_poster_data()
    for i in ['11']: #'09', '10', '11', '12']:
        select_ids = load_session_posters(i)
        out_file_name = f'list-{i}.html'
        generate_file(out_file_name, authors, links, titles, poster_id, select_ids)

if __name__ == '__main__':
    process()
