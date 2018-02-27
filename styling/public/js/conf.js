$(document).bind('toolbar_setup', function() {
	$('.navbar-home').html('<img class="erpnext-icon" src="'+
			frappe.urllib.get_base_url()+'/assets/styling/images/invi+.jpg" />');
});