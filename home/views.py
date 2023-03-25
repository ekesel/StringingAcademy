from django.shortcuts import render
from .models import PageConfig, Leads, Banners, Testimonials, Contact, Course
from django.core.mail import mail_admins
from constance import config
from django.shortcuts import redirect


def index(request):
	page_config = PageConfig.objects.filter(page_name='index').last()
	params = {}
	if request.POST and 'phone' in request.POST:
		try:
		    lead = Leads.objects.create(name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'],query=request.POST['query'])
		    params['response'] = 'success'
		    message = 'Please check lead, Name: '+ lead.name + ', phone:  '+lead.phone+', email: '+lead.email+', query: ' + lead.query
		    mail_admins(
				'New Lead Captured',
				message
			)
		except:
			params['response'] = 'error'
	banners = Banners.objects.filter(page_name='index_class')
	advantages = Banners.objects.filter(page_name='index_advantages')
	flexes = Banners.objects.filter(page_name='index_flex')
	if banners.exists():
		params['banners'] = banners
	if advantages.exists():
		params['advantages'] = advantages
	if flexes.exists():
		params['flexes'] = flexes
	testimonials = Testimonials.objects.all()
	if testimonials.exists():
		params['testimonials'] = testimonials
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		params['calling_number'] = "tel:+91" + page_config.calling_number
	params['privacy_policy'] = config.PRIVACY_POLICY
	params['cancellation_policy'] = config.CANCELLATION_POLICY
	params['terms_policy'] = config.TERMS_POLICY
	params['instagram_link'] = config.INSTAGRAM_LINK
	params['facebook_link'] = config.FACEBOOK_LINK
	params['first_line'] = config.BANNER_FIRST_LINE
	params['second_line'] = config.BANNER_SECOND_LINE
	params['third_line'] = config.BANNER_THIRD_LINE
	params['fourth_line'] = config.BANNER_FOURTH_LINE
	params['fifth_line'] = config.BANNER_FIFTH_LINE
	params['last_line'] = config.BANNER_SIXTH_LINE 
	
	return render(request, 'index.html', params)

def contact(request):
	page_config = PageConfig.objects.filter(page_name='contact').last()
	params = {}
	if request.POST:
		if 'phone' in request.POST:
			try:
				lead = Leads.objects.create(name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'],query=request.POST['query'])
				params['response'] = 'success'
				message = 'Please check lead, Name: '+ lead.name + ', phone:  '+lead.phone+', email: '+lead.email+', query: ' + lead.query
				mail_admins(
					'New Lead Captured',
					message
				)
			except:
				params['response'] = 'error'
		if 'contact_number' in request.POST:
			try:
				contact = Contact.objects.create(name=request.POST['contact_name'],phone=request.POST['contact_number'],email=request.POST['contact_email'],message=request.POST['contact_message'])
				message = 'Please check Enquiry, Name: '+ contact.name + ', phone:  '+contact.phone+', email: '+contact.email+', query: ' + contact.message
				mail_admins(
					'New Enquiry Captured',
					message
				)
				params['contact_response'] = 'success'
			except:
				params['contact_response'] = 'error'
	params['privacy_policy'] = config.PRIVACY_POLICY
	params['cancellation_policy'] = config.CANCELLATION_POLICY
	params['terms_policy'] = config.TERMS_POLICY
	params['instagram_link'] = config.INSTAGRAM_LINK
	params['facebook_link'] = config.FACEBOOK_LINK
	params['phone'] = config.CONTACT_PHONE
	params['email'] = config.CONTACT_EMAIL
	params['address'] = config.CONTACT_ADDRESS
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		params['calling_number'] = "tel:+91" + page_config.calling_number
	return render(request, 'contact.html', params)

def about(request):
	page_config = PageConfig.objects.filter(page_name='about').last()
	params = {}
	if request.POST and 'phone' in request.POST:
		try:
			lead = Leads.objects.create(name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'],query=request.POST['query'])
			params['response'] = 'success'
			message = 'Please check lead, Name: '+ lead.name + ', phone:  '+lead.phone+', email: '+lead.email+', query: ' + lead.query
			mail_admins(
				'New Lead Captured',
				message
			)
		except:
			params['response'] = 'error'
	params['privacy_policy'] = config.PRIVACY_POLICY
	params['cancellation_policy'] = config.CANCELLATION_POLICY
	params['terms_policy'] = config.TERMS_POLICY
	params['instagram_link'] = config.INSTAGRAM_LINK
	params['facebook_link'] = config.FACEBOOK_LINK
	params['about_header'] = config.ABOUT_US_HEADER
	params['about_sub_header'] = config.ABOUT_US_SUB_HEADER 
	params['about_content'] = config.ABOUT_US_CONTENT
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		params['calling_number'] = "tel:+91" + page_config.calling_number
		
	return render(request, 'about.html', params)

def pricing(request):
	page_config = PageConfig.objects.filter(page_name='pricing').last()
	params = {}
	params['privacy_policy'] = config.PRIVACY_POLICY
	params['cancellation_policy'] = config.CANCELLATION_POLICY
	params['terms_policy'] = config.TERMS_POLICY
	params['instagram_link'] = config.INSTAGRAM_LINK
	params['facebook_link'] = config.FACEBOOK_LINK
	courses = Course.objects.all()
	if courses.exists():
		params['courses'] = courses
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		params['calling_number'] = "tel:+91" + page_config.calling_number
		
	return render(request, 'pricing.html', params)

def privacy(request):
	return redirect("https://merchant.razorpay.com/policy/LVbGcTyISzngNa/privacy")

def terms(request):
	return redirect("https://merchant.razorpay.com/policy/LVbGcTyISzngNa/terms")

def cancellation(request):
	return redirect("https://merchant.razorpay.com/policy/LVbGcTyISzngNa/refund")

def shipping(request):
	return redirect("https://merchant.razorpay.com/policy/LVbGcTyISzngNa/shipping")
