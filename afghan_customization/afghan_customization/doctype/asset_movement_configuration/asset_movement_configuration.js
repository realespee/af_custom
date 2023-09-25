// Copyright (c) 2023, Raaj Tailor and contributors
// For license information, please see license.txt

frappe.ui.form.on('Asset Movement Configuration', {
	refresh: function(frm) {
		frm.set_query("asset", "asset_item", function(doc, cdt, cdn) {
            var d =locals[cdt][cdn]
            
            return {
				query: "afghan_customization.afghan_customization.doctype.asset_movement_configuration.asset_movement_configuration.asset_list_filter",
                filters:{"item": d.item,"make":d.make,"model":d.model,"capacity":d.capacity} 
            };
            
        });

        frm.set_query("asset_tag", "asset_item", function(doc, cdt, cdn) {
            var d =locals[cdt][cdn]
            
            return {
				query: "afghan_customization.afghan_customization.doctype.asset_movement_configuration.asset_movement_configuration.asset_tag_filter",
                filters:{"asset_id": d.asset} 
            };
            
        });
	}
});
