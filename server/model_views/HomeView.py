import json
from datetime import datetime, timedelta
from flask_admin import BaseView, expose, AdminIndexView
from sqlalchemy import Date, cast, func

from database.models import User, Order


class HomeView(AdminIndexView):
    @staticmethod
    def get_chart_data(period=30):
        """
        :param period: number of last days to receive data
        :return: json object
        """
        from_date = datetime.now().date() - timedelta(days=period)

        labels = []
        user_registrations = []
        order_creations = []

        for i in range(1, period + 1):
            current_date = from_date + timedelta(days=i)
            labels.append(current_date.strftime('%d-%m-%Y'))

            registrations_count = User.query.filter(func.date(User.was_registered) == current_date).count()
            user_registrations.append(registrations_count)

            orders_count = Order.query.filter(func.date(Order.was_created) == current_date).count()
            order_creations.append(orders_count)

        return json.dumps({
            'period': period,
            'labels': labels,
            'registrationsCount': user_registrations,
            'ordersCount': order_creations,
        })

    @expose('/')
    def index(self):
        return self.render('home.html', chart_data=self.get_chart_data())
