from __future__ import unicode_literals
import frappe
#from werkzeug.local import Local, release_local
import os,sys, importlib, inspect, json
from frappe.utils.background_jobs import get_jobs
from frappe.utils import get_sites

def test_schedule():
	jobs_per_site={}
	if os.path.exists(os.path.join('.', '.restarting')):
		# Don't add task to queue if webserver is in restart mode
		return
	with frappe.init_site():
		jobs_per_site = get_jobs()
		sites = get_sites()
	#print(jobs_per_site)
	for site in sites:
		conf = frappe.get_site_config("/home/frappe/frappe-bench/sites","/home/frappe/frappe-bench/sites/"+site)
		if conf.db_name!="db_commeta":
			continue
		print(site)
		print(conf.db_name)
		#print (frappe.conf.db_name)
		#print(jobs_per_site[site])
		#print("\n\n")
def test():
	event="daily"
	scheduler_events = frappe.cache().get_value('scheduler_events')
	print(frappe.cache().get_value('scheduler_events'))
	print(frappe.get_hooks("scheduler_events"))
	if not scheduler_events:
		scheduler_events = frappe.get_hooks("scheduler_events")
		frappe.cache().set_value('scheduler_events', scheduler_events)

	print(scheduler_events.get(event) or [])

def do_doc():
	list=["STE-03444","STE-03754","STE-04142","STE-04193","STE-04376","STE-04434","STE-04500","STE-04721","STE-05172-3","STE-05247","STE-05264","STE-05352-1"]
	for row in list:
		print(row)
		doc=frappe.get_doc("Stock Entry",row)
		if doc.docstatus==1:
			doc.cancel()
