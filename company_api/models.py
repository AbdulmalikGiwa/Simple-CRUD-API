from company_api import db, ma


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(50))
    phone_number = db.Column(db.Integer, unique=True)

    def __init__(self, company_name, email, address, phone_number):
        self.company_name = company_name
        self.address = address
        self.email = email
        self.phone_number = phone_number


class CompanySchema(ma.Schema):
    class Meta:
        fields = ('company_name', 'address', 'email', 'phone_number')


company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)



