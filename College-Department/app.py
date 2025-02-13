from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

# Define Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')

@app.route('/staffs')
def staffs():
    return render_template('staffs.html')

@app.route('/profileofthedepartment')
def profile():
    return render_template('profileofthedepartment.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/metaofficeofcoe')
def metaofficeofcoe():
    return render_template('metaofficeofcoe.html')

@app.route('/cia')
def cia():
    return render_template('cia.html')

@app.route('/semester')
def semester():
    return render_template('semester.html')

@app.route('/rulesandregulations')
def rulesandregulations():
    return render_template('rulesandregulatations.html')

@app.route('/coedowntheyears')
def coedowntheyears():
    return render_template('coedowntheyears.html')

@app.route('/studentsclub')
def studentsclub():
    return render_template('studentsclub.html')

@app.route('/scholership')
def scholership():
    return render_template('schollership.html')

@app.route('/counsellor')
def counsellor():
    return render_template('counsellor.html')

@app.route('/trainingandplacement')
def training_and_placement():
    return render_template('trainingandplacement.html')

@app.route('/enhancementscheme')
def enhancement_scheme():
    return render_template('enhancementscheme.html')


@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save data to database
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        flash('Your message has been received successfully!', 'success')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)