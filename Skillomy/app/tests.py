def checkout(request):
	user=request.user
	course_id=request.GET.get('course_id',None)
	course=Product.objects.get(id=course_id)
	Cart(user=user,course=course).save()
	return redirect('/cart')

	address=Customer.objects.filter(user=user)
	cart_item=Cart.objects.filter(user=user)
	ammount=0.0
	total_ammount=0.0
	cart_product=[p for p in Cart.objects.all() if p.user==request.user]
	
	if cart_product:
		for p in cart_product:
			tempammount=(p.quantity * p.course.discounted_price)
			total_ammount+=tempammount
		return render(request, 'app/checkout.html',{'address':address,'total_ammount':total_ammount,'cart_item':cart_item})

	custid=request.GET.get('custid')
	customer=Customer.objects.get(id=custid)
	cart=Cart.objects.filter(user=user)
	
	for c in cart:
		OrderPlaced(user=user,customer=customer,course=c.course,quantity=c.quantity).save()
		c.delete()
	return redirect("orders")