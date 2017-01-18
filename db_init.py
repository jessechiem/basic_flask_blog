'''
Initial creation of SQLite3 database, intended to
be run once before very first deployment of site.
'''
def create_db(db_path, overwrite=False):
    '''
    If given file doesn't already exist, create
    new database via SQLite3 of single table w/
    title (TEXT) and post (TEXT), our lone model.
    '''
    import os
    if not os.path.isfile(db_path) or overwrite == True:
        print("Creating new database: {}".format(db_path))
        import sqlite3
        with sqlite3.connect(db_path) as connection:
            c = connection.cursor()
            c.execute("""CREATE TABLE blog_posts
                    (title TEXT, post TEXT)""")

if __name__ == "__main__":
    import sys
    # require database path if run on command line
    if len(sys.argv) == 2:
        create_db(sys.argv[1])
    else:
        print("Please provide path of database name.")
