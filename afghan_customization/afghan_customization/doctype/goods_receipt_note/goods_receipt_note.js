// Copyright (c) 2023, Raaj Tailor and contributors
// For license information, please see license.txt

frappe.ui.form.on('Goods Receipt Note', {
	refresh: function(frm) {
		frm.set_read_only();
	},
	onload: function(frm) {
		frm.set_read_only();
	}
});
