import pymysql
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Load config file.
app.config.from_pyfile('config.py')
cors = CORS(app)


def get_db_connection():
    # Set up MySql connection
    conn = pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           passwd=app.config['DB_PASS'],
                           database="urlshortener",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


# Define hash length, plus hidden salt.
hashids = Hashids(min_length=8, salt=app.config['SECRET_KEY'])


@app.route('/', methods=('GET', 'POST'))
def index():
    # Set up connection and link
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check method is POST
    if request.method == 'POST':
        # Grab parameter from form
        url = request.form['url']
        # Error handling if no URL inputted.
        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        # Add new url to local variable and table.
        cursor.execute('INSERT INTO urls (`original_url`) VALUES (%s)',
                       (url,))
        # Commit to database and close connections.
        conn.commit()
        cursor.close()
        conn.close()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM urls ORDER BY id DESC LIMIT 1')
        url_data = cursor.fetchone()
        # Get last row of table.
        url_id = str(url_data)
        # Encode url.
        numeric_filter = filter(str.isdigit, url_id)
        numeric_string = "".join(numeric_filter)
        idinteger = int(numeric_string)
        hashid = hashids.encode(idinteger)
        # Create shortened url.
        short_url = request.host_url + hashid

        # Jump to the url redirect method with data.
        return render_template('index.html', short_url=short_url)

    # Load page again if GET request.
    return render_template('index.html')


@app.route('/<id>')
def url_redirect(id):
    # Set up connection and link
    conn = get_db_connection()
    cursor = conn.cursor()

    # Decode hashed id into old link.
    original_id = hashids.decode(id)
    # Check if url exists.
    if original_id:
        # Get first instance of url in case of duplicates.
        original_id = original_id[0]
        # Fetch appropriate fields than match id.
        cursor.execute('SELECT original_url, clicks FROM urls'
                       ' WHERE id = %s', (original_id,)
                       )
        url_data = cursor.fetchone()
        # Assign local variables to updated table data.
        original_url = url_data['original_url']
        clicks = url_data['clicks']

        # Update table with new click.
        cursor.execute('UPDATE urls SET clicks = %s WHERE id = %s',
                       (clicks + 1, original_id))

        # Commit to database and close connections.
        conn.commit()
        cursor.close()
        conn.close()
        # Load decoded url.
        return redirect(original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))


@app.route('/about')
def about():
    # Load about page (placeholder).
    return render_template('about.html')


@app.route('/stats')
def stats():
    # Set up connection and link.
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all records from database.
    cursor.execute('SELECT id, original_url, clicks FROM urls')
    db_urls = cursor.fetchall()
    # Commit to database and close connections.
    conn.commit()
    cursor.close()
    conn.close()

    # Create array.
    urls = []

    # Populate array
    for url in db_urls:
        url = dict(url)
        url['short_url'] = request.host_url + hashids.encode(url['id'])
        urls.append(url)

    # Load stats page with populated array.
    return render_template('stats.html', urls=urls)


if __name__ == '__main__':
    app.run(port=40001, debug=True)
