from django.urls import re_path

from .views import (
    tickets_admin_etickets_view,
    tickets_admin_export_view,
    tickets_admin_export_yearly_statistics_view,
    tickets_admin_order_view,
    tickets_admin_orders_view,
    tickets_admin_paulig_export_view,
    tickets_admin_pos_view,
    tickets_admin_reports_view,
    tickets_admin_stats_by_date_view,
    tickets_admin_stats_view,
    tickets_admin_tools_view,
    tickets_view,
)

urlpatterns = [
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/?$",
        tickets_view,
        name="tickets_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/?$",
        tickets_admin_stats_view,
        name="tickets_admin_stats_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/by-date/raw/?$",
        tickets_admin_stats_by_date_view,
        {"raw": True},
        name="tickets_admin_stats_by_date_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/orders/?$",
        tickets_admin_orders_view,
        name="tickets_admin_orders_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/orders\.(?P<format>html)$",
        tickets_admin_paulig_export_view,
        name="tickets_admin_paulig_export_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/orders\.(?P<format>xlsx|csv)$",
        tickets_admin_export_view,
        name="tickets_admin_export_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/orders/(?P<order_id>\d+)/?$",
        tickets_admin_order_view,
        name="tickets_admin_order_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/orders/(?P<order_id>\d+)/etickets.pdf$",
        tickets_admin_etickets_view,
        name="tickets_admin_etickets_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/tools/?$",
        tickets_admin_tools_view,
        name="tickets_admin_tools_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/reports/?$",
        tickets_admin_reports_view,
        name="tickets_admin_reports_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/reports/statistics.csv$",
        tickets_admin_export_yearly_statistics_view,
        name="tickets_admin_export_yearly_statistics_view",
    ),
    re_path(
        r"events/(?P<event_slug>[a-z0-9-]+)/tickets/admin/pos/?$",
        tickets_admin_pos_view,
        name="tickets_admin_pos_view",
    ),
]
