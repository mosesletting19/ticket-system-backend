from flask import request, jsonify
from app.models.ticket import Ticket
from app.database import db
from . import main_bp

@main_bp.route('/api/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = Ticket(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        category=data['category'],
        tickets=data['tickets']
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket created successfully!'}), 201
