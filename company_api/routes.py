from flask import request, jsonify

from company_api import app, db
from company_api.models import Company, company_schema


# Add a company
@app.route('/company', methods=['POST'])
def add_company():
    company_name = request.json['company_name']
    address = request.json['address']
    email = request.json['email']
    phone_number = request.json['phone_number']

    new_company = Company(company_name, address, email, phone_number)

    db.session.add(new_company)
    db.session.commit()
    return company_schema.jsonify(new_company)


# Get Company Info
@app.route('/company<id>', methods=['GET'])
def get_company_info(id):
    company_info = Company.query.get(id)
    return company_schema.jsonify(company_info)


# Update Company Info
@app.route('/company<id>', methods=['PUT'])
def update_company(id):
    company_info = Company.query.get(id)

    company_name = request.json['company_name']
    address = request.json['address']
    email = request.json['email']
    phone_number = request.json['phone_number']

    company_info.company_name = company_name
    company_info.address = address
    company_info.email = email
    company_info.phone_number = phone_number

    db.session.commit()
    return company_schema.jsonify(company_info)

# Delete Company
@app.route('/company<id>', methods=['DELETE'])
def delete_company_info(id):
    company_info = Company.query.get(id)
    db.session.delete(company_info)
    db.session.commit()
    return company_schema.jsonify(company_info)
