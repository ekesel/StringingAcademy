from django.shortcuts import render
from .models import PageConfig, Leads, Banners, Testimonials
from django.core.mail import mail_admins


def index(request):
	page_config = PageConfig.objects.filter(page_name='index').last()
	params = {}
	if request.POST and request.POST['phone']:
		try:
		    lead = Leads.objects.create(name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'],query=request.POST['query'])
		    params['response'] = 'success'
		    # message = 'Please check lead, Name: '+ lead.name + ', phone:  '+lead.phone+', email: '+lead.email+', query: ' + lead.query
		    # # mail_admins(
			# # 	'New Lead Captured',
			# # 	message
			# # )
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
	if testimonials:
		params['testimonials'] = testimonials
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		params['calling_number'] = "tel:+91" + page_config.calling_number
		
	return render(request, 'index.html', params)

def contact(request):
	page_config = PageConfig.objects.filter(page_name='contact').last()
	params = {}
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		
	return render(request, 'contact.html', params)

def about(request):
	page_config = PageConfig.objects.filter(page_name='about').last()
	params = {}
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		
	return render(request, 'about.html', params)

def pricing(request):
	page_config = PageConfig.objects.filter(page_name='pricing').last()
	params = {}
	if page_config:
		params['title'] = page_config.title
		params['meta_keywords'] = page_config.meta_keywords
		params['meta_author'] = page_config.meta_author
		params['meta_description'] = page_config.meta_description
		
	return render(request, 'pricing.html', params)