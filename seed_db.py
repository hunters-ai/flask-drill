from app import app
from database.db import db
from model.detector import Detector
from model.organization import Organization


def seed_db():
    with app.app_context():
        db.create_all()

        # Create Some organizations
        organizations = [
            Organization(id=1, name='Hunters'),
            Organization(id=2, name='Google'),
            Organization(id=3, name='Databricks'),
            Organization(id=4, name='Amazon')
        ]

        detectors = [
            Detector(id=1, name='suspicious_signin'),
            Detector(id=2, name='platform_alerts')
        ]

        # Insert organizations
        for org in organizations:
            db.session.add(org)

        # Insert detectors
        for detector in detectors:
            db.session.add(detector)

        db.session.commit()


if __name__ == "__main__":
    seed_db()
