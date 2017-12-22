from django.shortcuts import render
from jdshow.models import jdproduct
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from decimal import Decimal
# Create your views here.
def index(request):
    items = jdproduct.objects[:10]
    price_list  = []
    phone_name = []
    for i in items:
        price_list.append(i['product_price'])
        phone_name.append(i['product_name'][:5])
    paginator = Paginator(items,10)#每页10条数据
    page = request.GET.get("page")#获得当前的页数
    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)#不是整数就显示一页
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)#空就显示最后一页

    return render(request,'jdshow/index.html',{"items":rows,'price':price_list,'name':phone_name})

#详情页面
def detail(request,product_id):
    items = jdproduct.objects(product_id = product_id)
    url = 'https:'+items.first().product_url
    good_count = items.first().good_commt_num #好评
    gen_count = items.first().gen_commt_num #中评
    bad_count = items.first().bad_commt_num #差评
    comment_count = items.first().comment_num #评论数量
    good_comment_rate = round(Decimal(good_count)/int(comment_count))
    bad_count_rate = round(Decimal(good_count)/int(bad_count))
    gen_count_rate = round(Decimal(good_count)/int(gen_count))
    data = {'good_rate':good_comment_rate,'url':url,'comment':comment_count,'bad_rate':bad_count_rate,
            'gen_rate':gen_count_rate,'good':good_count,'bad':bad_count,'gen':gen_count

    }
    return  render(request,'jdshow/detail.html',{"items":items,"data":data})

