import frappe


def on_submit(self,method):
    for item in self.items:
        if item.qa_check == 0:
            frappe.throw("Quality Check For This User:{0} is Remaining".format(item.assigned_representative))

        frappe.db.set_value('Asset', {'item_code':item.item_code,'purchase_receipt':self.name}, {
            'model': item.model,
            'make': item.make,
            'capacity':item.capacity
        })
        frappe.db.commit()    

@frappe.whitelist()
def create_todo(item_name,qty,user,date,assign_user,name):
    try:
        new_doc = frappe.new_doc("ToDo")
        new_doc.allocated_to = user
        new_doc.date = date
        new_doc.priority = "High"
        new_doc.description = "Quality Check for Item Name: <b>{0}</b>, Qty:<b>{1}</b>".format(item_name,qty)
        new_doc.reference_type = "Purchase Receipt"
        new_doc.reference_name = name
        new_doc.assigned_by = assign_user

        new_doc.insert(ignore_permissions = True)
        todo_doc = new_doc.save()
        return todo_doc.name
    except:
        frappe.log_error(message = frappe.get_traceback(),title="Create ToDo from Purchase Receipt Item")
        frappe.msgprint("Error occured while creating ToDo, Kindly check the logs")