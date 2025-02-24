from . import __version__ as app_version

app_name = "afghan_customization"
app_title = "Afghan Customization"
app_publisher = "Raaj Tailor"
app_description = "Afghan Wireless Communication System"
app_email = "tailorraj111@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/afghan_customization/css/afghan_customization.css"
# app_include_js = "/assets/afghan_customization/js/afghan_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/afghan_customization/css/afghan_customization.css"
# web_include_js = "/assets/afghan_customization/js/afghan_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "afghan_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js ={
    "Stock Entry":"custom_scripts/stock_entry.js",
    "Purchase Receipt":"custom_scripts/purchase_receipt.js",
    "Item":"custom_scripts/item.js",
    "Purchase Order":"custom_scripts/purchase_order.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "afghan_customization.utils.jinja_methods",
#	"filters": "afghan_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "afghan_customization.install.before_install"
# after_install = "afghan_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "afghan_customization.uninstall.before_uninstall"
# after_uninstall = "afghan_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "afghan_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Purchase Receipt": {
		"on_submit": "afghan_customization.afghan_customization.doctype_triggers.purchase_receipt.purchase_receipt.on_submit",
	},
    "Asset":{
        "on_submit": "afghan_customization.afghan_customization.doctype_triggers.asset.asset.on_submit"
	},
    "Purchase Order":{
        "validate":"afghan_customization.afghan_customization.doctype_triggers.purchase_order.purchase_order.validate"
    },
    "Asset Movement":{
        "on_submit":"afghan_customization.afghan_customization.doctype_triggers.asset_movement.asset_movement.on_submit"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"afghan_customization.tasks.all"
#	],
#	"daily": [
#		"afghan_customization.tasks.daily"
#	],
#	"hourly": [
#		"afghan_customization.tasks.hourly"
#	],
#	"weekly": [
#		"afghan_customization.tasks.weekly"
#	],
#	"monthly": [
#		"afghan_customization.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "afghan_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "afghan_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "afghan_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"afghan_customization.auth.validate"
# ]


fixtures = [
#     {"dt": "Role", "filters": [["name", "in", [
#         'Branch Shop',
#         'Branch Shop Executive',
#         'HQ Logistic Manager',
#         'Regional Manager',
#         'Regional Warehouse Manager',
#         'HQ Finance Manager',
#         'Regional Sales Manager',
#         'HQ Warehouse Manager',
#         'HQ Sales Manager',
#         'Cashier',
#         'Regional Logistic Manager',
#         'Branch Shop Officer',
#         'Regional Finance Manager',
#     ]]]},

#     {"dt": "Role Profile", "filters": [["name", "in", [
#         'Branch Shop',
#         'Branch Shop Executive',
#         'Regional Manager',
#         'Cashier',
#         'Afghan Wireless',
#         'SAF Team'
#     ]]]},

#     {"dt": "Custom DocPerm", "filters": [["role", "in", [
#         'Branch Shop',
#         'Branch Shop Executive',
#         'HQ Logistic Manager',
#         'Regional Manager',
#         'Regional Warehouse Manager',
#         'HQ Finance Manager',
#         'Regional Sales Manager',
#         'HQ Warehouse Manager',
#         'HQ Sales Manager',
#         'Cashier',
#         'Regional Logistic Manager',
#         'Branch Shop Officer',
#         'Regional Finance Manager',
#     ]]]},

#     {"dt": "Module Profile", "filters": [["name", "in", [
#         'HQ Manager',
#         'Regional Manager',
#         'POS Agent',
#         'Safman'
#     ]]]},

    # {"dt": "Workspace", "filters": [["name", "in", [
    #     'Branch Shop Manager',
    #     'Regional Manager',
    #     'HQ Finance Manager',
    #     'Branch Executives',
    #     'HQ Logistic',
    #     'HQ Warehouse',
    #     'Asset Management',
    #     'SAF Team'
    # ]]]}

    {"dt": "UOM", "filters": [["name", "in", [
        'Can',
        'Takhta',
        'Roll',
        'Pocket',
        'Pack',
        'Lot',
        'Kit',
        'Khada',
        'Coil',
        'Carten',
        'Bottle',
        'Ballon',
        'Year',
        'Number',
        'Antenna',
        'Each',
        'Pcs'

    ]]]},
    'Item Group'

]

