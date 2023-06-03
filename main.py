from justpy import *



def mysample():
	# THIS TRANSITION ANIMATION ONLY SUPPORT IN webPage
	# NO FOR QUASARPAGE()

	app = WebPage()
	def runanimate(self,msg):
		# NOW I WANT TO SHOW AND HIDE DIV ELEMENT
		# AND YOU CAN SEE ANIMATION TRANSITION
		# WHEN I SHOW AND HIDE DIV
		if d.has_class("hidden"):
			# AND HIDE
			d.remove_class("hidden")
		else:
			d.set_class("hidden")

	# AND NOW YOU CAN DEFINE CSS ANIMATION HERE 
	# like SCALE , transform

	mytrans = {
	# THIS WILL THERE 3 PARAMETER 
	# 1. is enter = enter is you animation when div is you open
	# 2. is load = load is you animation when div is load first open
	# 3. and last is leave = leave is you div will close animation
	# if you hide div

	"enter":"transition ease-out duration-1000",
	"enter_start":"opacity-0 transform scale-0",
	"enter_end":"opacity-100 transform scale-1",
	
	# AND FOR LEAVE OR DIV WILL CLOSE HIDE
	"leave":"transition ease-out duration-1000",
	"leave_start":"opacity-100 transform scale-1",
	"leave_end":"opacity-0 transform scale-0",
	# AND IF div is open first then auto run animation


	"load":"transition ease-out duration-1000",
	"load_start":"opacity-0 transform scale-0",
	"load_end":"opacity-100 transform scale-100",


	}



	d = Div(
		classes="m-10 p-10 bg-red-200",
		text="THIS YOU ANIMATION",
		style="font-size:30px",
		a=app
		)
	d.transition = mytrans
	
	bt = Button(text="you can animate",
		click=runanimate,
		classes="bg-purple-900 text-white p-3 shadow-lg m-10",
		a=app
		)
	return app


justpy(mysample)
