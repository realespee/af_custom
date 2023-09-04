# Copyright (c) 2023, Raaj Tailor and contributors
# For license information, please see license.txt

from urllib import request
import frappe
from frappe.model.document import Document
import json
from frappe.desk.reportview import get_filters_cond, get_match_cond

class AssetRequestForm(Document):
	# pass
	def on_submit(self):
		try:
			for item in self.item_request:
				if not item.is_asset_item:
					mr_doc = frappe.get_doc({
						'doctype':'Material Request',
						'transaction_date':self.date,
						'material_request_type':'Material Transfer',
						'schedule_date':self.date,
						
					})
					item_doc = frappe.get_doc({
						'doctype':'Material Request Item',
						'item_code':item.item,
						'qty':item.qty
					})
					mr_doc.append('items', item_doc)
					mr_doc.insert(ignore_permissions = 1)
					frappe.msgprint("Your Material Request Is Created")
		except:
			frappe.log_error(message=frappe.get_traceback(),title="Creation Of Material Reuest From Asset Request Form: ")
			frappe.msgprint("Error occured while creating the Material Request, Kindly check the logs")	


@frappe.whitelist()
def create_todo(self):
	self = json.loads(self)
	try:
		if not frappe.db.exists('ToDo',{'reference_name':self['name']}):
			todo_doc = frappe.get_doc({
				'doctype':'ToDo',
				'status':'Open',
				'priority':'High',
				'date':self['date'],
				'allocated_to':self['hod'],
				'description':'Please Check Asset Request Form: <b>{0}</b>'.format(self['name']),
				'reference_type':'Asset Request Form',
				'reference_name':self['name'],
				'assigned_by':self['requested_by']
			})
			todo_doc.insert(ignore_permissions =1)
			todo = todo_doc.name
			frappe.msgprint("Your Todo Document Name Is:<b>{0}</b> created".format(todo))
		else:
			frappe.msgprint("ToDo Is Already Created For This Asset Request Form!")

	except Exception as e:
		frappe.log_error(message=frappe.get_traceback(),title="Creation Of ToDo From Asset Request Form: ")
		frappe.msgprint("Error occured while creating the ToDo, Kindly check the logs")	

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def asset_tag_filter(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql("""
        SELECT at.name,a.name
        FROM `tabAsset Tag` at
        Left Join`tabAsset` a on at.asset_id = a.name 
        WHERE a.item_code = %(item_code)s AND a.item_code LIKE %(txt)s
        {mcond}
        """.format(**{
            'key': searchfield,
            'mcond':get_match_cond(doctype)
        }),
        {
        "item_code" :filters.get("item_code") ,
        'txt': "%{}%".format(txt),
        '_txt': txt.replace("%", "")
        }
        )