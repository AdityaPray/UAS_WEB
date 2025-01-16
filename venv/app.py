from flask import Flask, render_template, request, redirect, url_for, session, flash
from main import fetch_all_places, insert_place, fetch_place_by_id, update_place, delete_place

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Route Home untuk Pengunjung
@app.route('/')
def index():
    places = fetch_all_places()  # Ambil data dari database
    print("DEBUG: Places sent to template:", places)  # Debugging tambahan
    return render_template('Web.html', places=places)


# Route Login untuk Pemilik Web
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin_password':
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!')
    return render_template('login.html')

# Route Dashboard
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        places = fetch_all_places()
        return render_template('dashboard.html', places=places)
    else:
        flash('Please log in first!')
        return redirect(url_for('login'))

# Route untuk Tambah Tempat Wisata
@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'loggedin' in session:
        if request.method == 'POST':
            nama = request.form['nama']
            url_gambar = request.form['url_gambar']
            deskripsi = request.form['deskripsi']
            insert_place(nama, url_gambar, deskripsi)
            return redirect(url_for('dashboard'))
        return render_template('create.html')
    else:
        flash('Please log in first!')
        return redirect(url_for('login'))

# Route untuk Update Tempat Wisata
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if 'loggedin' in session:
        if request.method == 'POST':
            nama = request.form['nama']
            url_gambar = request.form['url_gambar']
            deskripsi = request.form['deskripsi']
            update_place(id, nama, url_gambar, deskripsi)
            return redirect(url_for('dashboard'))
        place = fetch_place_by_id(id)
        return render_template('update.html', place=place)
    else:
        flash('Please log in first!')
        return redirect(url_for('login'))

# Route untuk Hapus Tempat Wisata
@app.route('/delete/<int:id>')
def delete(id):
    if 'loggedin' in session:
        delete_place(id)
        return redirect(url_for('dashboard'))
    else:
        flash('Please log in first!')
        return redirect(url_for('login'))

# Route Logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
