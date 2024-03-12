from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout
import datetime
from datetime import timedelta
from django.core.mail import send_mail
from ecommerce.settings import EMAIL_HOST_USER

# Create your views here.
def indexfun(request):
    return render(request,'index.html')

def sellerlogin(request):
    if request.method=='POST':
        uname=request.POST.get('phone')
        passw=request.POST.get('passw')
        bb=sregmodelview.objects.all()
        for i in bb:
            if(i.username==uname and i.password==passw):
                request.session['id2']=i.id     #global variable is request.session  id becomes global
                return redirect(prof)
        else:
            return HttpResponse('Invalid username or password')
    return render(request,'loginseller.html')

def sellerreg(request):
    if request.method=='POST':
        imgup=request.FILES.get('imgup')
        sname=request.POST.get('sname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        cname=request.POST.get('cname')
        tl=request.POST.get('tl')
        caddress=request.POST.get('caddress')
        usernm=request.POST.get('usernm')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        a=sregmodelview(imgup=imgup,sname=sname,email=email,phone=phone,cname=cname,tl=tl,caddress=caddress,username=usernm,password=password)
        a.save()
        if password==cpassword:
            return redirect(sellerlogin)
        else:
            return HttpResponse('Invalid Password')
    return render(request,'sellerreg.html')



def productup(request):
    if request.method=='POST':
        pimage=request.FILES.get('pimage')
        pname=request.POST.get('pname')
        pcategory = request.POST.get('pcategory')
        price=request.POST.get('price')
        pdes=request.POST.get('pdes')
        cc=itemup(pimage=pimage,pname=pname,category=pcategory,price=price,pdes=pdes)
        cc.save()
        return redirect(prof)
    return render(request,'productup.html')


# def sellerprof(request):    #functionwise id
#     id1=request.session['id']
#     bb=sregmodelview.objects.get(id=id1)
#     img=str(bb.imgup).split('/')[-1]
#     return render(request,'profileview.html',{'data':bb,'img':img})


def prof(request):
    id1 = request.session['id2']
    bb = sregmodelview.objects.get(id=id1)
    img = str(bb.imgup).split('/')[-1]
    return render(request,'profileview1.html',{'data':bb,'img':img})


def profedit(request,id):
    a=sregmodelview.objects.get(id=id)
    img=str(a.imgup).split('/')[-1]
    if request.method=='POST':
        a.imgup=request.FILES['imgup']
        a.sname=request.POST.get('sname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.cname=request.POST.get('cname')
        a.tl=request.POST.get('tl')
        a.caddress=request.POST.get('caddress')
        a.save()
        return redirect(prof)


    return render(request,'update.html',{'data':a,'img':img})


def prodview(request):
    pimage=[]
    pname=[]
    price=[]
    pdes=[]
    id=[]
    categ=[]
    idd1 = request.session['id2']
    cc=sregmodelview.objects.get(id=idd1)
    img1 = str(cc.imgup).split('/')[-1]
    aa=itemup.objects.all()
    for i in aa:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'productdisp.html',{'data':mylist,'idd2':cc,'img1':img1})
    

def productedit(request,id):
    cc=itemup.objects.get(id=id)
    img=str(cc.pimage).split('/')[-1]
    if request.method=='POST':
        if request.FILES.get('pimage')==None:
            cc.save()
        else:
            cc.pimage=request.FILES['pimage']
            cc.save()
        cc.pname=request.POST.get('pname')
        if request.POST.get('pcategory')==None:
            cc.save()
        else:
            cc.category=request.POST.get('pcategory')
            cc.save()
        cc.price=request.POST.get('price')
        cc.pdes=request.POST.get('pdes')
        cc.save()
        return redirect(prodview)
    return render(request,'productedit.html',{'data':cc,'img':img,'cc':cc})

def product_delete(request,id):
    dd=itemup.objects.get(id=id)
    dd.delete()
    return redirect(prodview)


def buyrereg(request):
    if request.method=='POST':
        pimg=request.FILES.get('pimg')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        aa = buyerregmodel(pimg=pimg, fname=fname, lname=lname, email=email, phone=phone, uname=uname,
                           password=password)
        a=buyerregmodel.objects.all()
        for i in a:
            if (i.email==email or i.uname==uname):
                return HttpResponse('Already Registered')
        else:

            if password==cpassword:
                aa.save()
                subject = f'Registration Successfull'
                message = f'Your Regsitration with Grand Coffee is Successfull\nthank You'
                email_from = EMAIL_HOST_USER
                sendmail = 'shiginmadappally5@gmail.com'
                send_mail(
                    subject,
                    message,
                    email_from,
                    [sendmail]
                )
                return redirect(buyerlog)
            else:
                return HttpResponse('Invalid Password')

    return render(request,'buyerreg.html')



def buyerlog(request):
    if request.method=='POST':
        logname=request.POST.get('logename')
        logpassword=request.POST.get('logpassword')
        a=buyerregmodel.objects.all()
        for i in a:
            if (i.uname==logname and i.password==logpassword):
                request.session['id']=i.id
                return redirect(buyerdisp)
        else:
            return HttpResponse('Invalid Password')
    return render(request,'buyerlognew.html')

def buyerdisp(request):
    try:
        id1=request.session['id']
        cc=buyerregmodel.objects.get(id=id1)
        img=str(cc.pimg).split('/')[-1]
        return render(request,'buyerprofnew.html',{'data':cc,'img':img})
    except:
        request.session['id']=None
        return redirect(buyerlog)

def buyerprodview(request):
    pimage=[]
    pname=[]
    price=[]
    pdes=[]
    id=[]
    categ=[]
    idd3 = request.session['id']
    ee = buyerregmodel.objects.get(id=idd3)
    img2 = str(ee.pimg).split('/')[-1]
    aa=itemup.objects.all()

    for i in aa:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'buyerproduct view.html',{'data':mylist,'img2':img2,'ee':ee,'idd3':idd3})


def coffeeitems(request):
    pimage = []
    pname = []
    price = []
    pdes = []
    id = []
    categ = []
    idd4 = request.session['id']
    ff = buyerregmodel.objects.get(id=idd4)
    img3 = str(ff.pimg).split('/')[-1]
    a=itemup.objects.all()
    for i in a:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'cofeeitems.html',{'data':mylist,'img2':img3,'ff':ff,'idd3':idd4})


def coffeepowders(request):
    pimage = []
    pname = []
    price = []
    pdes = []
    id = []
    categ = []
    idd5 = request.session['id']
    gg = buyerregmodel.objects.get(id=idd5)
    img4 = str(gg.pimg).split('/')[-1]
    a=itemup.objects.all()
    for i in a:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'cofeepowders.html',{'data':mylist,'img4':img4,'gg':gg,'idd5':idd5})


def coffeemugs(request):
    pimage = []
    pname = []
    price = []
    pdes = []
    id = []
    categ = []
    idd6 = request.session['id']
    hh = buyerregmodel.objects.get(id=idd6)
    img5 = str(hh.pimg).split('/')[-1]
    a=itemup.objects.all()
    for i in a:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'cofeemug.html',{'data':mylist,'img5':img5,'hh':hh,'idd6':idd6})


def coffeemachines(request):
    pimage = []
    pname = []
    price = []
    pdes = []
    id = []
    categ = []
    idd7 = request.session['id']
    jj = buyerregmodel.objects.get(id=idd7)
    img6 = str(jj.pimg).split('/')[-1]
    a=itemup.objects.all()
    for i in a:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'cofeemachines.html',{'data':mylist,'img6':img6,'jj':jj,'idd7':idd7})


def coffeeblenders(request):
    pimage = []
    pname = []
    price = []
    pdes = []
    id = []
    categ = []
    idd8 = request.session['id']
    kk = buyerregmodel.objects.get(id=idd8)
    img7 = str(kk.pimg).split('/')[-1]
    a=itemup.objects.all()
    for i in a:
        pimage1=str(i.pimage).split('/')[-1]
        pimage.append(pimage1)
        pname1=i.pname
        pname.append(pname1)
        price1=i.price
        price.append(price1)
        pdes1=i.pdes
        pdes.append(pdes1)
        id1=i.id
        id.append(id1)
        cat1=i.category
        categ.append(cat1)
    mylist=zip(pimage,pname,price,pdes,id,categ)
    return render(request,'cofeeblenders.html',{'data':mylist,'img7':img7,'kk':kk,'idd7':idd8})



def buyerprofedit(request,id):
    aa=buyerregmodel.objects.get(id=id)
    img=str(aa.pimg).split('/')[-1]
    if request.method=='POST':
        aa.pimg=request.FILES['pimg']
        aa.fname=request.POST.get('fname')
        aa.lname=request.POST.get('lname')
        aa.email=request.POST.get('email')
        aa.phone=request.POST.get('phone')
        aa.uname=request.POST.get('uname')
        aa.save()
        return redirect(buyerdisp)


    return render(request,'buyerprofedit.html',{'data':aa,'img':img})



def wishlistfun(request,id):
    a=itemup.objects.get(id=id)
    id1=request.session['id']         #user id
    c=wishlist.objects.all()
    for i in c:
        if id==i.prod_id and id1==i.userid:
            return HttpResponse('item already exist')
    else:
        b=wishlist(userid=id1,prod_id=a.id,product_image=a.pimage,product_name=a.pname,prod_category=a.category,prod_price=a.price,prod_description=a.pdes)
        b.save()
        return redirect(wishlistviewfun)



def wishlistviewfun(request):
    id1 = request.session['id']
    proimage=[]
    proname=[]
    proprice=[]
    prodes=[]
    proid=[]
    procateg=[]
    prouserid=[]
    id=[]
    mm = buyerregmodel.objects.get(id=id1)
    img8 = str(mm.pimg).split('/')[-1]
    aa=wishlist.objects.all()
    for i in aa:
        proimage1=str(i.product_image).split('/')[-1]
        proimage.append(proimage1)
        proname1=i.product_name
        proname.append(proname1)
        proprice1=i.prod_category
        proprice.append(proprice1)
        prodes1=i.prod_price
        prodes.append(prodes1)
        proid1=i.prod_id
        proid.append(proid1)
        procat1=i.prod_category
        procateg.append(procat1)
        prouserid1=i.userid
        prouserid.append(prouserid1)
        id2=i.id
        id.append(id2)
    print(proid)
    mylist1=zip(proimage,proname,proprice,prodes,proid,procateg,prouserid,id)
    return render(request,'wishlistdisplay.html',{'data':mylist1,'userid':id1,'img8':img8,'mm':mm})



# def wishdelete(request):


def cartfun(request,id):
    a=itemup.objects.get(id=id)
    print(id)
    id4=request.session['id']
    cc=cart.objects.all()
    for i in cc:
        if id==i.kprod_id and id4==i.kuserid:
            return HttpResponse('already added')
    else:
        count=1
        bb=cart(kuserid=id4,kprod_id=a.id,quantity=count,kimage=a.pimage,kprodname=a.pname,kprodprice=a.price,kproddes=a.pdes,kprodcat=a.category)
        bb.save()
        return redirect(cartviewfun)

def cartviewfun(request):
    id1 = request.session['id']
    print(id1)
    proimage=[]
    proname=[]
    proprice=[]
    prodes=[]
    proid=[]
    procateg=[]
    prouserid=[]
    quantity=[]
    id2=[]
    total=0

    aa=cart.objects.filter(kuserid=id1)
    cc=delivery.objects.all()

    # aa=cart.objects.all()
    for i in aa:
        proimage1=str(i.kimage).split('/')[-1]
        proimage.append(proimage1)
        proname1=i.kprodname
        proname.append(proname1)
        proprice1=i.kprodprice
        proprice.append(proprice1)
        prodes1=i.kproddes
        prodes.append(prodes1)
        proid1=i.kprod_id
        proid.append(proid1)
        procat1=i.kprodcat
        procateg.append(procat1)
        prouserid1=i.kuserid
        prouserid.append(prouserid1)
        quantity1=i.quantity
        quantity.append(quantity1)
        idd2=i.id
        id2.append(idd2)
    total=sum(proprice)
    request.session['total_amount']=total
    request.session.save()


    mylist1=zip(proimage,proname,proprice,prodes,proid,procateg,prouserid,quantity,id2)
    ab=delivery.objects.all()
    dt=datetime.date.today()
    if request.method=='POST':
        tot=request.POST.get('total')
        addr=request.POST.get('address')
        booking_date=dt
        for j in aa:
            prod_img=j.kimage
            for i in ab:
                if i.delivery_add==addr:
                    strt=i.streetname
                    state=i.state
                    country=i.country
                    pin=i.pin
                    gg=cart_details(userid=id1,prod_img=prod_img,booking_date=booking_date,amount=tot,street=strt,city=state,country=country,pin=pin)
                    gg.save()
        return redirect(paymentcart)
    return render(request,'cartnew.html',{'data':mylist1,'userid':id1,'total':total,'cc':cc})

def deletewishlist(request,id):
    b=wishlist.objects.get(id=id)
    b.delete()

    return redirect(wishlistviewfun)


def deletecart(request,id):
    c=cart.objects.get(id=id)
    c.delete()
    return redirect(cartviewfun)



def cartinc(request,id):
    a=cart.objects.get(id=id)
    b=itemup.objects.get(id=a.kprod_id)
    price=b.price
    a.quantity+=1
    a.kprodprice=a.quantity*price
    a.save()
    return redirect(cartviewfun)

def cartdes(request,id):
    a=cart.objects.get(id=id)
    b=itemup.objects.get(id=a.kprod_id)
    price=b.price
    if a.quantity>1:
        a.quantity -= 1
        a.kprodprice=a.quantity*price
        a.save()
    return redirect(cartviewfun)



def delfun(request):
    try:
        user_id=request.session['id']
        d=delivery.objects.all()
        for i in d:
            if i.userid == user_id:
                return redirect(address_display)
        else:
            raise Exception


    except Exception:
        if request.method=='POST':
            userid=request.session['id']
            name=request.POST.get('name')
            lname=request.POST.get('lname')
            pin=request.POST.get('pin')
            delivery_add=request.POST.get('delivery_add')
            phone=request.POST.get('phone')
            streetname=request.POST.get('streetname')
            country=request.POST.get('country')
            state=request.POST.get('state')
            aa=delivery(name=name,lname=lname,pin=pin,delivery_add=delivery_add,phone=phone,streetname=streetname,country=country,state=state,userid=userid)
            aa.save()
            return redirect(address_display)
        return render(request,'shippingaddress.html')


def add_new_add(request):
    if request.method == 'POST':
        userid = request.session['id']
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        pin = request.POST.get('pin')
        delivery_add = request.POST.get('delivery_add')
        phone = request.POST.get('phone')
        streetname = request.POST.get('streetname')
        country = request.POST.get('country')
        state = request.POST.get('state')
        aa = delivery(name=name, lname=lname, pin=pin, delivery_add=delivery_add, phone=phone, streetname=streetname,
                      country=country, state=state, userid=userid)
        aa.save()
        return redirect(address_display)
    return render(request, 'shippingaddress.html')






def address_display(request):
    userid2=request.session['id']
    a=delivery.objects.all()
    if request.method=='POST':
        adrs1=request.POST.get('selected_address')
        if adrs1:
            request.session['ad']=adrs1
    return render(request,'shippingaddressdisplaynew.html',{'data':a,'user':userid2})



def delv_address(request):
    if request.method=='POST':
        userid = request.session['id']
        fname=request.POST.get('fullname')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pin=request.POST.get('zip')
        country=request.POST.get('country')
        a=delivery(name=fname,pin=pin,delivery_add=address,phone=phone,streetname=city,state=state,country=country,userid=userid)
        a.save()
        return redirect(cartviewfun)
    return render(request,'deliveryaddress.html')

def del_address_display(request):
    userid2=request.session['id']
    id=[]
    name=[]
    delivery_address=[]
    phone=[]
    street=[]
    pin=[]
    state=[]
    country=[]
    userid=[]
    a=delivery.objects.all()
    for i in a:
        name1=i.name
        name.append(name1)
        delivery_address1=i.delivery_add
        delivery_address.append(delivery_address1)
        phone1=i.phone
        phone.append(phone1)
        street1=i.streetname
        street.append(street1)
        pin1=i.pin
        pin.append(pin1)
        state1=i.state
        state.append(state1)
        country1=i.country
        country.append(country1)
        userid1=i.userid
        userid.append(userid1)
        id1=i.id
        id.append(id1)
    mylist=zip(name,delivery_address,phone,street,state,country,userid,id)
    return render(request,'del_address_display.html',{'data':a,'user':userid2,'mylist':mylist})


def delv_address_edit(request,id):
    a=delivery.objects.get(id=id)
    if request.method=='POST':
        a.userid = request.session['id']
        a.fname=request.POST.get('fullname')
        a.delivery_add=request.POST.get('address')
        a.phone=request.POST.get('phone')
        a.city=request.POST.get('city')
        a.state=request.POST.get('state')
        a.pin=request.POST.get('zip')
        a.country=request.POST.get('country')
        # a=delivery(name=fname,pin=pin,delivery_add=address,phone=phone,streetname=city,state=state,country=country,userid=userid)
        a.save()
        return redirect(del_address_display)

    return render(request,'address_edit.html',{'a':a})


def buyer_logout(request):
    logout(request)
    return redirect(buyerlog)

# def payment(request):
#     return render(request,'paymentnew.html')





def details_delivery(request):
    id10 = request.session['id']
    a = cart.objects.all()
    b = delivery.objects.all()

    price = request.session['total_amount']
    address1 = []
    ord_date = datetime.date.today()
    est_date = ord_date+timedelta(days=3)
    for i in b:
        if i.userid == id10:
            address1.append(i.name)
            address1.append(i.lname)
            address1.append(i.pin)
            address1.append(i.delivery_add)
            address1.append(i.phone)
            address1.append(i.streetname)
            address1.append(i.state)
    prodlist=[]
    for i in a:
        if i.kuserid == id10:
            pic=str(i.kimage).split('/')[-1]
            prodlist.append(pic)
            prodlist.append(i.kprodname)
            prodlist.append(i.kprodprice)
            prodlist.append(i.kproddes)
            prodlist.append(i.kprodcat)
            prodlist.append(i.quantity)

    c = confirmmodel(userid=id10,address=address1,order_date=ord_date,estimated_date=est_date,prod_details=prodlist,totalprice=price)
    c.save()
    subject=f'order confirmation'
    message=f'ordesrsuccessfull'
    email_from=EMAIL_HOST_USER
    sendmail='shiginmadappally5@gmail.com'
    send_mail(
        subject,
        message,
        email_from,
        [sendmail]
    )
    return HttpResponse('suceess')


def paymentcart(request):
    id1 = request.session['id']
    proimage=[]
    proname=[]
    proprice=[]
    prodes=[]
    proid=[]
    procateg=[]
    prouserid=[]
    quantity=[]
    id2=[]
    total=0

    aa=cart.objects.filter(kuserid=id1)

    # aa=cart.objects.all()
    for i in aa:
        proimage1=str(i.kimage).split('/')[-1]
        proimage.append(proimage1)
        proname1=i.kprodname
        proname.append(proname1)
        proprice1=i.kprodprice
        proprice.append(proprice1)
        prodes1=i.kproddes
        prodes.append(prodes1)
        proid1=i.kprod_id
        proid.append(proid1)
        procat1=i.kprodcat
        procateg.append(procat1)
        prouserid1=i.kuserid
        prouserid.append(prouserid1)
        quantity1=i.quantity
        quantity.append(quantity1)
        idd2=i.id
        id2.append(idd2)
    total=sum(proprice)
    q=sum(quantity)
    request.session['total_amount']=total
    request.session.save()
    mylist1=zip(proimage,proname,proprice,prodes,proid,procateg,prouserid,quantity,id2)
    gk=cart_details.objects.all()
    if request.method=='POST':
        cardname=request.POST.get('cardname')
        cardno=request.POST.get('cardno')
        expiry=request.POST.get('expairy')
        cvv=request.POST.get('cvv')
        for j in gk:
            prod_img=j.prod_img
            booking_date=j.booking_date
            amount=j.amount
            street=j.street
            city=j.city
            country=j.country
            pin=j.pin
            gh=cardmodel(prod_img=prod_img,booking_date=booking_date,amount=amount,street=street,city=city,country=country,pin=pin,cardname=cardname,cardno=cardno,expiry=expiry,cvv=cvv,userid=id1)
            gh.save()
        return redirect(preview_fun_new)

    return render(request,'paymentnew.html',{'data':mylist1,'userid':id1,'total':total,'qty':q})







def preview_fun(request):
    id1 = request.session['id']
    print('user',id1)
    date=[]
    amount=[]
    cardno=[]
    expiry=[]
    street=[]
    state=[]
    country=[]
    pin=[]
    userid=[]
    id=[]
    idnew=[]
    kimage=[]
    kprodname=[]
    a=cart_details.objects.all()
    b=cardmodel.objects.all()
    c=cart.objects.all()
    for i in a:
        date1=i.booking_date
        date.append(date1)
        amount1=i.amount
        amount.append(amount1)
        street1=i.street
        street.append(street1)
        state1=i.city
        state.append(state1)
        country1=i.country
        country.append(country1)
        pin1=i.pin
        pin.append(pin1)
        for j in b:
            cardno1=j.cardno
            cardno.append(cardno1[14:])
            expiry1=j.expiry
            expiry.append(expiry1)
            userid1=j.userid
            # print(userid1)
            userid.append(userid1)
            id2=j.id
            id.append(id2)
            idnew1=j.id
            # print(idnew1)
            idnew.append(idnew1)
            for k in c:
                kimage1=str(k.kimage).split('/')[-1]
                kimage.append(kimage1)
                kprodname1=k.kprodname
                kprodname.append(kprodname1)


    idd=idnew[-1]
    print('idd=',idd)
    mylist=zip(date,amount,cardno,expiry,street,state,country,pin,userid,id,idnew,kimage,kprodname)

    if request.method=='POST':
        userid = id1
        prod_name = request.POST.get('pname')
        booked_date = request.POST.get('bdate')
        amount = request.POST.get('amount')
        card_number = request.POST.get('cno')
        expiry = request.POST.get('expiry')
        street = request.POST.get('street')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zips = request.POST.get('zip')
        bc=place_order(userid=userid,prod_name=prod_name,booked_date=booked_date,amount=amount,card_number=card_number,expiry=expiry,street=street,city=state,state=country,zip=zips)
        bc.save()
        return redirect(orderplaced)
    return render(request,'preview.html',{'mylist':mylist,'user':id1,'idd':idd})




def preview_fun_new(request):
    idd20=request.session['id']
    img1=[]
    booking_date=[]
    amount=[]
    card_number=[]
    cardname=[]
    expiry=[]
    street=[]
    city=[]
    country=[]
    pin=[]
    userid=[]
    gh=cardmodel.objects.last()
    if gh:
        img11=str(gh.prod_img).split('/')[-1]
        img1.append(img11)
        booking_date1=gh.booking_date
        booking_date.append(booking_date1)
        amount1=gh.amount
        amount.append(amount1)
        card_number1=gh.cardno
        card_number.append(card_number1[13:])
        cardname1=gh.cardname
        cardname.append(cardname1)
        expiry1=gh.expiry
        expiry.append(expiry1)
        street1=gh.street
        street.append(street1)
        city1=gh.city
        city.append(city1)
        country1=gh.country
        country.append(country1)
        pin1=gh.pin
        pin.append(pin1)
        userid1=gh.userid
        userid.append(userid1)

    mylist=zip(img1,booking_date,amount,card_number,cardname,expiry,street,city,country,pin,userid)
    if request.method=='POST':
        userid = idd20
        prod_name = request.POST.get('pname')
        booked_date = request.POST.get('bdate')
        amount = request.POST.get('amount')
        card_number = request.POST.get('cno')
        expiry = request.POST.get('expiry')
        street = request.POST.get('street')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zips = request.POST.get('zip')
        bc=place_order(userid=userid,prod_name=prod_name,booked_date=booked_date,amount=amount,card_number=card_number,expiry=expiry,street=street,city=state,state=country,zip=zips)
        bc.save()
        subject = f'order confirmation'
        message = f'order successfull..Thank You for choosing Us.'
        email_from = EMAIL_HOST_USER
        sendmail = 'shiginmadappally5@gmail.com'
        send_mail(
            subject,
            message,
            email_from,
            [sendmail]
        )
        return redirect(orderplaced)
    return render(request,'preview.html',{'mylist':mylist,'user':idd20})
def orderplaced(request):
    return render(request,'ordersuccess.html')

def orders(request):
    idd=request.session['id']
    pname=[]
    bdate=[]
    amount=[]
    a=place_order.objects.all()
    for i in a:
        if idd==i.userid:
            pname1=i.prod_name
            pname.append(pname1)
            bdate1=i.booked_date
            bdate.append(bdate1)
            amount1=i.amount
            amount.append(amount1)
    mylist=zip(pname,bdate,amount)
    return render(request,'orders.html',{'mylist':mylist})


def cart_delete(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(cartviewfun)


def seller_orderhistory(request):
    pname=[]
    bdate=[]
    amount=[]
    customer_name=[]
    a=place_order.objects.all()
    b=buyerregmodel.objects.all()
    for j in b:
        idd=j.id
        for i in a:
            if idd==i.userid:
                customer_name1=j.fname
                customer_name.append(customer_name1)
                pname1=i.prod_name
                pname.append(pname1)
                bdate1=i.booked_date
                bdate.append(bdate1)
                amount1=i.amount
                amount.append(amount1)
    mylist=zip(pname,bdate,amount,customer_name)
    return render(request,'seller_orderhistory.html',{'mylist':mylist})

def gallery(request):
    return render(request,'gallery.html')

def services(request):
    return render(request,'services.html')






































