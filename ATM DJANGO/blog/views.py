from django.shortcuts import render
from django.http import HttpResponse
from .models import logininfo,ministatement
from django.shortcuts import render
import datetime


def home1(request):
	return render(request,'login.html')



def home2(request):
	if request.method=="POST":
		password=request.POST.get("password")
		user_name=request.POST.get("username")
		id = (logininfo.objects.get(user_name=user_name).id)
		request.session['id'] = id	
		request.session['un'] = user_name	
		
		user_obj=logininfo.objects.filter(user_name=user_name,password=password)
		if user_obj.count()==0:
			return HttpResponse("Sorry wrong password try again")
	return render(request,'home.html')



def home3(request):
	t = logininfo.objects.get(id = request.session['id'])
	context = {
		'balance': int(t.balance),
	}
	return render(request, "viewBalance.html", context) 



def home4(request):
	return render(request,'Deposit.html')       



def home5(request):
	if request.method=="POST":
		DepositAmt=request.POST.get("DepositAmt")
		t = logininfo.objects.get(id=request.session['id'])
		t.balance = int(t.balance)+int(DepositAmt) 
		t.save() 

		article = ministatement()
		article.amount = DepositAmt
		article.type = 'DEPOSIT'
		article.user_name = t.user_name
		article.abalance = int(t.balance)
		article.tdate = str(datetime.datetime.now())
		article.save()

		context = {
			'DepositAmt': DepositAmt,
			'balance': int(t.balance),
		}

	return render(request,'processDeposit.html',context) 



def home6(request):
	return render(request,'Withdraw.html') 



def home7(request):
	if request.method=="POST":
		WithdrawAmt=request.POST.get("WithdrawAmt")
		t = logininfo.objects.get(id=request.session['id'])
		t.balance = int(t.balance)-(int)(WithdrawAmt)  # change field
		t.save() # this will update only
		article = ministatement()
		article.amount = WithdrawAmt
		article.type = 'WITHDRAW'
		article.user_name = t.user_name
		article.abalance = int(t.balance)
		article.tdate = str(datetime.datetime.now())
		article.save()
	context = {
		'WithdrawAmt': WithdrawAmt,
		'balance': int(t.balance),
	}
	return render(request,'processWithdraw.html',context)      



def home8(request):
	return render(request,'editPassword.html')  



def home9(request):
	if request.method=="POST":
		cpswd=request.POST.get("cpswd")
		npswd=request.POST.get("npswd")
		cnpswd=request.POST.get("cnpswd")
		t = logininfo.objects.get(id=request.session['id'])
		if cpswd==t.password:
			if npswd==cnpswd:
				t.password=cnpswd
				t.save()
				return render(request,'processPassword.html')
	return HttpResponse("Sorry wrong password try again")		
					  
 
def home10(request):
	context = {
		'query_results' : ministatement.objects.filter(user_name=request.session['un'])
	}
	return render(request, 'mini.html',context)
