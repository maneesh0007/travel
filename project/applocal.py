# Sample data for travel options
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
    # Sample flights for static 'Available Flights' section
    {'id': 101, 'airline': 'IndiGo', 'from': 'Delhi', 'to': 'Mumbai', 'price': 4500, 'time': '08:30', 'duration': '2h 15m', 'flight_class': 'Economy'},
    {'id': 102, 'airline': 'SpiceJet', 'from': 'Bangalore', 'to': 'Hyderabad', 'price': 3200, 'time': '14:45', 'duration': '1h 30m', 'flight_class': 'Economy'},
    {'id': 103, 'airline': 'Air India', 'from': 'Chennai', 'to': 'Delhi', 'price': 5800, 'time': '19:20', 'duration': '2h 45m', 'flight_class': 'Business'},
]

HOTELS = [
    {'id': 1, 'name': 'Taj Palace', 'location': 'Mumbai', 'price': 8000, 'rating': 5, 'type': 'Luxury'},
    {'id': 2, 'name': 'Hotel Comfort Inn', 'location': 'Bangalore', 'price': 3500, 'rating': 4, 'type': 'Business'},
    {'id': 3, 'name': 'Budget Stay', 'location': 'Delhi', 'price': 1500, 'rating': 3, 'type': 'Budget'},
    {'id': 4, 'name': 'Royal Residency', 'location': 'Hyderabad', 'price': 4000, 'rating': 4, 'type': 'Business'},
    {'id': 5, 'name': 'Sunshine Hotel', 'location': 'Ahmedabad', 'price': 3200, 'rating': 3, 'type': 'Standard'},
    {'id': 6, 'name': 'Sea View Resort', 'location': 'Chennai', 'price': 5000, 'rating': 5, 'type': 'Luxury'},
    {'id': 7, 'name': 'Grand Eastern', 'location': 'Kolkata', 'price': 4200, 'rating': 4, 'type': 'Business'},
    {'id': 8, 'name': 'Pune Suites', 'location': 'Pune', 'price': 2800, 'rating': 3, 'type': 'Budget'},
    {'id': 9, 'name': 'Jaipur Heritage', 'location': 'Jaipur', 'price': 3500, 'rating': 4, 'type': 'Heritage'},
    {'id': 10, 'name': 'Lucknow Comfort', 'location': 'Lucknow', 'price': 2700, 'rating': 3, 'type': 'Standard'},
    {'id': 11, 'name': 'Kanpur Residency', 'location': 'Kanpur', 'price': 2600, 'rating': 3, 'type': 'Standard'},
    {'id': 12, 'name': 'Nagpur Palace', 'location': 'Nagpur', 'price': 3100, 'rating': 4, 'type': 'Business'},
    {'id': 13, 'name': 'Indore Inn', 'location': 'Indore', 'price': 2500, 'rating': 3, 'type': 'Budget'},
    {'id': 14, 'name': 'Thane Residency', 'location': 'Thane', 'price': 2400, 'rating': 3, 'type': 'Standard'},
    {'id': 15, 'name': 'Bhopal Grand', 'location': 'Bhopal', 'price': 3300, 'rating': 4, 'type': 'Business'},
    {'id': 16, 'name': 'Vizag Bay Hotel', 'location': 'Visakhapatnam', 'price': 3700, 'rating': 4, 'type': 'Luxury'},
    {'id': 17, 'name': 'Patna Residency', 'location': 'Patna', 'price': 2200, 'rating': 3, 'type': 'Budget'},
    {'id': 18, 'name': 'Vadodara Suites', 'location': 'Vadodara', 'price': 2600, 'rating': 3, 'type': 'Standard'},
    {'id': 19, 'name': 'Ghaziabad Comfort', 'location': 'Ghaziabad', 'price': 2100, 'rating': 3, 'type': 'Budget'},
    {'id': 20, 'name': 'Ludhiana Palace', 'location': 'Ludhiana', 'price': 2300, 'rating': 3, 'type': 'Standard'},
    {'id': 21, 'name': 'Agra View', 'location': 'Agra', 'price': 3400, 'rating': 4, 'type': 'Heritage'},
    {'id': 22, 'name': 'Nashik Retreat', 'location': 'Nashik', 'price': 2500, 'rating': 3, 'type': 'Budget'},
    {'id': 23, 'name': 'Faridabad Residency', 'location': 'Faridabad', 'price': 2100, 'rating': 3, 'type': 'Standard'},
    {'id': 24, 'name': 'Meerut Comfort', 'location': 'Meerut', 'price': 2000, 'rating': 3, 'type': 'Budget'},
    {'id': 25, 'name': 'Rajkot Suites', 'location': 'Rajkot', 'price': 2200, 'rating': 3, 'type': 'Standard'},
    {'id': 26, 'name': 'Kalyan Residency', 'location': 'Kalyan-Dombivli', 'price': 2100, 'rating': 3, 'type': 'Budget'},
    {'id': 27, 'name': 'Vasai Virar Inn', 'location': 'Vasai-Virar', 'price': 2000, 'rating': 3, 'type': 'Budget'},
    {'id': 28, 'name': 'Varanasi Palace', 'location': 'Varanasi', 'price': 3200, 'rating': 4, 'type': 'Heritage'},
    {'id': 29, 'name': 'Srinagar Paradise', 'location': 'Srinagar', 'price': 4500, 'rating': 5, 'type': 'Luxury'},
    {'id': 30, 'name': 'Aurangabad Residency', 'location': 'Aurangabad', 'price': 2100, 'rating': 3, 'type': 'Standard'},
    # ...add more for other cities as needed...
]


from flask import Flask, render_template, request, redirect, url_for, session, flash
import boto3
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# DynamoDB Local Configuration
dynamodb = boto3.resource('dynamodb', 
                         endpoint_url='http://localhost:8000',
                         region_name='us-east-1',
                         aws_access_key_id='dummy',
                         aws_secret_access_key='dummy')

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Initialize tables
def init_db():
    import botocore
    try:
        existing_tables = [t.name for t in dynamodb.tables.all()]
        # Users table
        if 'users' not in existing_tables:
            try:
                users_table = dynamodb.create_table(
                    TableName='users',
                    KeySchema=[
                        {'AttributeName': 'email', 'KeyType': 'HASH'}
                    ],
                    AttributeDefinitions=[
                        {'AttributeName': 'email', 'AttributeType': 'S'}
                    ],
                    BillingMode='PAY_PER_REQUEST'
                )
                users_table.meta.client.get_waiter('table_exists').wait(TableName='users')
                print("Users table created!")
            except botocore.exceptions.ClientError as e:
                print(f"Error creating users table: {e}")
        else:
            print("Users table already exists.")

        # Bookings table
        if 'bookings' not in existing_tables:
            try:
                bookings_table = dynamodb.create_table(
                    TableName='bookings',
                    KeySchema=[
                        {'AttributeName': 'booking_id', 'KeyType': 'HASH'}
                    ],
                    AttributeDefinitions=[
                        {'AttributeName': 'booking_id', 'AttributeType': 'S'}
                    ],
                    BillingMode='PAY_PER_REQUEST'
                )
                bookings_table.meta.client.get_waiter('table_exists').wait(TableName='bookings')
                print("Bookings table created!")
            except botocore.exceptions.ClientError as e:
                print(f"Error creating bookings table: {e}")
        else:
            print("Bookings table already exists.")
    except Exception as e:
        print("\n[ERROR] Could not connect to DynamoDB Local. Please ensure DynamoDB Local is running on http://localhost:8000 before starting the Flask app.")
        print(f"[DETAILS] {e}\n")
        return
# --- SEARCH ENDPOINTS FOR FILTERING ---

import random

@app.route('/search_buses', methods=['POST'])
def search_buses():
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    date = request.form.get('date')
    # If both cities are selected and not the same, generate mock results
    buses = []
    if origin not in (None, '', 'Select Origin') and destination not in (None, '', 'Select Destination') and origin != destination:
        bus_names = ['Volvo AC Sleeper', 'Mercedes Multi-Axle', 'Scania AC Seater', 'Express Non-AC', 'Luxury Sleeper', 'Superfast AC', 'Deluxe Coach']
        times = ['06:00', '08:30', '12:00', '15:00', '18:30', '21:00', '23:45']
        durations = ['3h', '4h', '5h', '6h', '7h', '8h', '9h']
        for i in range(1, 6):
            buses.append({
                'id': i,
                'name': random.choice(bus_names),
                'from': origin,
                'to': destination,
                'price': random.randint(300, 1500),
                'time': random.choice(times),
                'duration': random.choice(durations)
            })
    return render_template('buses.html', buses=buses, selected_origin=origin, selected_destination=destination, selected_date=date)


@app.route('/search_trains', methods=['POST'])
def search_trains():
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    date = request.form.get('date')
    trains = []
    if origin not in (None, '', 'Select Origin') and destination not in (None, '', 'Select Destination') and origin != destination:
        train_names = ['Rajdhani Express', 'Shatabdi Express', 'Duronto Express', 'Garib Rath', 'Jan Shatabdi', 'Superfast Express', 'Intercity Express']
        times = ['05:30', '09:00', '13:15', '17:45', '20:00', '22:30']
        durations = ['4h', '5h', '6h', '7h', '8h', '10h', '12h']
        for i in range(1, 6):
            trains.append({
                'id': i,
                'name': random.choice(train_names),
                'from': origin,
                'to': destination,
                'price': random.randint(200, 2500),
                'time': random.choice(times),
                'duration': random.choice(durations)
            })
    return render_template('trains.html', trains=trains, selected_origin=origin, selected_destination=destination, selected_date=date)


@app.route('/search_flights', methods=['POST'])
def search_flights():
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    date = request.form.get('date')
    flight_class = request.form.get('flight_class', 'Economy')
    flights = []
    if origin not in (None, '', 'Select Origin') and destination not in (None, '', 'Select Destination') and origin != destination:
        airlines = ['IndiGo', 'SpiceJet', 'Air India', 'Go First', 'Vistara', 'AirAsia', 'Akasa Air']
        times = ['06:10', '08:55', '12:40', '15:25', '18:15', '21:50']
        durations = ['1h 10m', '1h 30m', '2h', '2h 15m', '2h 45m', '3h']
        class_price_multiplier = {
            'Economy': 1.0,
            'Premium Economy': 1.3,
            'Business': 2.0,
            'First': 3.0
        }
        for i in range(1, 6):
            base_price = random.randint(1500, 9000)
            price = int(base_price * class_price_multiplier.get(flight_class, 1.0))
            flights.append({
                'id': i,
                'airline': random.choice(airlines),
                'from': origin,
                'to': destination,
                'price': price,
                'time': random.choice(times),
                'duration': random.choice(durations),
                'flight_class': flight_class
            })
    return render_template('flights.html', flights=flights, selected_origin=origin, selected_destination=destination, selected_date=date, selected_class=flight_class)


@app.route('/search_hotels', methods=['POST'])
def search_hotels():
    location = request.form.get('location')
    checkin = request.form.get('checkin')
    checkout = request.form.get('checkout')
    guests = request.form.get('guests')
    # Filter hotels by location (case-insensitive, ignore 'Select City')
    filtered_hotels = [hotel for hotel in HOTELS if location and location != 'Select City' and hotel['location'].lower() == location.lower()] if location and location != 'Select City' else HOTELS
    return render_template('hotels.html', hotels=filtered_hotels, selected_location=location, checkin=checkin, checkout=checkout, guests=guests)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']
        
        users_table = dynamodb.Table('users')
        
        # Check if user already exists
        try:
            response = users_table.get_item(Key={'email': email})
            if 'Item' in response:
                flash('Email already registered!')
                return render_template('signup.html')
        except:
            pass
        
        # Create new user
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
        
        users_table = dynamodb.Table('users')
        
        try:
            response = users_table.get_item(Key={'email': email})
            if 'Item' in response:
                user = response['Item']
                if check_password_hash(user['password'], password):
                    session['user_email'] = email
                    session['user_name'] = user['name']
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid password!')
            else:
                flash('User not found!')
        except Exception as e:
            flash('Login failed!')
    
    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        return redirect(url_for('signin'))
    
    # Get user bookings
    bookings_table = dynamodb.Table('bookings')
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
    
    users_table = dynamodb.Table('users')
    try:
        response = users_table.get_item(Key={'email': session['user_email']})
        user = response.get('Item', {})
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
    # Only show the search form, not the mock FLIGHTS list, to avoid duplicate data
    return render_template('flights.html', flights=[])

@app.route('/hotels')
def hotels():
    return render_template('hotels.html', hotels=HOTELS)

@app.route('/book/<service_type>/<int:service_id>')
def book_service(service_type, service_id):
    if 'user_email' not in session:
        return redirect(url_for('signin'))
    
    service_data = None
    if service_type == 'bus':
        service_data = next((bus for bus in BUSES if bus['id'] == service_id), None)
    elif service_type == 'train':
        service_data = next((train for train in TRAINS if train['id'] == service_id), None)
    elif service_type == 'flight':
        service_data = next((flight for flight in FLIGHTS if flight['id'] == service_id), None)
    elif service_type == 'hotel':
        service_data = next((hotel for hotel in HOTELS if hotel['id'] == service_id), None)
    
    if not service_data:
        flash('Service not found!')
        return redirect(url_for('index'))
    
    return render_template('booking.html', service=service_data, service_type=service_type)

@app.route('/payment', methods=['POST'])
def payment():
    if 'user_email' not in session:
        return redirect(url_for('signin'))
    
    service_type = request.form['service_type']
    service_id = request.form['service_id']
    service_name = request.form['service_name']
    price = request.form['price']
    
    return render_template('payment.html', 
                         service_type=service_type,
                         service_id=service_id,
                         service_name=service_name,
                         price=price)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    if 'user_email' not in session:
        return redirect(url_for('signin'))
    
    # Create booking record
    booking_id = str(uuid.uuid4())
    bookings_table = dynamodb.Table('bookings')
    
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
        flash('Payment successful! Booking confirmed.')
        return render_template('booking_success.html', booking=booking_data)
    except Exception as e:
        flash('Payment failed! Please try again.')
        return redirect(url_for('dashboard'))

@app.route('/cancel_booking/<booking_id>')
def cancel_booking(booking_id):
    if 'user_email' not in session:
        return redirect(url_for('signin'))
    
    bookings_table = dynamodb.Table('bookings')
    try:
        bookings_table.update_item(
            Key={'booking_id': booking_id},
            UpdateExpression='SET #status = :status',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={':status': 'Cancelled'}
        )
        flash('Booking cancelled successfully!')
    except Exception as e:
        flash('Failed to cancel booking!')
    
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)