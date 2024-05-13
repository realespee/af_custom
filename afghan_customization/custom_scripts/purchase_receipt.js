frappe.ui.form.on('Purchase Receipt', {
	refresh(frm) {
		// your code here
	},
	custom_assign_multiple_representative:function(frm){
		
		for(var i in frm.doc.items){
			frm.doc.items[i].assigned_representative = frm.doc.custom_assign_multiple_representative
		}
	},
	custom_assign_multiple_:function(frm){
		frappe.call({
			method: 'afghan_customization.afghan_customization.doctype_triggers.purchase_receipt.purchase_receipt.create_multiple_todo',
			args: {
				'items': frm.doc.items,
				'date':frm.doc.posting_date,
				'assign_user':frappe.session.user,
				'name':frm.doc.name

			},
			freeze: true,
			callback: (r) => {
				// on success
				console.log(r.message)	
				frm.reload_doc();
			}
		})
	}
})

frappe.ui.form.on('Purchase Receipt Item', {
	refresh:function(frm,cdt,cdn) {
		// your code here
	},
    assign:function(frm,cdt,cdn){
        var row = locals[cdt][cdn]
		
		if(!row.todo){
			frappe.call({
				method: 'afghan_customization.afghan_customization.doctype_triggers.purchase_receipt.purchase_receipt.create_todo',
				args: {
					'item_name': row.item_name,
					'qty':row.qty,
					'user':row.assigned_representative,
					'date':frm.doc.posting_date,
					'assign_user':frappe.session.user,
					'name':frm.doc.name
	
				},
				// freeze the screen until the request is completed
				freeze: true,
				callback: (r) => {
					// on success
					console.log(r.message)
					if(r.message){
						frappe.model.set_value(cdt,cdn,'todo',r.message)
						refresh_field("items")
						frappe.msgprint("Your ToDO is Create for {0}".format(user))
						frm.save();
					}
					
					
					
				},
				error: (r) => {
					// on error
				}
			})

		}
		else{
			frappe.msgprint("For This Item and Assigned Representative todo is already Created")
		}
    
    },
	quality_check_approved:function(frm,cdt,cdn){
		const l = locals[cdt][cdn]
		frappe.model.set_value(cdt,cdn,"qa_check",1)
		refresh_field("items")
		frm.save()
	},
	clear_quality_check:function(frm,cdt,cdn){
		let m = locals[cdt][cdn]
		frappe.model.set_value(cdt,cdn,"qa_check",0)
		refresh_field("items")
		frm.save()
	}
})