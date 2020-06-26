from app import db


class EnergyPlans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer, nullable=False)
    tdu_company = db.Column(db.String, nullable=False)
    rep_company = db.Column(db.String, nullable=False)
    plan_name = db.Column(db.String, nullable=False)
    price_per_kwh_500 = db.Column(db.Float, nullable=False)
    price_per_kwh_1000 = db.Column(db.Float, nullable=False)
    price_per_kwh_2000 = db.Column(db.Float, nullable=False)
    term_value = db.Column(db.Integer, nullable=False)
    prepaid = db.Column(db.Boolean, nullable=False)
    plan_details = db.Column(db.String, nullable=False)
    pricing_details = db.Column(db.String, nullable=False)
    renewable_percentage = db.Column(db.Integer, nullable=False)
    enroll_phone_number = db.Column(db.String, nullable=True)
    fact_sheet_link = db.Column(db.String, nullable=True)
    term_sheet_link = db.Column(db.String, nullable=True)
    order_link = db.Column(db.String, nullable=True)
    new_customer = db.Column(db.Boolean, nullable=False)
    min_usage = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, zip_code, tdu_company, rep_company, plan_name, price_per_kwh_500, price_per_kwh_1000,
                 price_per_kwh_2000, term_value, prepaid, plan_details, pricing_details, renewable_percentage,
                 enroll_phone_number, fact_sheet_link, term_sheet_link, order_link, new_customer, min_usage, rating):
        self.id = id
        self.zip_code = zip_code
        self.tdu_company = tdu_company
        self.rep_company = rep_company
        self.plan_name = plan_name
        self.price_per_kwh_500 = price_per_kwh_500
        self.price_per_kwh_1000 = price_per_kwh_1000
        self.price_per_kwh_2000 = price_per_kwh_2000
        self.term_value = term_value
        self.prepaid = prepaid
        self.plan_details = plan_details
        self.pricing_details = pricing_details
        self.renewable_percentage = renewable_percentage
        self.enroll_phone_number = enroll_phone_number
        self.fact_sheet_link = fact_sheet_link
        self.term_sheet_link = term_sheet_link
        self.order_link = order_link
        self.new_customer = new_customer
        self.min_usage = min_usage
        self.rating = rating

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'                 : self.id,
           'zip_code'           : self.zip_code,
           'tdu_company'        : self.tdu_company,
           'rep_company'        : self.rep_company,
           'plan_name'          : self.plan_name,
           'price_per_kwh_500'  : self.price_per_kwh_500,
           'price_per_kwh_1000' : self.price_per_kwh_1000,
           'price_per_kwh_2000' : self.price_per_kwh_2000,
           'term_value'         : self.term_value,
           'prepaid'            : self.prepaid,
           'plan_details'       : self.plan_details,
           'pricing_details'    : self.pricing_details,
           'renewable_percentage': self.renewable_percentage,
           'enroll_phone_number' : self.enroll_phone_number,
           'fact_sheet_link'    : self.fact_sheet_link,
           'term_sheet_link'    : self.term_sheet_link,
           'order_link'         : self.order_link,
           'new_customer'       : self.new_customer,
           'min_usage'          : self.min_usage,
           'rating'             : self.rating
       }