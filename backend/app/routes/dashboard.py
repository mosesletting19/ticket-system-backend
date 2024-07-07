from flask import request, jsonify
from app.models.ticket import Ticket
from . import main_bp

@main_bp.route('/api/data', methods=['GET'])
def get_data():
    filter_query = request.args.get('filter', '').lower()
    tickets = Ticket.query.all()
    filtered_tickets = [
        ticket for ticket in tickets
        if filter_query in ticket.name.lower()
        or filter_query in ticket.email.lower()
        or filter_query in ticket.phone
    ]
    return jsonify([ticket.__dict__ for ticket in filtered_tickets])
