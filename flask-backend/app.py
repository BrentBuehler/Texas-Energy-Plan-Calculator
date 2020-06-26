from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import simplejson

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///energy_development'
engine = create_engine('postgresql:///energy_development')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
db = SQLAlchemy()
session = Session()
db.init_app(app)
from models import EnergyPlans



@app.route("/<zip_code>", methods=['GET'])
def db_results(zip_code):
    plans = session.query(EnergyPlans).filter_by(zip_code=zip_code)
    list_of_fields = []

    for column in plans:
        row_data = {
            'id': column.id,
            'zip_code': column.zip_code,
            'tdu_company': column.tdu_company,
            'rep_company': column.rep_company,
            'plan_name': column.plan_name,
            'price_per_kwh_500': column.price_per_kwh_500,
            'price_per_kwh_1000': column.price_per_kwh_1000,
            'price_per_kwh_2000': column.price_per_kwh_2000,
            'term_value': column.term_value,
            'prepaid': column.prepaid,
            'plan_details': column.plan_details,
            'pricing_details': column.pricing_details,
            'renewable_percentage': column.renewable_percentage,
            'enroll_phone_number': column.enroll_phone_number,
            'fact_sheet_link': column.fact_sheet_link,
            'term_sheet_link': column.term_sheet_link,
            'order_link': column.order_link,
            'new_customer': column.new_customer,
            'min_usage': column.min_usage,
            'rating': column.rating}
        list_of_fields.append(row_data)

    return simplejson.dumps(list_of_fields)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
