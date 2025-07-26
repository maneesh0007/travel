@app.route('/search_hotels', methods=['POST'])
def search_hotels():
    location = request.form.get('location')
    checkin = request.form.get('checkin')
    checkout = request.form.get('checkout')
    guests = request.form.get('guests')
    # Filter hotels by location (city)
    filtered_hotels = [hotel for hotel in HOTELS if hotel['location'].lower() == location.lower()] if location and location != 'Select City' else HOTELS
    return render_template('hotels.html', hotels=filtered_hotels, selected_location=location, checkin=checkin, checkout=checkout, guests=guests)
from flask import Flask, render_template, request, redirect, url_for, session, flash
import boto3
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# AWS Configuration
AWS_REGION = 'us-east-1'
USERS_TABLE = 'fixtinow_user'
SERVICES_TABLE = 'fixtinow_service'
BOOKINGS_TABLE = 'bookings'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:604665149129:fixtinow_Topic'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
sns_client = boto3.client('sns', region_name=AWS_REGION)

users_table = dynamodb.Table(USERS_TABLE)
services_table = dynamodb.Table(SERVICES_TABLE)
bookings_table = dynamodb.Table(BOOKINGS_TABLE)

# Static sample data
BUSES = [
    {'id': 1, 'name': 'Volvo AC Sleeper', 'from': 'Hyderabad', 'to': 'Bangalore', 'price': 800, 'time': '22:00', 'duration': '8h'},
    {'id': 2, 'name': 'Mercedes Multi-Axle', 'from': 'Chennai', 'to': 'Coimbatore', 'price': 650, 'time': '23:30', 'duration': '6h'},
    {'id': 3, 'name': 'Scania AC Seater', 'from': 'Mumbai', 'to': 'Pune', 'price': 400, 'time': '07:00', 'duration': '3h'},
]

TRAINS = [
    {'id': 1, 'name': 'Rajdhani Express', 'from': 'Delhi', 'to': 'Mumbai', 'price': 2500, 'time': '16:55', 'duration': '15h'},
    {'id': 2, 'name': 'Shatabdi Express', 'from': 'Bangalore', 'to': 'Chennai', 'price': 1200, 'time': '06:00', 'duration': '5h'},
    {'id': 3, 'name': 'Duronto Express', 'from': 'Kolkata', 'to': 'Delhi', 'price': 1800, 'time': '14:30', 'duration': '17h'},
]

FLIGHTS = [
    {'id': 1, 'airline': 'IndiGo', 'from': 'Delhi', 'to': 'Mumbai', 'price': 4500, 'time': '08:30', 'duration': '2h 15m'},
    {'id': 2, 'airline': 'SpiceJet', 'from': 'Bangalore', 'to': 'Hyderabad', 'price': 3200, 'time': '14:45', 'duration': '1h 30m'},
    {'id': 3, 'airline': 'Air India', 'from': 'Chennai', 'to': 'Delhi', 'price': 5800, 'time': '19:20', 'duration': '2h 45m'},
    {'id': 101, 'airline': 'IndiGo', 'from': 'Delhi', 'to': 'Mumbai', 'price': 4500, 'time': '08:30', 'duration': '2h 15m', 'flight_class': 'Economy'},
    {'id': 102, 'airline': 'SpiceJet', 'from': 'Bangalore', 'to': 'Hyderabad', 'price': 3200, 'time': '14:45', 'duration': '1h 30m', 'flight_class': 'Economy'},
    {'id': 103, 'airline': 'Air India', 'from': 'Chennai', 'to': 'Delhi', 'price': 5800, 'time': '19:20', 'duration': '2h 45m', 'flight_class': 'Business'},
]

HOTELS = [
    {'id': 1, 'name': 'Taj Palace', 'location': 'Mumbai', 'price': 8000, 'rating': 5, 'type': 'Luxury'},
    {'id': 2, 'name': 'Hotel Comfort Inn', 'location': 'Bangalore', 'price': 3500, 'rating': 4, 'type': 'Business'},
    {'id': 3, 'name': 'Budget Stay', 'location': 'Delhi', 'price': 1500, 'rating': 3, 'type': 'Budget'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']

        try:
            if 'Item' in users_table.get_item(Key={'email': email}):
                flash('Email already registered!')
                return render_template('signup.html')
        except:
            pass

        hashed_password = generate_password_hash(password)
        users_table.put_item(Item={
            'email': email,
            'password': hashed_password,
            'name': name,
            'phone': phone,
            'created_at': datetime.now().isoformat()
        })

        flash('Registration successful! Please login.')
        return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            response = users_table.get_item(Key={'email': email})
            user = response.get('Item', {})
            if user and check_password_hash(user['password'], password):
                session['user_email'] = email
                session['user_name'] = user['name']
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials!')
        except:
            flash('Login failed!')
    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        return redirect(url_for('signin'))

    try:
        response = bookings_table.scan(
            FilterExpression='user_email = :email',
            ExpressionAttributeValues={':email': session['user_email']}
        )
        bookings = response.get('Items', [])
    except:
        bookings = []

    return render_template('dashboard.html', bookings=bookings)

@app.route('/profile')
def profile():
    if 'user_email' not in session:
        return redirect(url_for('signin'))

    try:
        user = users_table.get_item(Key={'email': session['user_email']}).get('Item', {})
    except:
        user = {}

    return render_template('profile.html', user=user)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/buses')
def buses():
    return render_template('buses.html', buses=BUSES)

@app.route('/trains')
def trains():
    return render_template('trains.html', trains=TRAINS)

@app.route('/flights')
def flights():
    return render_template('flights.html', flights=[])

@app.route('/hotels')
def hotels():
    return render_template('hotels.html', hotels=HOTELS)

@app.route('/book/<service_type>/<int:service_id>')
def book_service(service_type, service_id):
    if 'user_email' not in session:
        return redirect(url_for('signin'))

    service_map = {
        'bus': BUSES,
        'train': TRAINS,
        'flight': FLIGHTS,
        'hotel': HOTELS
    }
    service_data = next((s for s in service_map.get(service_type, []) if s['id'] == service_id), None)

    if not service_data:
        flash('Service not found!')
        return redirect(url_for('index'))

    return render_template('booking.html', service=service_data, service_type=service_type)

@app.route('/payment', methods=['POST'])
def payment():
    if 'user_email' not in session:
        return redirect(url_for('signin'))

    return render_template('payment.html',
                           service_type=request.form['service_type'],
                           service_id=request.form['service_id'],
                           service_name=request.form['service_name'],
                           price=request.form['price'])

@app.route('/process_payment', methods=['POST'])
def process_payment():
    if 'user_email' not in session:
        return redirect(url_for('signin'))

    booking_id = str(uuid.uuid4())

    booking_data = {
        'booking_id': booking_id,
        'user_email': session['user_email'],
        'service_type': request.form['service_type'],
        'service_name': request.form['service_name'],
        'price': request.form['price'],
        'payment_method': request.form['payment_method'],
        'booking_date': datetime.now().isoformat(),
        'status': 'Confirmed'
    }

    try:
        bookings_table.put_item(Item=booking_data)

        # Optional: Send notification via SNS
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"Booking Confirmed: {booking_id} for {session['user_email']}",
            Subject='FixItNow Booking Confirmation'
        )

        flash('Payment successful! Booking confirmed.')
        return render_template('booking_success.html', booking=booking_data)
    except Exception as e:
        flash('Payment failed! Please try again.')
        return redirect(url_for('dashboard'))

@app.route('/cancel_booking/<booking_id>')
def cancel_booking(booking_id):
    if 'user_email' not in session:
        return redirect(url_for('signin'))

    try:
        bookings_table.update_item(
            Key={'booking_id': booking_id},
            UpdateExpression='SET #status = :status',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={':status': 'Cancelled'}
        )
        flash('Booking cancelled successfully!')
    except:
        flash('Failed to cancel booking!')

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# For AWS Elastic Beanstalk WSGI compatibility
application = app

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
