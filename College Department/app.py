from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Initialize the Flask app
app = Flask(__name__)

# MySQL database connection configuration
db_config = {
    'host': 'contact_form',        # MySQL host
    'user': 'root',             # MySQL username
    'password': 'root',             # MySQL password (update with your password)
    'database': 'contact_form'  # MySQL database name
}

# Route to display the contact form
@app.route('/')
def contact():
    return render_template('index.html')  # Render the Contact Us page

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Collect form data
        fullname = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert form data into the database
        cursor.execute("INSERT INTO submissions (fullname, email, message) VALUES (%s, %s, %s)",
                       (fullname, email, message))

        # Commit changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to the success page after form submission
        return redirect(url_for('success'))

# Route to display success message
@app.route('/success')
def success():
    return render_template('success.html')  # Render the Success page

if __name__ == '__main__':
    app.run(debug=True)
