import requests
from bs4 import BeautifulSoup
# pip3 install requests
# pip3 install BeautifulSoup4
# 练习题一：获取一个
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3')
# print(h3)
# 找到所有新闻
# 标题，简介，url，图片
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# print(response.text)
# soup = BeautifulSoup(response.text,'html.parser')

html = """<!doctype html>
<html>
<head>
	<meta charset="gb2312" />
	<title>【图】最新汽车新闻_资讯_汽车之家</title>
<meta name="keywords" content="最新汽车新闻,汽车新闻">
<meta name="description" content="汽车之家新闻频道提供国产新车,进口新车,汽车热点追踪,汽车行业动态,车闻轶事,人物访谈等最新信息.">
    <meta name="robots" content="all" />
	<link href="http://x.autoimg.cn/com/bo.ashx?path=|as|css-2.0.2|global|autoshow.css,|as|css-2.0.2|infor|focusimg.css,|as|css-2.0.2|infor|nav-typebar.css,|as|css-2.0.2|infor|page.css,|as|css-2.0.2|infor|search.css,|as|css-2.0.2|public|btn.css,|as|css-2.0.2|public|icon.css,|as|css-2.0.2|public|gotop.css,|as|static|monkey.css" rel="stylesheet">
    <link href="" rel="stylesheet">
    <style type="text/css">
        @charset "UTF-8";a.more{display:inline-block;position:absolute;right:10px;top:0;z-index:200;font-size:12px;font-weight:100;font-family:"\5B8B\4F53"}a.more:link,a.more:visited{color:#666;text-decoration:none}a.more:hover{color:#d60000;text-decoration:underline}.navFixed{position:fixed;_position:absolute;top:0;z-index:990}.hot-title,.relative{position:relative}.nav-typebar{width:990px}.subnav{margin-top:10px;margin-bottom:20px}.subnav-title-name{padding-bottom:5px;font:700 22px/1.5 'Microsoft YaHei',arial,tahoma,sans-serif;color:#3a5998}.subnav-title-ad{padding:3px 0 0 15px}.subnav-title-ad img{vertical-align:top;width:65px;height:30px;*margin-top:-4px}.subnav-title-ad span{font:16px 'Microsoft YaHei',arial,tahoma,sans-serif;line-height:30px}.advbox{line-height:0}.icon-tuiguang{display:inline-block;height:12px;padding:1px 1px 1px 2px;background-color:#d60000;overflow:hidden;vertical-align:middle;text-align:center;font-family:"\5B8B\4F53",arial,tahoma,sans-serif;font-weight:400;font-style:normal;font-size:12px;line-height:12px;color:#fff;-webkit-border-radius:2px;-moz-border-radius:2px;border-radius:2px}.advlist{margin:10px 0;font-size:14px;font-weight:700;line-height:20px}.advlist i{float:left;margin:1px 0 0}.advlist li,.advlist ul{float:left}.advlist li{width:194px;padding-left:6px}.advlist a{color:#666}.advlist a:hover{color:#d60000;text-decoration:underline}.news,.news-focus p{height:36px;color:#666}.grid-left{padding-right:20px;border-right:1px solid #f0f0f0}.content .row .grid-right{width:309px;margin-left:20px;_margin-left:10px}.num-big{font-size:32px}.num-small{font-size:18px}.news{width:545px;line-height:18px}.news-focus h2{font:28px/1.5 'Microsoft YaHei',arial,tahoma,sans-serif}.news-focus p{line-height:18px;margin-bottom:15px}.article-wrapper ul,.article-wrapper ul li a:link,.article-wrapper ul li a:visited{color:#999}.news-focus .focusimg02 .focusimg-pic,.news-focus .focusimg02 .focusimg-pic ul{height:413px}.news-focus .focusimg02 .focusimg-bt-left,.news-focus .focusimg02 .focusimg-bt-right{height:323px;top:90px}.news-focus .focusimg02 .focusimg-bt a{margin-top:130px}.news-focus .focusimg02 .focusimg-bt-left{left:0;padding-left:10px}.news-focus .focusimg02 .focusimg-bt-right{right:0;padding-right:10px}.article-wrapper{width:630px;margin-top:10px}.article-wrapper ul li{height:100px;padding-top:10px}.article-wrapper ul li a{display:block;*display:inline-block;width:620px;height:100px;padding:0 5px;overflow:hidden;cursor:pointer}.loading,.loading-cont,.loadmore{display:inline-block}.article-wrapper ul li a:hover{text-decoration:none;background-color:#f9f9f9}.article-wrapper ul li img{float:left;margin-right:15px;padding-top:5px}.article-wrapper ul li h3{line-height:30px;font-family:\5FAE\8F6F\96C5\9ED1;font-size:18px;color:#3b5998}.article-wrapper ul li h3 i{margin-left:10px}.article-wrapper ul li .article-bar{height:21px;line-height:21px;overflow:hidden;padding-bottom:5px}.article-wrapper ul li .article-bar em{display:inline-block;line-height:16px;padding-left:20px;font-size:12px}.article-wrapper ul li .article-bar i{float:left;margin:2px 3px 0 0}.article-wrapper ul li p{line-height:22px}.loading,.loadmore{width:630px;height:40px;border-radius:5px;background:#efefef;text-align:center;font:700 18px/40px "\5B8B\4F53",arial,tahoma,sans-serif;color:#666}.loadmore:hover{background:#333;text-decoration:none;color:#fff}.loading{margin-top:20px}.loading img{margin-top:10px;margin-left:5px;vertical-align:top}.loading:hover{text-decoration:none;color:#666}.page{margin-top:20px}.editorblog,.hot{margin-top:15px;margin-bottom:15px}.hot-title{_margin-top:2px}.editorblog-title,.hot-title{border-bottom:2px solid #3b5998;padding-bottom:12px;font:700 14px/14px "\5B8B\4F53",arial,tahoma,sans-serif}.hot-more{float:right;font-weight:400;font-style:normal;font-size:12px}.comment-ul li{width:309px;margin-bottom:20px;vertical-align:top}.comment-tittle{height:23px;font-size:12px;color:#999;white-space:nowrap}.comment-tittle div{line-height:20px}.comment-tittle a{font-size:14px}.comment-tittle .comment-pic{width:30px;height:30px;float:left;margin-right:10px}.comment-content{margin-bottom:9px;*margin-bottom:6px}.comment-content a{display:block;*display:inline-block;width:307px;position:relative;border:1px solid #ccd3e4;background-color:#f9f9f9;-moz-border-radius:3px;border-radius:3px}.comment-content p{line-height:22px;padding:10px 10px 12px;color:#666;word-break:break-all}.comment-content-author{color:#999}.comment-content-arrow{background:url(http://x.autoimg.cn/www/channnel/2014/images/artjt-bg.png);width:10px;height:11px;overflow:hidden;position:absolute;bottom:-11px;left:14px}.comment-popup,.pop-content{position:relative;cursor:pointer}.comment-content a:hover{text-decoration:none;background-color:#efefef}.comment-content a:hover .comment-content-author,.comment-content a:hover p{color:#3b5998}.comment-content a:hover .comment-content-arrow{background-position:-20px 0}.editorblog{margin-top:20px}.editor-change{float:right;margin-top:2px;height:12px;line-height:12px}.editor-change:hover i{background-position:-100px -80px}.editor-change:hover a{text-decoration:underline;color:red}.editor-change i{vertical-align:middle;margin-top:-2px;*margin-right:5px}.hot-article-wrap li{width:297px;border-bottom:1px dotted #d0d0d0;color:#999;padding-top:18px;padding-bottom:10px;overflow:hidden;_display:inline-block}.hot-intro{line-height:22px}.editor-wrap img,.hot-article-wrap img,.hot-comment-wrap .avatar{margin-right:10px;float:left}.hot-comment-wrap .avatar{margin-top:5px}.hot-article-wrap h2{margin-bottom:10px;font:700 16px/24px "Microsoft YaHei",arial,tahoma,sans-serif}.editor-wrap li,.hot-comment-wrap li{margin-top:15px;color:#999}.hot-article-rec{padding-top:10px}.hot-article-rec img{vertical-align:top}.hot-article-rec li{float:left;width:140px;margin:6px 10px 0 0;text-align:center}.hot-article-rec li p{margin:5px 0}.coo-media .media-abstract{font-size:14px;line-height:26px;padding-top:5px}.coo-media .media-abstract p{background:url(http://x.autoimg.cn/www/channnel/2014/images/icon-square.png) 0 12px no-repeat;padding-left:13px}.editor-wrap li{height:55px;width:154px;float:left}.comment-link{margin-left:8px}.comment-wrapper i,.view-wrapper i{vertical-align:sub;*vertical-align:middle}.comment-popup{display:block;margin-top:10px;margin-bottom:9px;border:1px solid #ccd3e4;background:#f9f9f9;padding:10px;-moz-border-radius:3px;border-radius:3px}.div-fouc-tx ul li,.div-fouc-tx ul li a,.pop-content,.tuiguang i,.tuiguang li,.tuiguang ul,.tuiguang-arrow{display:inline-block}.user-right{height:23px;padding-left:32px;font-size:14px}.comment-from{line-height:14px;padding-bottom:2px;color:#999;white-space:nowrap}.comment-num,.view-num{*margin-left:5px}.pop-content{color:#666;z-index:10}.btns,.btns i{position:absolute}.editorname{margin-top:1px}.editorname a{font:700 14px/14px "\5B8B\4F53",arial,tahoma,sans-serif}.grid-right .advbox{width:290px}.btns{width:74px;height:37px;right:0;top:45px}.btns i{top:50%;left:50%;margin-top:-8px;margin-left:-8px}.app-ad{margin:15px auto 20px}.tuiguang{margin-top:15px;font-size:14px;line-height:16px}.tuiguang i{position:relative;float:left;margin-right:10px;height:14px;line-height:14px;background:#D60000;color:#FFF;font-style:normal;font-size:12px;vertical-align:top;padding:1px}.tuiguang-arrow{width:0;height:0;float:left;line-height:0;margin-left:-10px;border-left:8px solid #D60000;border-top:7px solid #FFF;border-bottom:8px solid #FFF}.tuiguang ul{width:600px}.tuiguang li{width:200px;float:left}.tuiguang a{color:#666;font-weight:700}.news-item h1{font:28px/1.5 'Microsoft YaHei',arial,tahoma,sans-serif}.btn-small.btn-blue.icon16-search1{_background:url(http://x.autoimg.cn/as/images/ie6-search-icon.png) no-repeat}.gotop02{position:fixed;_position:absolute;left:50%;margin-left:505px}.article img,.hot-article-wrap img{width:120px;height:90px}.editor-wrap img{width:40px;height:52px}.m-nav-title{height:28px;line-height:28px;border:1px solid #ccd3e4;position:relative;padding:0 0 0 10px;clear:both;font-weight:700;color:#333;font-size:14px;margin:25px 0 -5px}.m-nav-title-border{height:27px;line-height:27px;border:1px solid #ccd3e4;border-top:solid 2px #3b5998}.m-nav-title h3{padding:0 15px 0 0;float:left;color:#333}.m-nav-title h3 a:link,.m-nav-title h3 a:visited{color:#333}.m-nav-title h3 a:hover{text-decoration:none;color:#d60000}.m-nav-title h3.h3cur a:link,.m-nav-title h3.h3cur a:visited{color:#3b5998;font-weight:700}.m-nav-title .div-fouc{float:left;width:582px}.m-nav-title .div-fouc-bt{width:16px}.m-nav-title .div-fouc-bt-left{float:left;margin:3px 15px 0 0;*margin:5px 15px 0 0}.m-nav-title .div-fouc-bt-right{float:right;margin:3px 0 0 10px;*margin:5px 0 0 10px}.m-nav-title .div-fouc-tx{width:525px;float:left;overflow:hidden;height:27px;line-height:27px;position:relative}.div-fouc-tx ul{width:525px;height:27px;position:absolute;opacity:0;filter:0}.div-fouc-tx ul.fouc-current{z-index:10;opacity:10}.div-fouc-tx ul li{float:left;height:27px;padding:0}.div-fouc-tx ul li a{padding:0 9px;width:auto;float:left;font-weight:400}.div-fouc-tx ul li a:link,.div-fouc-tx ul li a:visited{color:#333}.div-fouc-tx ul li a:hover{color:#d60000;text-decoration:none}.div-fouc-tx ul li.current{background-color:#fff;text-decoration:none}.div-fouc-tx ul li.current a:link,.div-fouc-tx ul li.current a:visited{color:#3b5998;font-weight:700}.flos{margin:50px auto;text-align:center}.aname{font-size:0;line-height:0}.wide-body .content,.wide-body .content .subnav .nav-typebar{width:1000px}.wide-body .content .row .grid-left{padding-left:19px}.wide-body .content .row .grid-right{width:300px}.wide-body .content .row .grid-right .hot-article-rec ul{width:302px}.wide-body .content .row .grid-right .hot-article-rec li{width:136px;margin:6px 15px 0 0}.wide-body .content .row .grid-right .hot-article-rec img{width:136px;height:78px}.wide-body .content .row .grid-right .hot-article-wrap li{width:300px}.wide-body .content .row .grid-right .editor-wrap li{width:150px}.wide-body .content .row .grid-right .advbox{width:300px}.wide-body .mini-main{width:1000px}.wide-body .header-main{width:1000px}.wide-body .topbar-header-main{width:1000px}.wide-body .footer_auto{width:1000px}
    </style>
    <meta name="apple-itunes-app" content="app-id=415842508">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit" />
<script src="//x.autoimg.cn/bi/mda/ahas_head.min.js?v=20170621"></script>
<style type="text/css">.mini-left,.mini-left li,.mini-logo,.topbar-tip{float:left}.find-club a,.mini-logo img{vertical-align:top}.citypop-ct ul li a,.citypop-scity dl,.citypop-scity dl dd,.topbar-clearfix{zoom:1}.citypop-ct ul,.pop_forum ol,.pop_login ul{list-style:none}.topbar{position:relative;z-index:10000;_zoom:1}.topbar-helper{z-index:999}.citypop-close i,.citypop-ct .ntextdicon,.citypop-ct .zdicon,.citypop-search,.navcar .icon-newcar,.topbar-icon{background:url(//x.autoimg.cn/www/common/images/topbar-bg_20150728.png) no-repeat}.moreli-title-app,.moreli-title-notice{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAMCAMAAACUVSdlAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjQ5NzQ3MUEwMDMxOTExRTRCNjU2OTE4QzQ2NEQ5NEQ5IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjQ5NzQ3MUExMDMxOTExRTRCNjU2OTE4QzQ2NEQ5NEQ5Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NDk3NDcxOUUwMzE5MTFFNEI2NTY5MThDNDY0RDk0RDkiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NDk3NDcxOUYwMzE5MTFFNEI2NTY5MThDNDY0RDk0RDkiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5hF5cPAAAABlBMVEXS0tIAAACF+VnAAAAADklEQVR42mJgwA4AAgwAABgAAWQOeGIAAAAASUVORK5CYII=) no-repeat;_background:url(//x.autoimg.cn/www/common/images/split_bg.png) no-repeat}.citypop,.topbar-dropdown,.topbar-tip{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAbSURBVHjaYjQ2NpZiIAIwMRAJRhVSRyFAgAEALsEAx5m+/ZYAAAAASUVORK5CYII=);_background:url(//x.autoimg.cn/as/images/shadow_bg.png?v=20140322)}.topbar-clearfix:after{visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0}.topbar-icon,.topbar-tip .topbar-tip-arrow{display:inline-block;overflow:hidden}.topbar-icon16{width:16px;height:16px}.topbar-icon12{width:12px;height:12px}.topbar-icon10{width:10px;height:10px}.topbar-icon10-sjb{background-position:0 -205px}.topbar-icon12-array1{background-position:-40px -165px}.topbar-icon16-club{background-position:-20px -165px}.topbar-icon16-building{background-position:-60px -405px}.topbar-icon-fm{width:18px;height:16px;background-position:0 -434px}.topbar-icon-close{width:12px;height:12px;background-position:-22px -367px}.topbar-tip{min-width:50px;max-width:250px;position:absolute;z-index:100;padding:2px;font-size:12px}.topbar-tip .topbar-tip-content{position:relative;z-index:1;border:1px solid #ccd3e4;background-color:#FFF;padding:5px;line-height:18px;font-size:12px}.topbar-tip .topbar-tip-arrow{position:absolute;z-index:2;background:url(//x.autoimg.cn/as/images/layer_arrow24.png?v=20141215) no-repeat;_background:url(//x.autoimg.cn/as/images/layer_arrow8.png?v=20141215) no-repeat}.citi-active,.moreli-active,.moreli-fm{z-index:800}.topbar-tip .topbar-tip-bottom{width:15px;height:11px;top:-8px;left:43%;background-position:0 -26px}.topbar-tip .topbar-tip-left{width:11px;height:15px;top:30%;right:-8px;background-position:-30px -29px}.topbar-dropdown{width:80px;position:absolute;display:none;padding:2px;font-size:12px}.topbar-dropdown dl{border:1px solid #ccd3e3;background-color:#fff}.topbar-dropdown dd a{display:block;text-align:left;height:27px;line-height:27px;color:#666;text-decoration:none;padding:0 6px}.topbar-dropdown dd a:hover{background-color:#f1f5f8;color:#3b589a}.minitop{background-color:#333;color:#999}.mini-main{margin:0 auto;width:1000px;height:30px;line-height:30px}.mini-main a:hover{text-decoration:underline}.mini-main a.orangelink:hover,.mini-main a.orangelink:link,.mini-main a.orangelink:visited{color:#f60}.mini-main a.greylink:link,.mini-main a.greylink:visited{color:#999}.mini-main a.greylink:hover{color:#f60}.mini-main a.whitelink:link,.mini-main a.whitelink:visited{color:#fff}.mini-main a.whitelink:hover{color:#f60}.mini-main li.vlli{padding:0 5px}.mini-left ul{padding-left:184px}.mini-left li{position:relative}.mini-left .topbar-icon16-building{float:left;margin:7px 5px 0 0}.mini-right{float:right}.mini-right li{float:left;position:relative;z-index:800}.mini-right li.frs-login{padding-right:14px}.mini-right .frs-login a{padding:0 2px}.mini-right .frs-login a:link,.mini-right .frs-login a:visited{color:#fff}.mini-right .frs-login a.minitop-uname:hover,.mini-right .frs-login a.minitop-uname:link,.mini-right .frs-login a.minitop-uname:visited,.mini-right .frs-login a:hover{color:#f60}.mini-right .frs-login a.minitop-logoff:link,.mini-right .frs-login a.minitop-logoff:visited{color:#999}.mini-right .frs-login a.minitop-jifen-link:hover,.mini-right .frs-login a.minitop-jifen-link:link,.mini-right .frs-login a.minitop-jifen-link:visited,.mini-right .frs-login a.minitop-logoff:hover{color:#f60}.mini-right li.frs-zhaopin{padding:0 14px}.moreli-title{float:left;height:30px;*vertical-align:middle}.moreli-title a{display:block;_display:inline-block;height:30px;padding:0 14px;cursor:pointer}.moreli-title a:hover,.moreli-title a:link,.moreli-title a:visited{color:#999}.moreli-title a:hover{text-decoration:none}.moreli-title i,.moreli-title span{float:left;cursor:pointer}.moreli-title .topbar-icon10-sjb{position:relative;margin-left:5px;top:10px}.moreli-title .topbar-icon16{margin:8px 5px 0 0}.moreli-title .topbar-icon12{margin:10px 7px 0 0}.moreli-title .topbar-icon-fm{margin:7px 5px 0 0}.moreli-title-notice{background-position:left center}.moreli-title-notice span.info{display:inline-block;height:12px;padding:2px 3px;text-align:center;line-height:12px;background-color:#f60;border-radius:2px;color:#fff;margin:7px 1px 0 5px;font-weight:700}.moreli-title-club a{background-color:#f60}.moreli-title-club span{color:#fff}.moreli-title-club .topbar-icon10-sjb{background-position:-20px -205px}.moreli-title-app{background-position:left center}.moreli-active .active-bg{background-color:#f9f9f9}.moreli-active .moreli-title span{color:#666}.moreli-active .moreli-title-notice span.info{color:#fff}.moreli-active .moreli-title .topbar-icon12-array1{background-position:-60px -165px}.moreli-active .moreli-title .topbar-icon16-club{background-position:0 -165px}.moreli-active .moreli-title .topbar-icon10-sjb{background-position:-60px -205px}.moreli-title-fm a:hover .topbar-icon-fm{background-position:-22px -434px}.moreli-fm{position:relative}.moreli-fm .topbar-tip{width:178px;top:30px;left:0}.moreli-fm .topbar-tip .topbar-tip-content{padding:8px}.moreli-fm .topbar-tip .topbar-tip-bottom{left:25px}.citi-title a{padding:0 0 0 6px}.citi-title .topbar-icon10-sjb{margin-left:2px}.citi-title a:hover .topbar-icon10-sjb{background-position:-60px -205px}.find-club{padding:0 14px}.find-club a{display:inline-block;height:20px;line-height:20px;padding:0 20px;background-color:#f60;color:#fff;border-radius:2px;margin-top:5px;_margin-top:5px}.find-club a:hover,.find-club a:link{color:#fff;text-decoration:none}.topchadiv{position:absolute;right:-2px;top:31px;z-index:10;*background-image:url(about:blank);display:none}.topchadiv-dw02,.topchadiv-dw03{_right:-3px}.topchadiv-box{padding:0 2px 2px 0;clear:both;position:relative;top:-1px}.topchadiv-dw01 .topchadiv-box{width:110px}.topchadiv-dw02 .topchadiv-box{min-width:130px;overflow:visible;_width:130px}.topchadiv-dw03 .topchadiv-box{width:210px}.topchadiv-con{border:1px solid #ccd3e4;background-color:#fff;line-height:20px;text-align:left;padding:5px 0}.topchadiv-con a{display:block;height:27px;line-height:27px;white-space:nowrap;padding:0 15px;overflow:hidden}.topchadiv-con a:hover,.topchadiv-con a:link,.topchadiv-con a:visited{color:#666;text-decoration:none}.topchadiv-con a span{display:inline-block}.topchadiv-con a span.cn{color:#666;float:left}.topchadiv-con a span.ck{cursor:pointer;float:right}.topchadiv-con a:hover{color:#3b5998;background-color:#f9f9f9}.topchadiv-con .linedc{border-top:dotted 1px #cecece;height:1px;clear:both;font-size:0;margin:5px;line-height:0}.topchadiv-dw02 .topchadiv-con a{min-width:120px;overflow:visible}.topchadiv-dw03 .topchadiv-con a{padding:0 10px}.topchadiv-dw03 .topchadiv-con a:hover,.topchadiv-dw03 .topchadiv-con a:link,.topchadiv-dw03 .topchadiv-con a:visited{color:#3b5998}.topbar-header{position:relative;height:85px;margin-bottom:10px;background-color:#efefef}.topbar-header-blue{width:100%;height:35px;background-color:#3b5998;position:absolute;top:0;left:0;overflow:hidden}.topbar-header-main{width:1000px;height:85px;margin:0 auto;position:relative;z-index:100}.topbar-header .logo{width:170px;height:90px;float:left;background-color:#fff;position:relative;top:-5px;margin-bottom:-5px}.topbar-header .logo-shadow1{width:0;height:0;overflow:hidden;border:6px solid #333;border-left-color:#999;border-right:0;position:absolute;top:-5px;left:170px}.topbar-header .logo-shadow2{display:inline-block;width:6px;height:7px;overflow:hidden;background-color:#3b5998;position:absolute;top:0;left:170px}.topbar-header .nav{width:820px;height:87px;float:right;position:relative;top:-2px;margin-bottom:-2px;z-index:10}.topbar-header .navlink{width:820px}.topbar-header .navlink ul{height:37px;}.topbar-header .navlink li{float:left;position:relative}.topbar-header .navlink a.navlink-item{display:inline-block;height:37px;line-height:40px;float:left;overflow:hidden;text-align:center;font-size:14px;font-weight:700}.topbar-header .navlink a.navlink-item:link,.topbar-header .navlink li a.navlink-item:visited{color:#fff;text-decoration:none}.topbar-header .navlink a.navlink-item:hover,.topbar-header .navlink li a.navlink-item-current{color:#fff;text-decoration:none;background-color:#57b}.topbar-header .navlink a.navlink-item .topbar-icon10-sjb{float:right;position:relative;top:15px;right:1px;width:7px;background-position:-21px -205px}.topbar-header .navlink a.navlink-item sup{font-size:12px;line-height:0;position:relative;vertical-align:baseline;top:-.5em;font-weight:400}.topbar-header .navlink a.nw-2{width:43px}.topbar-header .navlink a.nw-25{width:51px}.topbar-header .navlink a.nw-2arrow{width:49px;padding-right:6px}.topbar-header .navlink a.nw-3{width:62px}.topbar-header .navlink a.nw-4{width:78px}.topbar-header .navlink .topbar-dropdown{width:80px;left:-2px;top:35px;background-image:none;font-family:"\5B8B\4F53",simsun,arial,tahoma,sans-serif}.topbar-header .navcar ul{width:814px;height:50px;padding-left:6px}.topbar-header .navcar li{width:72px;height:50px;line-height:14px;text-align:center;float:left}.topbar-header .navcar li a{display:block;height:25px;line-height:22px;padding-top:25px}.topbar-header .navcar li.navcar07{position:relative}.topbar-header .navcar li.navcar07 .topbar-icon10-sjb{float:right;position:relative;top:6px;right:21px}.topbar-header .navcar li a:hover .topbar-icon10-sjb{background-position:-60px -205px}.topbar-header .navcar li.navcar07 div.topbar-dropdown{width:78px;left:-2px;top:48px}.topbar-header .navcar li.navcar07 div.topbar-dropdown a{background:0 0;height:27px;line-height:27px;padding:0 6px}.topbar-header .navcar li.navcar07 div.topbar-dropdown a:hover{background-color:#f1f5f8;color:#3b589a}.topbar-header .navcar li.navcar01,.topbar-header .navcar li.navcar02,.topbar-header .navcar li.navcar11{width:58px}.topbar-header .navcar li a:link,.topbar-header .navcar li a:visited{color:#666}.topbar-header .navcar li a:hover{color:#d60000;text-decoration:none;background-color:#fff}.topbar-header .navcar li .icon-newcar{position:absolute;right:0;top:-3px;width:21px;height:11px;background-position:-170px -358px}.topbar-header .navcar li.navcar06{width:80px}.topbar-header .navcar li.navcar12{width:56px;position:relative}.topbar-header .navcar li a{background:url(//x.autoimg.cn/www/common/images/topbar_car.png) no-repeat;background-image:-webkit-image-set(url(//x.autoimg.cn/www/common/images/topbar_car.png) 1x,url(//x.autoimg.cn/www/common/images/topbar_car@2x.png) 2x)}.topbar-header .navcar li.navcar01 a{background-position:-11px 0}.topbar-header .navcar li.navcar02 a{background-position:-91px 0}.topbar-header .navcar li.navcar03 a{background-position:-164px 0}.topbar-header .navcar li.navcar04 a{background-position:-244px 0}.topbar-header .navcar li.navcar05 a{background-position:-4px -60px}.topbar-header .navcar li.navcar06 a{background-position:-80px -60px}.topbar-header .navcar li.navcar07 a{background-position:-164px -58px}.topbar-header .navcar li.navcar08 a{background-position:-244px -58px}.topbar-header .navcar li.navcar09 a{background-position:-4px -120px}.topbar-header .navcar li.navcar10 a{background-position:-84px -118px}.topbar-header .navcar li.navcar11 a{background-position:-171px -120px}.topbar-header .navcar li.navcar12 a{background-position:-251px -120px}.citypop{position:absolute;top:28px;left:-12px;padding:2px;z-index:1000;font-size:12px;line-height:26px;display:none}.citypop a:link,.citypop a:visited{text-decoration:none}.citypop a:hover{color:#d60000}.citypop .citypop-content{width:485px;position:relative;z-index:1;border:1px solid #ccd3e4;background-color:#FFF}.citypop .citypop-content .citypop-close{display:inline-block;width:29px;height:29px;overflow:hidden;position:absolute;right:0;_right:-1px;top:0;background-color:#fafbfc;border-left:solid 1px #cfd5e5}.citypop .citypop-content .citypop-content-top{height:29px;line-height:29px;padding-left:8px;position:relative;background-color:#fcfcfc;border-bottom:solid 1px #ccd3e4}.citypop .citypop-content .citypop-close i{display:inline-block;width:16px;height:16px;background-position:-19px -365px;margin:6px;cursor:pointer;line-height:16px}.citypop .citypop-content a.citypop-close:hover{background-color:#3b5998}.citypop .citypop-content a.citypop-close:hover i{background-position:1px -365px}.citypop .citypop-arrow{overflow:hidden;position:absolute;z-index:2;font-family:"\5b8b\4f53"}.citypop-nb a,.citypop-scity dl dt .nu{font-family:Arial,Helvetica,sans-serif}.citypop .citypop-arrow .citypop-arrow-shadow{filter:alpha(opacity=10);-moz-opacity:.1;opacity:.1}.citypop .citypop-arrow .citypop-arrow-background,.citypop .citypop-arrow .citypop-arrow-border,.citypop .citypop-arrow .citypop-arrow-shadow{overflow:hidden;position:absolute;font-size:12pt}.citypop-bottom .citypop-arrow{width:16px;height:14px;top:-11px;left:23px}.citypop-bottom .citypop-arrow .citypop-arrow-background,.citypop-bottom .citypop-arrow .citypop-arrow-border,.citypop-bottom .citypop-arrow .citypop-arrow-shadow{height:11px}.citypop-bottom .citypop-arrow .citypop-arrow-border{top:3px;color:#d0d0e8}.citypop-bottom .citypop-arrow .citypop-arrow-background{top:4px;color:#f8fcff}.citypop-search{width:140px;height:22px;float:left;margin-top:3px;background-position:-36px -182px;border:1px solid #ccd3e4;background-color:#fff;position:relative}.citypop-search input{outline:0;height:22px;line-height:22px;width:118px;position:absolute;left:22px;top:0;border:none;background-color:#fff;color:#b8bbc1;padding:0}.citypop-search input.focus{width:132px;padding:0 4px;left:0;color:#000}.citypop-hotcity{float:left;padding-left:5px}.citypop-hotcity a{margin-left:10px;display:inline-block;float:left}.citypop-nb{height:28px;padding:8px 6px;border-bottom:dotted 1px #cecfd3}.citypop-nb a{display:inline-block;width:19px;height:19px;line-height:19px;border-radius:2px;margin:4px;font-size:14px;text-align:center;border:1px solid #cbddeb;background-color:#f0f9fe;float:left}.citypop-nb a.current:hover,.citypop-nb a.current:link,.citypop-nb a.current:visited,.citypop-nb a:hover{background-color:#3b5997;border:1px solid #17469e;color:#fff}.citypop-scity{height:255px;overflow-y:scroll;overflow-x:hidden}.citypop-scity dl{border-top:dotted 1px #cecfd3;margin:0;overflow:hidden;padding:8px 0}.citypop-scity .dlbg{background-color:#f9f9f9}.citypop-scity dl.dlbg-top{border-top:none}.citypop-scity dl dd,.citypop-scity dl dt{float:left;margin:0}.citypop-scity dl dt{width:78px;color:#333;text-align:right;font-weight:700;padding-top:2px}.citypop-scity dl dt .nu,.citypop-scity dl dt .tx{height:20px;line-height:20px;display:inline-block;float:right;padding:0}.citypop-scity dl dt .nu{float:left;font-size:18px;color:#d0d0d0;font-weight:100;padding-left:10px}.citypop-scity dl dd{width:390px}.citypop-scity dl dd a:active,.citypop-scity dl dd a:link,.citypop-scity dl dd a:visited{height:20px;line-height:20px;display:block;float:left;padding:0 5px;margin:2px;white-space:nowrap}.citypop-scity dl dd a:hover{height:20px;line-height:20px;color:#fff;background-color:#ff9410;_color:#D60000;_background-color:none}.citypop-scity a.current:hover,.citypop-scity a.current:link,.citypop-scity a.current:visited{background-color:#ff600f;color:#fff}.citypop-ct ul li a:after,.citypop-scity dl dd:after,.citypop-scity dl:after{visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0;line-height:0}.citypop-ct{width:195px;position:absolute;left:-1px;top:24px;border:1px solid #ccd3e4;background-color:#fff}.citypop-ct .ntextdicon,.citypop-ct .zdicon{height:14px;line-height:14px;padding:2px 0 2px 15px;color:#b8bbc1;margin-left:5px}.citypop-ct ul li,.citypop-ct ul li a{height:26px;line-height:26px;overflow:hidden}.citypop-ct .zdicon{background-position:-279px -161px}.citypop-ct .ntextdicon{background-position:-280px -182px}.citypop-ct ul{padding:0;margin:0}.citypop-ct ul li{float:none;clear:both;border-top:dotted 1px #ccd3e4}.citypop-ct ul li a{display:block;padding:0 12px}.citypop-ct ul li a:hover,.citypop-ct ul li.selected{background-color:#f9f9f9}.citypop-ct ul li span{float:left;display:inline-block}.citypop-ct ul li b{display:inline-block;font-weight:100;color:#b8bbc1;float:right}.pop_forum .ico_close,.pop_forum .ico_del,.pop_forum .pf_search,.pop_forum .pf_search .glass,.pop_forum .pf_search_fous{background:url(//x.autoimg.cn/club/v1Content/images_1/pub_pop_bg.png?11) no-repeat}.pop_forum blockquote,.pop_forum dd,.pop_forum div,.pop_forum dl,.pop_forum dt,.pop_forum fieldset,.pop_forum form,.pop_forum h1,.pop_forum h2,.pop_forum h3,.pop_forum h4,.pop_forum h5,.pop_forum h6,.pop_forum input,.pop_forum li,.pop_forum ol,.pop_forum pre,.pop_forum textarea,.pop_forum ul{margin:0;padding:0}.pop_forum li{list-style-type:none}.pop_forum img{vertical-align:top;border:0}.pop_forum h1,.pop_forum h2,.pop_forum h3,.pop_forum h4,.pop_forum h5,.pop_forum h6,.pop_forum table,.pop_forum td,.pop_forum th,.pop_forum tr{font-size:12px}.pop_forum table{margin:0 auto}.pop_forum{width:744px;height:420px;background:#fff;border-top:solid #005ab0 1px;font-family:\5B8B\4F53,Arial Narrow,arial,serif;font-size:12px;line-height:normal}.pop_forum a:link,.pop_forum a:visited{color:#3b5998;text-decoration:none}.pop_forum a:hover{text-decoration:underline}.pop_forum .pf_inner{border:6px solid #3b5998}.pop_forum .pf_tt{position:relative;height:37px;background:#f2f5f8;border-bottom:solid #ccd3e4 1px}.pop_forum .pf_tt .ico_close{position:absolute;top:6px;right:4px;width:30px;height:28px;text-indent:-999px;overflow:hidden;background-position:0 -31px}.pop_forum .pf_tab{position:absolute;top:12px;left:17px;font-size:12px}.pop_forum .pf_tab a:link,.pop_forum .pf_tab a:visited{display:block;float:left;width:83px;height:18px;padding:6px 0 0;margin:0 8px 0 0;background:#fff;border:solid #ccd3e4;border-width:1px 1px 0;font-weight:400;color:#3e3e3e;text-align:center}.pop_forum .pf_tab a:hover{text-decoration:none}.pop_forum .pf_tab a.cur:link,.pop_forum .pf_tab a.cur:visited{height:19px;padding:5px 0 0;font-weight:700;color:#3b5998;border:solid;border-color:#fc7400 #adc9df;border-width:2px 1px 0}.pop_forum .pf_bradet_tt h3{padding-left:18px;font-size:12px;color:#3b5998;line-height:37px}.pop_forum .pf_cont{height:370px;overflow:auto;position:relative}.pop_forum .pf_search,.pop_forum .pf_search_fous{position:relative;width:394px;height:28px;margin:21px auto 36px;border:1px solid #afc5e0;background-position:0 -87px}.pop_forum .pf_search_fous{border:1px solid #7692cd;width:394px}.pop_forum .pf_search .glass{width:16px;height:16px;display:inline-block;background-position:-83px 0;position:absolute;margin:7px 0 0 11px}.pop_forum .pf_search_fous .glasss{display:none}.pop_forum .pf_search .s_tx,.pop_forum .pf_search_fous .s_tx{width:275px;height:20px;padding:0 7px 0 33px;margin:5px 0 0;background:#fff;border:0;outline:0;box-shadow:none;font-size:12px;color:#999;line-height:20px}.pop_forum .pf_search_fous .s_tx{width:301px;padding:0 7px;color:#000}.pop_forum .pf_search .s_btn,.pop_forum .pf_search_fous .s_btn{background-color:#3b5998;position:absolute;right:-1px;top:-1px;width:80px;height:30px;line-height:30px;padding:0;text-shadow:none;overflow:hidden;font-weight:700;text-align:center;z-index:1}.pop_forum .pf_search .s_btn:link,.pop_forum .pf_search .s_btn:visited,.pop_forum .pf_search_fous .s_btn:link,.pop_forum .pf_search_fous .s_btn:visited{color:#fff;text-decoration:none}.pop_forum .pf_search .s_btn:hover,.pop_forum .pf_search_fous .s_btn:hover{padding:0}.pop_forum .pf_search .keywordsbox,.pop_forum .pf_search_fous .keywordsbox{z-index:1000;position:absolute;top:28px;left:-1px;background-color:#fff;font-size:12px;line-height:22px}.pop_forum .pf_search .keywordsbox ul,.pop_forum .pf_search_fous .keywordsbox ul{width:315px;padding:0;border:1px solid #7692cd;line-height:22px;overflow:hidden}.pop_forum .pf_search .keywordsbox ul li,.pop_forum .pf_search_fous .keywordsbox ul li{width:100%;height:22px;padding:0;line-height:22px;overflow:hidden}.pop_forum .pf_search .keywordsbox ul li a:link,.pop_forum .pf_search .keywordsbox ul li a:visited,.pop_forum .pf_search_fous .keywordsbox ul li a:link,.pop_forum .pf_search_fous .keywordsbox ul li a:visited{display:block;float:none;padding:0 8px;height:22px;line-height:22px;color:#000;text-decoration:none;text-shadow:none;overflow:hidden}.pop_forum .pf_search .keywordsbox ul li a:hover,.pop_forum .pf_search_fous .keywordsbox ul li a:hover{background-color:#f0f9fe;border:none;color:#000}.pop_forum .pf_list{padding:0 0 0 20px}.pop_forum .pf_list h3{margin:28px 0 0;font-weight:700;color:#3e3a39}.pop_forum .pf_default h3{margin:20px 0 0;text-align:left;font-size:12px;font-weight:700}.pop_forum .pf_default h3 span{display:inline-block;height:20px;line-height:20px;padding:0 5px;color:#fff;font-weight:700;background:#fc7400}.pop_forum .pf_list ul{width:690px;padding:12px 0 8px 2px;overflow:hidden}.pop_forum .pf_list li{float:left;width:132px;padding:0 6px 12px 0}.pop_forum .pf_list li a:link,.pop_forum .pf_list li a:visited{float:left;display:block;height:14px;overflow:hidden}.pop_forum .pf_collect .ico_del{display:block;float:left;width:11px;height:11px;margin:0 0 0 1px;overflow:hidden;cursor:pointer;background-position:-30px -31px}.pop_forum .pf_brand{padding:0 0 0 20px}.pop_forum .pf_brand h3{height:25px;margin:19px 0 0;overflow:hidden;font-size:12px}.pop_forum .pf_brand h3 a:link,.pop_forum .pf_brand h3 a:visited{display:block;float:left;width:86px;height:23px;margin-right:7px;background:#e4e9f1;border:1px solid #ccd3e4;font-family:Arial;font-weight:700;line-height:24px;text-align:center;overflow:hidden;letter-spacing:2px;_letter-spacing:-2px}.pop_forum .pf_brand h3 a:hover{text-decoration:none}.pop_forum .pf_brand h3 a.cur:link,.pop_forum .pf_brand h3 a.cur:visited{width:88px;height:25px;background:#526ca4;border:none;color:#fff}.pop_forum .pf_brand h3 i{font-style:normal;_font-weight:400}.pop_forum .pf_brand h4{margin:12px 0 0 4px;font-family:Arial;font-weight:700;color:#e75e15}.pop_forum .pf_brand ul{width:690px;padding:8px 0 0 2px;overflow:hidden}.pop_forum .pf_brand li{float:left;width:138px;padding:0 0 8px;overflow:hidden}.pop_forum .pf_brand li a:link,.pop_forum .pf_brand li a:visited{float:left;display:block;height:14px;overflow:hidden}.pop_forum .pf_hr,.pop_forum .pf_hr02{display:block;width:692px;height:0;border-top:dotted #ccc 1px;overflow:hidden}.pop_forum .pf_hr02{border-top:solid 1px #ccd3e4}.icon-new-01{display:inline-block;vertical-align:top;width:26px;height:12px;margin:6px 0 0 3px;background:url(//s.autoimg.cn/www/common/images/icon-new.png?v=2.1) no-repeat -20px -35px}.icon-new-02{display:inline-block;vertical-align:top;width:26px;height:14px;position:absolute;right:-3px;top:0;background:url(//s.autoimg.cn/www/common/images/icon-new.png?v=2.1) no-repeat -50px -35px}.topbar-header .navlink{ width:828px; }.topbar-header .navlink ul{ height:37px;}</style>  
    <base target="_blank" href="http://www.autohome.com.cn/" />
</head>
<body class="wide-body">
    <div id="auto-header" class="topbar">
    <!-- minitop begin -->
    <div class="minitop">
        <div class="mini-main">
            <div class="mini-left">
                <ul>
                    <li id="auto-header-fenzhan"><a target="_blank" href="//www.autohome.com.cn/beijing/cheshi/" class="orangelink"><i class="topbar-icon topbar-icon16 topbar-icon16-building"></i>进入北京车市</a></li>
                    <li class="vlli">|</li>
                    <li><a target="_blank" href="//www.autohome.com.cn/AreaList.html" class="greylink">查看其它地方车市</a></li>
                </ul>
            </div>
            <div class="mini-right">
                <ul>
                    <li id="auto-header-login" class="frs-login" style="display:none">
                        <div id="auto-header-login-text">
                        </div>

                    </li>
                    <li id="auto-header-info" style="display:none">
                        <div class="moreli-title moreli-title-notice">
                            <a href="javascript:void(0);" class="active-bg" target="_self">
                                <span>消息</span><span id="auto-header-info-allcount" class="info" style="display: none"></span><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>
                            </a>
                        </div>
                        <div id="auto-header-info-list" class="topchadiv topchadiv-dw03" style="display: none;">
                            <div class="topchadiv-box">
                                <div id="auto-header-info-listdata" class="topchadiv-con">
                                </div>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="find-club">
                            <a id="auto-header-find-club" target="_self" href="javascript:void(0);">找论坛</a>
                        </div>
                    </li>
                    <li id="auto-header-app">
                        <div class="moreli-title">
                            <a target="_self" class="active-bg" href="javascript:void(0);">
                                <span>更多应用</span>
                                <i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>
                            </a>
                        </div>
                        <div id="auto-header-app-list" class="topchadiv topchadiv-dw01" style="display:none">
                            <div class="topchadiv-box">
                                <div class="topchadiv-con">
                                    <a target="_blank" href="//app.autohome.com.cn/appn/">移动App</a>
                                    <a target="_blank" href="//app.autohome.com.cn/appn/m/">触屏版</a>
                                    <a target="_blank" href="//j.autohome.com.cn/quankuan_calculation.html">购车计算器</a>
                                    <a target="_blank" href="//www.autohome.com.cn/Violation/">违章查询</a>
                                    <a target="_blank" href="//car.autohome.com.cn/zhaoche/jiage/">按价格找车</a>
                                    <a target="_blank" href="//car.autohome.com.cn/zhaoche/pinpai/">按品牌找车</a>
                                    <a target="_blank" href="//www.autohome.com.cn/chezhan/#pvareaid=103405">车展</a>
                                    <div class="linedc"></div>
                                    <a target="_blank" href="//ics.autohome.com.cn/#pvareaid=104317">i车商</a>
                                    <a target="_blank" href="//www.che168.com/">二手车之家</a>
                                    <a target="_blank" href="//mall.autohome.com.cn/subject/2017/6/recruitment/#pvareaid=2023627">车商城入驻</a>
                                    <!--<a target="_blank" href="//www.pcpop.com">泡泡网</a>
                                    <a target="_blank" href="//www.it168.com">IT168</a>-->
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <!-- minitop end -->
    <!-- 双十一车商城推广位 begin -->
    <div class="ad-top-1111" style="display:none;" id="ad-top-1111">
        <div class="monkey">
            <div>
                <!-- 广告图图片路径写在 style 里 -->
                <a href="//mall.autohome.com.cn/carevent/?page=prea#pvareaid=2023272" id="header-ad-top-1111" target="_blank"></a>
            </div>
        </div>
    </div>
    <style type="text/css">
          .ad-top-1111{width:100%;margin:0 auto;}
          .ad-top-1111 a{display:block;width:100%;height:60px;margin:0 auto;}
          .topbar-header .logo-shadow1{border-top-color: transparent;}
    </style>
    <!-- 双十一车商城推广位 end -->
    <!-- club pop begin -->
    <div id="auto-header-clubmask" style="width: 100%; height: 100%; position: fixed; left: 0px; top: 0px; z-index: 1100; display: none; background-color: #000; opacity: 0.5; filter: alpha(opacity=50); -moz-opacity: 0.5; -khtml-opacity: 0.5;"></div>
    <div id="auto-header-clublayer" style="display:none; z-index: 1101; position: fixed; top:50%; left:50%; margin-top:-210px; margin-left:-377px;">
        <div class="pop_forum">
            <div class="pf_inner">
                <div class="pf_tt">
                    <h2 class="pf_tab">
                        <a id="auto-header-club-tab0" href="javascript:void(0);" target="_self" tabindex="0" class="cur">找论坛</a>
                        <a id="auto-header-club-tab1" href="javascript:void(0);" target="_self" tabindex="1">全部车系</a>
                        <a id="auto-header-club-tab2" href="javascript:void(0);" target="_self" tabindex="2">全部地区</a>
                        <a id="auto-header-club-tab3" href="javascript:void(0);" target="_self" tabindex="3">全部主题</a>
                        <a id="auto-header-club-tab4" href="javascript:void(0);" target="_self" tabindex="4">摩托车论坛</a>
                    </h2>
                    <a id="auto-header-clubclose" class="ico_close" href="javascript:void(0);" target="_self">关闭</a>
                </div>
                <div id="auto-header-clubhtml" class="pf_cont"></div>
            </div>
        </div>
    </div>
    <!-- club pop end -->
    <!-- header begin -->
    <div class="topbar-header">
        <div class="topbar-header-main">
            <div class="topbar-clearfix">
                <div class="logo"><a href="//www.autohome.com.cn/"><img width="170" height="90" alt="汽车之家" src="//x.autoimg.cn/www/common/images/logo_noslogan.png" srcset="//x.autoimg.cn/www/common/images/logo_noslogan.png 170w,//x.autoimg.cn/www/common/images/logo_noslogan_2x.png 340w" sizes="170px"></a></div>
                <div class="nav">
                    <div class="navlink">
                        <ul>
                            <li id="auto-header-news">
                                <a id="auto-header-channel2" class="navlink-item nw-2arrow" href="//www.autohome.com.cn/all/" target="_blank"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>文章</a>
                                <div id="auto-header-news-list" class="topbar-dropdown" style="display: none;">
                                    <dl>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/all/">查看全部</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/newbrand/">上市新车</a></dd>
                                        <dd><a target="_blank" href="//live.autohome.com.cn/#pvareaid=106367">直播</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/ah-100/">AH-100评价</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/23660/0/1/conjunction.html">长期测试</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/youji/">编辑游记</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/topics/#pvareaid=2023455">互动话题</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li><a id="auto-header-channel3" class="navlink-item nw-2" href="//www.autohome.com.cn/bestauto/">评测</a></li>
                            <li><a id="auto-header-channel19" class="navlink-item nw-3" href="//chejiahao.autohome.com.cn/#pvareaid=2023585">车家号</a></li>
                            <li id="auto-header-v">
                                <a id="auto-header-channel4" class="navlink-item nw-2arrow" href="//v.autohome.com.cn/#pvareaid=2029173"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>视频</a>
                                <div id="auto-header-v-list" class="topbar-dropdown" style="display: none;">
                                    <dl>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/#pvareaid=103409 ">查看全部</a></dd>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/u/19987472#pvareaid=106552">原创试车</a></dd>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/u/20380947#pvareaid=106554">用车小百科</a></dd>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/u/27493450#pvareaid=106548">微试车</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li><a id="auto-header-channel17" class="navlink-item nw-2" href="//live.autohome.com.cn#pvareaid=103435">直播</a></li>
                            <li><a id="auto-header-channel6" class="navlink-item nw-4" href="//car.autohome.com.cn/duibi/chexing/">车型对比</a></li>
                            <li><a id="auto-header-channel7" class="navlink-item nw-2" href="//car.autohome.com.cn/pic/index.html">图片</a></li>
                            <li><a id="auto-header-channel8" class="navlink-item nw-2" href="//car.autohome.com.cn/">报价</a></li>
                            <li><a id="auto-header-channel9" class="navlink-item nw-3" href="//mall.autohome.com.cn/">车商城</a></li>
                            <li><a id="auto-header-channel10" class="navlink-item nw-2" href="//buy.autohome.com.cn/">降价</a></li>
                            <li><a id="auto-header-channel11" class="navlink-item nw-3" href="//dealer.autohome.com.cn/">经销商</a></li>
                            <li><a id="auto-header-channel12" class="navlink-item nw-3" href="//www.che168.com/#pvareaid=2023133">二手车</a></li>
                            <li><a class="navlink-item nw-2" target="_blank" href="//j.autohome.com.cn/pcplatform/index.html?pt=_t&pvareaid=2020996" data-tjposition="">金融</a></li>
                            <li><a id="auto-header-channel14" class="navlink-item nw-2" href="//club.autohome.com.cn/">论坛</a></li>
                            <li><a id="auto-header-channel18" class="navlink-item nw-2" href="//club.autohome.com.cn/jingxuan/">精选</a></li>
                            <li><a id="auto-header-channel15" class="navlink-item nw-2" href="//k.autohome.com.cn/">口碑</a></li>
                        </ul>
                    </div>

                    <div class="navcar">
                        <ul>
                            <li class="navcar01"><a target="_blank" href="//www.autohome.com.cn/a00/">微型车</a></li>
                            <li class="navcar02"><a target="_blank" href="//www.autohome.com.cn/a0/">小型车</a></li>
                            <li class="navcar03"><a target="_blank" href="//www.autohome.com.cn/a/">紧凑型车</a></li>
                            <li class="navcar04"><a target="_blank" href="//www.autohome.com.cn/b/">中型车</a></li>
                            <li class="navcar05"><a target="_blank" href="//www.autohome.com.cn/c/">中大型车</a></li>
                            <li class="navcar06"><a target="_blank" href="//www.autohome.com.cn/d/">大型车</a></li>
                            <li class="navcar07" id="auto-header-suv">
                                <a target="_blank" href="//www.autohome.com.cn/suv/"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>SUV</a>
                                <div id="auto-header-suv-list" style="display: none;" class="topbar-dropdown">
                                    <dl>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suv/">全部SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suva0/">小型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suva/">紧凑型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suvb/">中型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suvc/">中大型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suvd/">大型SUV</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li class="navcar08"><a target="_blank" href="//www.autohome.com.cn/mpv/">MPV</a></li>
                            <li class="navcar09"><a target="_blank" href="//www.autohome.com.cn/s/">跑车</a></li>
                            <li class="navcar10"><a target="_blank" href="//www.autohome.com.cn/p/">皮卡</a></li>
                            <li class="navcar11"><a target="_blank" href="//www.autohome.com.cn/mb/">微面</a></li>
                            <li class="navcar12">
                                <a target="_blank" href="//diandong.autohome.com.cn#pvareaid=103686">电动车</a>

                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <i class="logo-shadow1"></i><i class="logo-shadow2"></i>
        </div>
        <div class="topbar-header-blue"></div>
    </div>
    <!-- header end -->
</div>

<script type="text/javascript">
    //sync-login.js
    !function(e){function n(e,n){var o,t,i=e+"=",u=m.cookie.split(";");for(o=0;o<u.length;o+=1){for(t=u[o];" "===t.charAt(0);)t=t.substring(1,t.length);if(0===t.indexOf(i))return decodeURIComponent(t.substring(i.length,t.length))}return"undefined"==typeof n?null:n}function o(e,n,o){var t=m.getElementsByTagName("body")[0],i=m.createElement("iframe");i.style.display="none",i.src=n,i.id=e,i.domain=o,t.appendChild(i)}function t(){var e,t=n("sessionuserid");null!=t&&0!==t.length||(e=n("autouserid"),null!=e&&e.length>0&&(m.domain.indexOf("autohome")>=0?o("tempIframe","//sso.autohome.com.cn/Home/CookieIFrame","autohome.com.cn"):o("tempIframe","//sso.che168.com/Home/CookieIFrame","che168.com")))}function i(){u&&clearTimeout(u),u=null,u=setTimeout(function(){t(),i()},432e5)}var m=e.document,u=null;t(),i()}(this);
    //auto-header.js
    !function (e) { function t(e, t) { var a, n, o = e + "=", i = document.cookie.split(";"); for (a = 0; a < i.length; a += 1) { for (n = i[a]; " " === n.charAt(0) ;) n = n.substring(1, n.length); if (0 === n.indexOf(o)) return decodeURIComponent(n.substring(o.length, n.length)) } return "undefined" == typeof t ? null : t } function a(e) { var t = document.createElement("script"); t.setAttribute("type", "text/javascript"), t.setAttribute("src", e.url), t.onload = t.onreadystatechange = function () { if (!this.readyState || "loaded" === this.readyState || "complete" === this.readyState) { "function" == typeof e.callBack && e.callBack(e.args), t.onload = t.onreadystatechange = null; try { t.parentNode && t.parentNode.removeChild(t) } catch (a) { } } }, document.getElementsByTagName("head")[0].appendChild(t) } function n(e) { this.isPageFocus = !0, this.Aleng = 0, this.init(e) } n.prototype = { $dom: function () { for (var e = [], t = 0; t < arguments.length; t++) { var a = arguments[t]; if ("string" == typeof a && (a = document.getElementById(a)), 1 === arguments.length) return a; e.push(a) } return e }, cookies: { read: function (e, t) { for (var a = e + "=", n = document.cookie.split(";"), o = 0; o < n.length; o++) { for (var i = n[o]; " " === i.charAt(0) ;) i = i.substring(1, i.length); if (0 === i.indexOf(a)) return decodeURIComponent(i.substring(a.length, i.length)) } return "undefined" == typeof t ? null : t }, set: function (e, t, a) { var n = e + "=" + encodeURIComponent(t); if (a) { if (a.expireHours) { var o = new Date; o.setTime(o.getTime() + 3600 * a.expireHours * 1e3), n += "; expires=" + o.toGMTString() } n += a.path ? "; path=" + a.path : "; path=/", a.domain && (n += "; domain=" + a.domain), a.secure && (n += "; true") } document.cookie = n }, del: function (e) { var t = new Date; t.setTime(t.getTime() - 1); var a = this.read(e); null != a && (document.cookie = e + "=" + a + ";expires=" + t.toGMTString()) } }, eventHandle: { add: function (e, t, a) { window.addEventListener ? e.addEventListener(t, a, !1) : e.attachEvent("on" + t, a) }, remove: function (e, t, a) { window.removeEventListener ? e.removeEventListener(t, a, !1) : e.detachEvent("on" + t, a) } }, jsLoad: function () { var e, t, a = [], n = arguments.length; if (1 == n) { var o = arguments[0] || {}; "object" == typeof o ? (e = o.url, t = o.fn, a = o.args) : e = o } else { e = arguments[0], t = arguments[1]; for (var i = 0; n - 2 > i; i++) a[i] = arguments[i + 2] } var r = document.createElement("script"); r.setAttribute("type", "text/javascript"), r.setAttribute("src", e), r.onload = r.onreadystatechange = function () { if (!r.readyState || "loaded" === r.readyState || "complete" === r.readyState) { "function" == typeof t && t.apply(this, a), r.onload = r.onreadystatechange = null; try { r.parentNode && r.parentNode.removeChild(r) } catch (e) { } } }, document.getElementsByTagName("head")[0].appendChild(r) }, domReady: function () { var e, t = document, a = [], n = "complete" === t.readyState, o = function () { var e = a.shift(); for (n = !0; e;) e(), e = a.shift() }; return n ? function (e) { e() } : (t.addEventListener ? t.addEventListener("DOMContentLoaded", e = function () { t.removeEventListener("DOMContentLoaded", e, !1), o() }, !1) : (t.attachEvent("onreadystatechange", e = function () { "complete" === t.readyState && (t.detachEvent("onreadystatechange", e), o()) }), t.documentElement.doScroll && self == top && !function i() { if (!n) { try { t.documentElement.doScroll("left") } catch (e) { return setTimeout(i, 50) } o() } }()), function (e) { n ? e() : a.push(e) }) }(), logoffFunctionArray: [], host: { www: "//www.autohome.com.cn/", club: "//club.autohome.com.cn/", clubService: "//club.service.autohome.com.cn/", user: "//i.autohome.com.cn", login: "//account.autohome.com.cn/?backurl=" + encodeURIComponent(location.href), register: "//account.autohome.com.cn/register?backurl=" + encodeURIComponent(location.href) }, user: { isLogin: !1, uid: null, un: null, up: null }, userArea: { cookieArea: null, cookieCityId: null, areaId: null, oldCityId: null, cityName: null, cityPinyin: null, provinceId: null, provinceName: null, provincePinyin: null, provinceSimple: null }, init: function (e) { this.initChannel(e), this.popControl("auto-header-info", "moreli-active", !0), this.popControl("auto-header-app", "moreli-active", !0), this.popControl("auto-header-suv", "", !0), this.popControl("auto-header-news", "", !0), this.popControl("auto-header-v", "", !0), this.getUserArea(), this.getUser(), this.showUserStatus(), this.showUserMsg(), this.trackRead() }, initChannel: function (e) { var t; e && (t = document.getElementById("auto-header-channel" + e), t && (t.className += " navlink-item-current")) }, popControl: function (e, t, a) { var n = this, o = function (e) { return this.li = document.getElementById(e), this.list = document.getElementById(e + "-list"), this.shown = !1, this.init() }; return o.prototype = { init: function () { var e, t = this; n.eventHandle.add(this.li, "mouseover", function () { clearTimeout(e), t.show() }), n.eventHandle.add(this.li, "mouseout", function () { e = setTimeout(function () { t.hide() }, 50) }) }, show: function () { this.shown = !0, this.list && (this.list.style.display = "block"), t && (this.li.className = t); var e = navigator.userAgent.indexOf("MSIE 6.0") > 0; if (a && e && 0 == this.li.getElementsByTagName("iframe").length) { var n = this.list.offsetWidth, o = this.list.offsetHeight, i = document.createElement("iframe"); i.setAttribute("scrolling", "no"), i.setAttribute("frameborder", 0), i.style.cssText = "zoom:1;position:absolute;top:0;left:0;filter:alpha(opacity=0);z-index:-1; width:" + n + "px;height:" + o + "px", this.list.appendChild(i) } }, hide: function () { this.shown = !1, this.list && (this.list.style.display = "none"), t && (this.li.className = "") } }, document.getElementById(e) ? new o(e) : null }, getUserArea: function (e) { var t; if (e) t = this.host.www + "Ashx/AjaxHeadArea.ashx?OperType=GetAreaInfo&VarName=areaData&CityId=" + (0 == e ? "110100" : e); else { var a = { cookieCityId: this.cookies.read("cookieCityId"), area: this.cookies.read("area") }; this.userArea.cookieCityId = a.cookieCityId ? parseInt(a.cookieCityId, 10) : 0, this.userArea.cookieArea = a.area ? parseInt(a.area) : 0, this.userArea.areaId = 0 == this.userArea.cookieCityId ? 100 * parseInt(this.userArea.cookieArea / 100) : this.userArea.cookieCityId, 0 == this.userArea.areaId && (this.userArea.areaId = 110100), t = this.host.www + "Ashx/AjaxHeadArea.ashx?OperType=GetAreaInfo&VarName=areaData&CityId=" + this.userArea.areaId } var n = this; return this.jsLoad(t, function () { "undefined" != typeof areaData && areaData.Status && (n.userArea.oldCityId = areaData.AreaInfo[0].DealerCityId, n.userArea.cityName = areaData.AreaInfo[0].CityName, n.userArea.cityPinyin = areaData.AreaInfo[0].Pinyin, n.userArea.provinceId = areaData.ProvinceInfo[0].ProvinceId, n.userArea.provinceName = areaData.ProvinceInfo[0].ProvinceName, n.userArea.provincePinyin = areaData.ProvinceInfo[0].Pinyin, n.userArea.provinceSimple = areaData.ProvinceInfo[0].ProvinceSample, n.getUserAreaCallback()) }), !1 }, getUserAreaCallback: function () { var e = document.getElementById("auto-header-fenzhan"), t = document.getElementById("auto-header-channel12"), a = '<a target="_blank" class="orangelink" href="' + this.host.www + this.userArea.cityPinyin + '/cheshi/"><i class="topbar-icon topbar-icon16 topbar-icon16-building"></i>\u8fdb\u5165' + this.userArea.cityName + "\u8f66\u5e02</a>"; e && (e.innerHTML = a), t && t.setAttribute("href", "//www.che168.com/" + this.userArea.cityPinyin + "/list/#pvareaid=100533") }, getUser: function () { var e, t = this.cookies.read("clubUserShow"); return null == t ? this.user.isLogin = !1 : (e = t.split("|"), this.user.isLogin = !0, this.user.un = e[3], this.user.uid = e[0], this.user.up = e[2]), !1 }, showUserStatus: function () { var e, t, a = this, n = this.$dom("auto-header-login"), o = this.$dom("auto-header-login-text"); t = this.user.isLogin ? '\u60a8\u597d\uff01 <a class="minitop-uname" href="' + this.host.user + '" target="_blank">' + this.user.un + '</a> <a id="auto-header-logoff" class="minitop-logoff" href="javascript:void(0);" target="_self">\u9000\u51fa</a>' : '\u60a8\u597d\uff01\u8bf7 <a href="' + this.host.login + '" target="_self">\u767b\u5f55</a> \u6216 <a href="' + this.host.register + '" target="_self">\u6ce8\u518c</a>', n.style.display = "", o.innerHTML = t, e = document.getElementById("auto-header-logoff"), e && a.eventHandle.add(e, "click", function () { a.logoff() }) }, showUserMsg: function () { var e = this, t = this.$dom("auto-header-info"); this.user.isLogin ? (t.style.display = "", this.eventHandle.add(window, "focus", function () { e.isPageFocus = !0 }), this.eventHandle.add(window, "blur", function () { e.isPageFocus = !1 })) : t.style.display = "none" }, jsonpGetUserMsg: function () { if (!this.isPageFocus) return !1; if (!this.user.isLogin) return !1; var e = "AuScrJsonpId", t = "//msg.autohome.com.cn/clubalert?uid=" + this.user.uid + "&callback=AjaxCallBackMessage&ALeng=" + this.Aleng, a = document.getElementById(e); a && a.parentNode.removeChild(a); var n = document.createElement("script"); n.setAttribute("id", e), n.setAttribute("src", t), document.getElementsByTagName("head")[0].appendChild(n), window.AjaxCallBackMessage = function (e) { var t, a = "", n = ""; e.NewReply > 0 ? a += '<a href="//i.autohome.com.cn/receivereply/#pvareaid=101298"><span class="cn">' + (e.NewReply > 99 ? "99+" : e.NewReply) + '\u6761\u65b0\u8bba\u575b\u56de\u590d</span><span class="ck">\u67e5\u770b\u8bba\u575b\u56de\u590d</span></a>' : n += '<a  href="//i.autohome.com.cn/receivereply/#pvareaid=101606">\u67e5\u770b\u8bba\u575b\u56de\u590d</a>', e.commentreply > 0 ? a += '<a href="//i.autohome.com.cn/inbox/#pvareaid=101482"><span class="cn">' + (e.commentreply > 99 ? "99+" : e.commentreply) + '\u6761\u65b0\u8bc4\u8bba\u56de\u590d</span><span class="ck">\u67e5\u770b\u8bc4\u8bba\u56de\u590d</span></a>' : n += '<a href="//i.autohome.com.cn/inbox/#pvareaid=101607">\u67e5\u770b\u8bc4\u8bba\u56de\u590d</a>', e.NewLetter > 0 ? a += '<a href="//i.autohome.com.cn/club/message/#pvareaid=101300"><span class="cn">' + (e.NewLetter > 99 ? "99+" : e.NewLetter) + '\u6761\u65b0\u79c1\u4fe1</span><span class="ck">\u67e5\u770b\u79c1\u4fe1</span></a>' : n += '<a href="//i.autohome.com.cn/club/message/#pvareaid=101609">\u67e5\u770b\u79c1\u4fe1</a>', e.NewNotice > 0 ? a += '<a href="//i.autohome.com.cn/club/notice/#pvareaid=101301"><span class="cn">' + (e.NewNotice > 99 ? "99+" : e.NewNotice) + '\u6761\u65b0\u901a\u77e5</span><span class="ck">\u67e5\u770b\u901a\u77e5</span></a>' : n += '<a href="//i.autohome.com.cn/club/notice/#pvareaid=101610">\u67e5\u770b\u901a\u77e5</a>', e.NewFollowers > 0 ? a += '<a href="//i.autohome.com.cn/club/follower/#pvareaid=101297"><span class="cn">' + (e.NewFollowers > 99 ? "99+" : e.NewFollowers) + '\u4e2a\u65b0\u7c89\u4e1d</span><span class="ck">\u67e5\u770b\u7c89\u4e1d</span></a>' : n += '<a href="//i.autohome.com.cn/club/follower/#pvareaid=101611">\u67e5\u770b\u7c89\u4e1d</a>', e.order && e.order > 0 ? a += '<a href="//i.autohome.com.cn/orderlist/#pvareaid=101548"><span class="cn">' + (e.order > 99 ? "99+" : e.order) + '\u6761\u65b0\u8ba2\u5355</span><span class="ck">\u67e5\u770b\u8ba2\u5355</span></a>' : n += '<a href="//i.autohome.com.cn/orderlist/#pvareaid=101612">\u67e5\u770b\u8ba2\u5355</a>', t = "" != a && "" != n ? a + '<div class="linedc"></div>' + n : "" == n ? a : n; var o = document.getElementById("auto-header-info-listdata"); o && (o.innerHTML = t); var i = e.NewReply + e.commentreply + e.NewLetter + e.NewNotice + e.NewFollowers + (e.order && null != e.order ? e.order : 0), r = document.getElementById("auto-header-info-allcount"); i > 99 ? (r.innerHTML = "99+", r.style.display = "") : i > 0 ? (r.innerHTML = i, r.style.display = "") : (r.innerHTML = "", r.style.display = "none") } }, trackRead: function () { var e = this; e.domReady(function () { }) }, logoff: function () { var e = this; this.jsLoad("//account.autohome.com.cn/login/logoutjson?backvar=autologinout&timestamp=" + Math.random(), function () { for (var t = 0, a = e.logoffFunctionArray.length; a > t; t++) if ("function" == typeof e.logoffFunctionArray[t]) try { e.logoffFunctionArray[t]() } catch (n) { } e.init(), e.jsLoad("//account.che168.com/login/logoutjson?backvar=cheloginout&timestamp=" + Math.random()) }) } }, e.readCookie = t, e.AutohomeJsLoad = a, e.AutoHeader = n }(this);
    //auto-header-club.js
    !function(e){function t(e,t){return new RegExp(" "+t+" ").test(" "+e.className+" ")}function n(e,n){t(e,n)||(e.className+=" "+n)}function a(e,n){var a=" "+e.className.replace(/[\t\r\n]/g," ")+" ";if(t(e,n)){for(;a.indexOf(" "+n+" ")>=0;)a=a.replace(" "+n+" "," ");e.className=a.replace(/^\s+|\s+$/g,"")}}function l(e,t){var n,a,l,o=t||document,u=[];if(o.querySelectorAll)return o.querySelectorAll("."+e);if(o.evaluate)for(a='.//*[contains(concat(" ", @class, " "), " '+e+' ")]',n=o.evaluate(a,o,null,0,null);l=n.iterateNext();)u.push(l);else for(n=o.getElementsByTagName("*"),a=new RegExp("(^|\\s)"+e+"(\\s|$)"),l=0;l<n.length;l++)a.test(n[l].className)&&u.push(n[l]);return u}function o(e,t,n){e.addEventListener?e.addEventListener(t,n,!1):e.attachEvent&&e.attachEvent("on"+t,n)}function u(e,t,n,a){e=e||"",t=t||{},n=n||"",a=a||function(){};var l=function(e){var t=[];for(var n in e)e.hasOwnProperty(n)&&t.push(n);return t};if("object"==typeof t){for(var o="",u=l(t),c=0;c<u.length;c++)o+=encodeURIComponent(u[c])+"="+encodeURIComponent(t[u[c]]),c!=u.length-1&&(o+="&");e+="?"+o}else"function"==typeof t&&(n=t,a=n);"function"==typeof n&&(a=n,n="callback"),Date.now||(Date.now=function(){return(new Date).getTime()});var r=Date.now(),i="jsonp"+Math.round(r+1000001*Math.random());window[i]=function(e){a(e);try{delete window[i]}catch(t){window[i]=void 0}},e+=e.indexOf("?")===-1?"?":"&";var s=document.createElement("script");s.setAttribute("src",e+n+"="+i),document.getElementsByTagName("head")[0].appendChild(s)}function c(){this.urls=["/ajax/AllBBS","/ajax/SeariesBBS","/ajax/areaBBS","/ajax/ThemeBBS","/ajax/MotorBBS"],this.urlDomain="//club.autohome.com.cn",this.clubData={findHtml:"",brandHtml:"",areaHtml:"",themeHtml:"",motorHtml:""},this.init()}c.prototype={init:function(){var e=this,t=document.getElementById("auto-header-find-club");o(t,"click",function(){e.openClubPop()});var n=document.getElementById("auto-header-clubclose");o(n,"click",function(){e.closeClubPop()});var a=document.getElementById("auto-header-club-tab0");o(a,"click",function(){e.enterClubTab(0)});var l=document.getElementById("auto-header-club-tab1");o(l,"click",function(){e.enterClubTab(1)});var u=document.getElementById("auto-header-club-tab2");o(u,"click",function(){e.enterClubTab(2)});var c=document.getElementById("auto-header-club-tab3");o(c,"click",function(){e.enterClubTab(3)});var r=document.getElementById("auto-header-club-tab4");o(r,"click",function(){e.enterClubTab(4)})},openClubPop:function(){this.changeTab(0),this.showView(this.urlDomain+this.urls[0],0);var e=document.getElementById("auto-header-clubmask"),t=document.getElementById("auto-header-clublayer");"none"==t.style.display&&(t.style.display="",e&&(e.style.display=""))},closeClubPop:function(){var e=document.getElementById("auto-header-clublayer"),t=document.getElementById("auto-header-clubmask");e&&(e.style.display="none"),t&&(t.style.display="none")},enterClubTab:function(e){this.changeTab(e),this.showView(this.urlDomain+this.urls[e],e)},changeTab:function(e){for(var t=0;t<=4;t++)document.getElementById("auto-header-club-tab"+t).className="";document.getElementById("auto-header-club-tab"+e).className="cur"},showView:function(e,t){function n(e){switch(document.getElementById("auto-header-clubhtml").innerHTML=e,t){case 0:a.initClubSearch();break;case 1:a.initClubSeries()}}var a=this,l=["findHtml","brandHtml","areaHtml","themeHtml","motorHtml"],o=l[t];if(o){document.getElementById("auto-header-clubhtml").innerHTML="";var c=a.clubData[o];""!=c?n(c):u(a.urlDomain+a.urls[t],function(e){var t=e.html||"";a.clubData[o]=t,n(t)})}},initClubSearch:function(){function e(e,t){if(2*e.length<=t)return e;for(var n=0,a="",l=0;l<e.length;l++)if(a+=e.charAt(l),e.charCodeAt(l)>128){if(n+=2,n>=t)return a.substring(0,a.length-1)}else if(n+=1,n>=t)return a.substring(0,a.length-2);return a}function t(e){if("none"!=r.style.display){var t=r.getElementsByTagName("li").length;38==e.keyCode&&(i--,i<=0&&(i=t)),40==e.keyCode&&(i++,i>t&&(i=1));for(var n=r.getElementsByTagName("a")[i-1],a=0;a<t;a++)r.getElementsByTagName("a")[a].style.backgroundColor="";n.style.backgroundColor="#e7f0f9",o.value=n.title}}function n(e){var t=o.value.replace(/(^\s*)|(\s*$)/g,"");if(""!=t&&t!=o.getAttribute("lang"))try{u("//sou.api.autohome.com.cn/v2/topicentry/search",{q:escape(t),_appid:"club"},"_callback",function(t){a(e,t)})}catch(n){}}function a(t,n){var a=[],l=[];if(n&&n.result&&"0"==n.returncode&&n.result.hitlist)for(var o=0;o<n.result.hitlist.length&&!(1==t&&a.length+l.length>9);o++){var u=n.result.hitlist[o].data,c=u.bbsname;if(c&&(c=c.indexOf("\u8bba\u575b")>-1?c:c+"\u8bba\u575b",a.push('<li><a target="_blank" href="//club.autohome.com.cn/bbs/forum-'+u.bbs+"-"+u.bbsid+'-1.html" title="'+c+'"  >'+c+"</a></li>")),u.carclub)for(var i=0;i<u.carclub.length;i++){var s=u.carclub[i];if(1==t&&a.length+l.length>9)break;l.push('<li><a target="_blank" href="//club.autohome.com.cn/carclub/index-'+u.bbs+"-"+u.bbsid+"-"+s.id+'-1.html" title="'+s.name+'">'+e(s.name,22)+"</a></li>")}}var d=document.getElementById("searchUl"),m=document.getElementById("searchh3"),h=document.getElementById("searchins");if(0==t){a.length>0?d.innerHTML=a.join(""):d.innerHTML="<span>\u62b1\u6b49\uff0c\u6ca1\u6709\u627e\u5230\u7ed3\u679c\u3002</span>",m.style.display="",d.style.display="",h.style.display="";var b=document.getElementById("_autoclubrecom"),f=b.getElementsByTagName("ul")[0];b.style.display="none",l.length>0&&(f.innerHTML=l.join(""),b.style.display="")}1==t&&(a.length+l.length>0?(r.innerHTML="<ul>"+a.join("")+l.join("")+"</ul>",r.style.display=""):r.style.display="none")}var l=document.getElementById("auto-header-clubhtml"),o=document.getElementById("otherSearch"),c=document.getElementById("otherBtn"),r=document.getElementById("seachtishibox"),i=0;""==o.value&&(o.value=o.getAttribute("lang")),o.onfocus=function(){o.parentNode.setAttribute("class","pf_search_fous"),o.getAttribute("lang")==o.value.replace(/(^\s*)|(\s*$)/g,"")&&(o.value="")},o.onblur=function(){""==o.value.replace(/(^\s*)|(\s*$)/g,"")&&(o.parentNode.setAttribute("class","pf_search"),o.value=o.getAttribute("lang"))},o.onkeydown=function(e){38!=e.keyCode&&40!=e.keyCode||t(e),13==e.keyCode&&(r.style.display="none",n(0))},o.onkeyup=function(e){38!=e.keyCode&&40!=e.keyCode&&13!=e.keyCode&&n(1)},c.onclick=function(){return n(0),r.style.display="none",!1},l.onclick=function(){r.style.display="none"},r.style.display="none"},initClubSeries:function(){function e(e){for(var t,n=c.getElementsByTagName("h4"),a=0;a<n.length;a++)if(t=n[a],t.getAttribute("lang")===e)return t}var t,o,u,c=document.getElementById("auto-header-clubhtml"),r=c.getElementsByTagName("h3")[0].getElementsByTagName("a"),i=l("backtop",c);for(i[0].style.display="none",u=0;u<i.length;u++)o=i[u],o.onclick=function(){c.scrollTop=0};for(u=0;u<r.length;u++)t=r[u],t.onclick=function(){for(var t=0;t<r.length;t++)a(r[t],"cur");n(this,"cur");var l=this.getAttribute("lang"),o=e(l);c.scrollTop=o.offsetTop}}},e.AutoHeaderClub=c,e.autoHeaderClubObj=new c}(this);
</script>
<script type="text/javascript">
    function loadScript(t, e) { var a = document.createElement("script"); a.type = "text/javascript", a.readyState ? a.onreadystatechange = function () { ("loaded" == a.readyState || "complete" == a.readyState) && (a.onreadystatechange = null, e()) } : a.onload = function () { e() }, a.src = t, document.body.appendChild(a) } loadScript("//x.autoimg.cn/space/AutoRequestHeader/zhixun/AutoHeartBeat.js?tv=101", function () { AutoHeartBeat.Main() });
</script>
<script type="text/javascript">
    (function () {
        var cityid = Math.floor(window.readCookie("cookieCityId", window.readCookie("area", 0)) / 100) * 100;
        var showCityId = [110100, 120100, 310100, 320500, 330100, 410100, 420100, 440100, 440300, 500100, 510100, 610100];
        if (showCityId.indexOf(cityid) > -1) {
            document.getElementById('auto-header-channel15').setAttribute("href", "//yc.autohome.com.cn/list?pvareaid=2868121");
            document.getElementById('auto-header-channel15').text = "养车";
        } else {
            document.getElementById('auto-header-channel15').setAttribute("href", "//k.autohome.com.cn/");
            document.getElementById('auto-header-channel15').text = "口碑";
        }
    })();
</script>

    <script type="text/javascript">
        var autoHeaderObj=new AutoHeader(2);
    </script>
    
	<div class="content">
	    
    <div class="monkey monkey_box fn-hide">
      <div id="s2823" data-adparent=".monkey"></div>
    </div>

		<!--导航栏开始-->
		

<div class="subnav">
	<div class="subnav-title fn-clear">
		<div class="subnav-title-name fn-left">
			<h2>资讯文章</h2>
		</div>
        <div class="subnav-title-ad fn-left" id="ad_pdgm">
            
        </div>
		<div class="search search02 fn-right">
			<div class="search-box">
                <form target="_blank" action="http://sou.autohome.com.cn/search.aspx" name="soform" id="souform">
                    <input data-toggle="search" data-val="请输入关键字" type="text" class="search-text" value="" autocomplete="off" id="q" name="q" />
                </form>
			</div>
			<a href="javascript:void(0);" onclick="document.getElementById('souform').submit(); return false;" class="btn btn-small btn-blue"><i class="icon16 icon16-search1"></i></a>
            <!--联想层-->
            <div id="autocomplateTip" class="search-pop" style="display:none"></div>
		</div>
	</div>
	<div id="ulNav" class="nav-typebar fn-clear">
	    <ul>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/all/">最新</a></li>
		    <li class="nav-item current"><a target="_self" href="http://www.autohome.com.cn/news/">新闻</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/advice/">导购</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/drive/">试驾评测</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/use/">用车</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/culture/">文化</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/travels/">游记</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/tech/">技术</a></li>
		    <li class="nav-item "><a target="_self" href="http://www.autohome.com.cn/tuning/">改装赛事</a></li>
	    </ul>
	</div>
</div>
        <!--导航栏结束-->
		
        <div class="row">
			<div class="column grid-13 grid-left">
				<!--焦点图开始-->
				
<div class="news-focus">
    <div class="focusimg focusimg02" id="focus-1">
        <!--图片内容部分-->
        <div class="focusimg-pic">
            <ul>
                
                    <li >
                        <h2><a href="http://www.autohome.com.cn/news/201708/906087.html#pvareaid=102623">昂科威降3.6万元 合资中型SUV降价排行</a></h2>
                        <p>[汽车之家 行情分析]  大家好，本周《降价排行榜》系列文章为大家介绍6款主流合资品牌中型SUV。我们从关注度较高的几款车中选取了近期优惠幅度较大的车型，包含楼兰、锐界、...</p>
                        <a href="http://www.autohome.com.cn/news/201708/906087.html#pvareaid=102623"><img src="http://www2.autoimg.cn/newsdfs/g15/M01/49/41/640x320_0_autohomecar__wKgH1lmeoICAd9DPAAkNQuRqwAc847.jpg" alt="昂科威降3.6万元 合资中型SUV降价排行"></a>
                    </li>
                
                    <li >
                        <h2><a href="http://www.autohome.com.cn/news/201708/906208.html#pvareaid=102623">60余款 2017成都车展首发/上市车汇总</a></h2>
                        <p>[汽车之家 新闻]  8月25日，2017成都车展于新国际会展中心（成都）正式拉开了帷幕，在此次车展上共有60余款新车上市/首发，包括新款奥迪A6系列、玛莎拉蒂新款Ghi...</p>
                        <a href="http://www.autohome.com.cn/news/201708/906208.html#pvareaid=102623"><img src="http://www3.autoimg.cn/newsdfs/g23/M14/2C/C6/640x320_0_autohomecar__wKgFXFmgKsyAKhPBAAchdRTCgFg669.jpg" alt="60余款 2017成都车展首发/上市车汇总"></a>
                    </li>
                
                    <li id="ad_368_1">
                        <h2><a href="http://www.autohome.com.cn/news/201708/906246.html#pvareaid=102623">8月29日发布 保时捷新Cayenne官图泄露</a></h2>
                        <p>[汽车之家 新车官图]  全新一代Cayenne将会在德国当地时间8月29日正式发布，接下来会在9月12日开幕的法兰克福车展上完成对公众的首秀。在新车亮相之前，新车的官图...</p>
                        <a href="http://www.autohome.com.cn/news/201708/906246.html#pvareaid=102623"><img src="http://www3.autoimg.cn/newsdfs/g15/M00/50/D5/640x320_0_autohomecar__wKjByFmiLWmAP0U8AAZliS_htrg508.jpg" alt="8月29日发布 保时捷新Cayenne官图泄露"></a>
                    </li>
                
            </ul>
        </div>
        <!--图片进度部分-->
        <div class="focusimg-bt">
            <div class="focusimg-bt-left"><a href="javascript:void(0);" target="_self"></a></div>
            <div class="focusimg-bt-right"><a href="javascript:void(0);" target="_self"></a></div>
        </div>
        <div class="focusimg-focus">
             
            <span class="selected" ><a href="javascript:void(0);" target="_self"></a></span>
             
            <span  ><a href="javascript:void(0);" target="_self"></a></span>
             
            <span  ><a href="javascript:void(0);" target="_self"></a></span>
             
        </div>
    </div>
</div>
				<!--焦点图结束-->
                
                <div class="advlist fn-clear">
                    
                    <i class="monkey__iconalone"></i>
                    <ul>
                        <li id="ad_word_t1"></li>
                        <li id="ad_word_t2"></li>
                        <li id="ad_word_t3"></li>
                    </ul>
                </div>
                <a name="liststart" class="aname">&nbsp;</a>
                <div class="monkey monkey_box fn-hide">
                  <div id="ad_760_21" data-adparent=".monkey"></div>
                  <div class="monkey__icon"></div>
                </div>
                
                <div class="m-nav-title m-nav-title-border">
                    <h3 class="h3cur"><a href="news/?p=s" target="_self">全部</a></h3>
                    <div class="div-fouc">
                        
                        <div class="div-fouc-bt div-fouc-bt-right"><a id="right" class="icon16 icon16-right" href="javascript:void(0);" target="_self"></a></div>
                  	    <div class="div-fouc-bt div-fouc-bt-left"><a id="left" class="icon16 icon16-left" href="javascript:void(0);" target="_self"></a></div>
                        
                        <div id="div-fouc-tx" class="div-fouc-tx">
                                             
                             <ul class='fouc-current'>                      
                                   
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="7" target="_self">行业动态</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="10" target="_self">热点追踪</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="40" target="_self">车闻轶事</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="70" target="_self">国产新车</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="71" target="_self">进口新车</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="87" target="_self">召回碰撞</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="114" target="_self">市场分析</a></li>
                            
                                 </ul>
                                          
                             <ul >                      
                                   
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="115" target="_self">用户调研</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="135" target="_self">高端访谈</a></li>
                            
                                 </ul>
                            
                    </div>
                                        
                    </div>
                </div>
                

				<!--文章内容开始-->
		        

<div id="auto-channel-lazyload-article" class="article-wrapper">
    
                     <ul class="article" >
    
                        <li data-artIdAnchor="906330">
                            <a href="http://www.autohome.com.cn/news/201708/906330.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g20/M04/2E/FB/120x90_0_autohomecar__wKgFWVmjdPGAW1LQAACcDXFWyJI637.jpg"></div>
                                <h3>将于9月正式亮相 曝奇瑞全新SUV设计图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">10分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1002</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906330"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，奇瑞官方表示，旗下的全新紧凑型SUV（代号M31T）将于今年9月12日开幕的法兰克福车展正式发布，同时其还公布了一组关于该...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906326">
                            <a href="http://www.autohome.com.cn/news/201708/906326.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g16/M05/4D/DA/120x90_0_autohomecar__wKgH11mjYlmAEmE_AAFFm5FMjro155.jpg"></div>
                                <h3>售7.89-8.99万元 比速T3自动挡正式上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">48分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4228</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906326"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  日前，我们从官方获悉，比速T3自动挡车型正式上市销售。新车推出搭载1.3T发动机共3款车型，传动匹配CVT变速箱。该车的上市...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906196">
                            <a href="http://www.autohome.com.cn/news/201708/906196.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g10/M07/4D/3E/120x90_0_autohomecar__wKjBzVmgINyAIV37AAGYzjt8DKA676.jpg"></div>
                                <h3>星脉/天逸等 成都车展年内上市新车盘点</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>19.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906196"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  2017成都车展还在进行当中，在8月25日的媒体日可谓是新车云集。其中，除了大量当日公布售价的上市车外，还有不少公布了预售价或者...</p>
                            </a>
                        </li>
    
                        <li id="ad_tw_04" style="display: none;"></li>
    
                        <li data-artIdAnchor="906325">
                            <a href="http://www.autohome.com.cn/news/201708/906325.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g5/M00/4C/F1/120x90_0_autohomecar__wKgHzFmi8eqACGOJAAFqEqA5Eh4067.jpg"></div>
                                <h3>配置更丰富 新款北京BJ40L谍照曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906325"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从相关渠道获得了一组新款北京BJ40L的测试车谍照，该车的外观和内饰设计与现款基本保持一致，前保险杠进行了小幅调整...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906318">
                            <a href="http://www.autohome.com.cn/news/201708/906318.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g10/M06/4D/A4/120x90_0_autohomecar__wKgH0VmisuSATUPdAAFMo709XMs099.jpg"></div>
                                <h3>3种动力/6款车型 福特新款翼搏9月上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906318"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  近日，我们从长安福特官方获悉，新款翼搏将于9月正式上市，新车将推出搭载1.5L/1.0T/2.0L三种动力的共计6款车型，传动系...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906323">
                            <a href="http://www.autohome.com.cn/news/201708/906323.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g9/M0D/4B/29/120x90_0_autohomecar__wKjBzlmi8PKAKQnUAADqObcGJRQ213.jpg"></div>
                                <h3>参与排放作弊 大众首位认罪高层被判刑</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>7179</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906323"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，有海外媒体报道，随着大众集团柴油车排放作弊事件的不断扩大，又有新的人员遭到了相关处罚。据悉，美国联邦检察部门近日判处了参与...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906320">
                            <a href="http://www.autohome.com.cn/news/201708/906320.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g12/M12/50/3E/120x90_0_autohomecar__wKjBy1mi0t2AcL4OAADuOw4IkWg798.jpg"></div>
                                <h3>将于9月正式上市销售 凯翼X5配置曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906320"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从官方获取到了凯翼X5的配置信息，根据配置表来看，该车将推出2.0L/1.5T两种动力共计6款车型，传动系统匹配5速手...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906319">
                            <a href="http://www.autohome.com.cn/news/201708/906319.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g7/M15/4E/48/120x90_0_autohomecar__wKgHzlmiyR-AfSbKAAEW3T7d_Z0807.jpg"></div>
                                <h3>睿骋CC年底上市 曝长安汽车新产品计划</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906319"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从官方获悉，长安旗下全新中型车——睿骋CC将会在今年年底正式上市销售，同时，长安CS75、CS35以及逸动等车型也将相...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906252">
                            <a href="http://www.autohome.com.cn/news/201708/906252.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g14/M05/51/33/120x90_0_autohomecar__wKgH5FmhMomAX7QXAAFzGwUUcSE749.jpg"></div>
                                <h3>起亚2款新车：KX CROSS/凯绅今日上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">9小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.6万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906252"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  今天下午（8月28日），东风悦达起亚凯绅及起亚KX CROSS车型将共同上市。其中，起亚凯绅是起亚K4的中期改款车型，动力方面搭...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906209">
                            <a href="http://www.autohome.com.cn/news/201708/906209.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g10/M01/49/DC/120x90_0_autohomecar__wKgH0Vmf2HqAWyrPAAENkrr0XJ4223.jpg"></div>
                                <h3>预计续航604公里 全新尚酷或转型电动车</h3>
                                <div class="article-bar">
                                    <span class="fn-left">13小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906209"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前有海外媒体报道称，全新一代大众尚酷或将转变成纯电动跑车。入门版车型为170马力，拥有300马力的高配车型或将搭载两台电动机，...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906188">
                            <a href="http://www.autohome.com.cn/news/201708/906188.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g4/M10/53/C2/120x90_0_autohomecar__wKgH2lmhWlOAKwj6AAEgmXPeTMM753.jpg"></div>
                                <h3>旋钮换挡配拨片 曝宝骏310 iAMT新谍照</h3>
                                <div class="article-bar">
                                    <span class="fn-left">23小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906188"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从相关渠道获得一组宝骏310 iAMT车型的实车图片。宝骏的iAMT（智能手动变速箱）是由上汽通用五菱和爱信共同研...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906181">
                            <a href="http://www.autohome.com.cn/news/201708/906181.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g10/M15/4C/16/120x90_0_autohomecar__wKjBzVmflCiACElSAAGRajbdHfE936.jpg"></div>
                                <h3>2018年发布 奥迪Q8国内路试谍照曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>18.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906181"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  继不久前海外媒体曝光了奥迪Q8的低伪装谍照之后，近期我们又从相关渠道获得了一组该车在国内路试的谍照图片。图中显示，两台车身贴...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906283">
                            <a href="http://www.autohome.com.cn/news/201708/906283.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g15/M13/50/02/120x90_0_autohomecar__wKgH5VmhihqAALmfAABtbp6gygQ759.jpg"></div>
                                <h3>M3自动挡9月上市 比速新产品计划公布</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906283"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  近日，我们从比速汽车官方获悉，比速M3自动挡车型和比速T5自动挡车型将分别于今年9月和10月正式上市，新车的推出将进一步丰富比速...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906269">
                            <a href="http://www.autohome.com.cn/news/201708/906269.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g18/M04/4F/0F/120x90_0_autohomecar__wKjBxVmhZ-WAdXtuAADhxGKCmsQ755.jpg"></div>
                                <h3>森雅R9/7座SUV 曝一汽吉林两款SUV计划</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>11.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906269"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从一汽吉林官方获悉，森雅R9将会在2018年5月正式上市。除此之外，在2019年还将推出一款7座SUV车型。『此前曝光...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906278">
                            <a href="http://www.autohome.com.cn/news/201708/906278.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g18/M0E/52/6B/120x90_0_autohomecar__wKgH6FmhftGAS6xMAAFXS_i1W2M000.jpg"></div>
                                <h3>推5款车型 奔驰新款S级详细预售价曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>23.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906278"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从奔驰经销商处获得了新款S级的具体车型预售价。据了解，新车共将推出5款车型，包括S 320 L、S 350 L、 S ...</p>
                            </a>
                        </li>
    
                    </ul>
    
                     <ul class="article" style="display:none;">
    
                        <li data-artIdAnchor="906158">
                            <a href="http://www.autohome.com.cn/news/201708/906158.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g22/M12/CC/84/120x90_0_autohomecar__wKgFW1mhcvqATH2MAAFYXn0Opug843.jpg"></div>
                                <h3>售7.38-11.68万元 广汽传祺GS3正式上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>72.8万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906158"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017年8月26日，广汽传祺GS3携手家族兄弟GS7在乌镇正式上市。此次GS3推出1.5L（150N）和1.3T（200T...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906154">
                            <a href="http://www.autohome.com.cn/news/201708/906154.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g16/M10/4B/9B/120x90_0_autohomecar__wKgH11mhbnCALBaVAAGOaAFkUY4675.jpg"></div>
                                <h3>售14.98-20.98万元 广汽传祺GS7上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>36.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906154"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市] 2017年8月26日，广汽传祺全新中型SUV车型GS7在乌镇正式上市，新车推出1.8T和2.0T两种排量共5款车型，售价区间为...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906253">
                            <a href="http://www.autohome.com.cn/news/201708/906253.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g14/M09/4A/8E/120x90_0_autohomecar__wKgH1VmhR_qAD0HOAAFrn4-ULd4201.jpg"></div>
                                <h3>2017成都车展：海马S5青春版5.98万元起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>12.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906253"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]　 在2017成都车展上，海马汽车旗下海马S5青春版正式上市，新车是海马S5 Young的更名车型，增加了CVT版本，共推出6款...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906237">
                            <a href="http://www.autohome.com.cn/news/201708/906237.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g19/M13/26/E2/120x90_0_autohomecar__wKjBxFmgHcWAOL3JAAFKfv87lEQ544.jpg"></div>
                                <h3>2018年3月正式投产 宝马M2 CS最新消息</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906237"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  宝马M2（F87）的推出并不是终点，只是个开始，宝马M部门接下来还将推出M2 CS以及M2 GTS等车型。日前，有这两款新车的投...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906230">
                            <a href="http://www.autohome.com.cn/news/201708/906230.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g18/M11/50/74/120x90_0_autohomecar__wKgH6FmgDhaASmTZAAFyNQJUkhw403.jpg"></div>
                                <h3>汉腾计划：X7s年底上市/明年推首款MPV</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906230"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  在本届成都车展上我们从汉腾汽车官方获悉，汉腾X7s车型将于今年年底上市销售。随着汉腾X7/X5/X7s的相继上市，汉腾的SUV产...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906227">
                            <a href="http://www.autohome.com.cn/news/201708/906227.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g22/M06/C7/C5/120x90_0_autohomecar__wKjBwVmgE7GAUFBlAAFkE3UizKE037.jpg"></div>
                                <h3>2017成都车展：斯威X7国米版售9.99万</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>11.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906227"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017成都车展已经正式拉开帷幕，在本届车展上，斯威汽车发布了斯威X7国际米兰特别版车型，该车型汲取了国际米兰球队的球队元素...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906213">
                            <a href="http://www.autohome.com.cn/news/201708/906213.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g6/M08/4C/4D/120x90_0_autohomecar__wKgHzVmgA7mAbPBwAAGgxGDp01A390.jpg"></div>
                                <h3>2017成都车展：2018款蔚揽实车首发</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>16.1万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906213"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  日前，我们从大众官方获悉，2018款大众蔚揽正式在2017成都车展亮相，新车将推出六款车型，预计于今年9-10月份左右上市销...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906219">
                            <a href="http://www.autohome.com.cn/news/201708/906219.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g16/M0C/49/C4/120x90_0_autohomecar__wKgH11mf-sGABqVPAAFiF1yf2pc189.jpg"></div>
                                <h3>最高降2万 比亚迪S7/宋/元全系官降</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>19.5万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906219"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 车型调价]  日前我们从比亚迪官方获悉，宋/S7/元三款车型全系价格下调，下调幅度最高2万元。下调后宋的售价区间为7.99-12.99万元...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906217">
                            <a href="http://www.autohome.com.cn/news/201708/906217.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g20/M11/27/4F/120x90_0_autohomecar__wKjBw1mf8EmAeGITAAGtngW33E0317.jpg"></div>
                                <h3>售26.8万起 纳智捷大7 SUV新增车型上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906217"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  日前，我们从官方获悉，纳智捷大7 SUV新增两款Sport+车型，售价分别为26.8和29.3万元。新车动力上继续搭载现款2...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906131">
                            <a href="http://www.autohome.com.cn/news/201708/906131.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g21/M14/26/91/120x90_0_autohomecar__wKjBwlmf5eiAEgG_AAF-Cc34_9Q328.jpg"></div>
                                <h3>成都车展：新款凯路威/迈特威35.18万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>6.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906131"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017成都车展已拉开帷幕，进口大众2018款迈特威/凯路威在本届车展正式上市，其中新款迈特威售价区间为41.88-55.5...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906197">
                            <a href="http://www.autohome.com.cn/news/201708/906197.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g21/M05/2A/13/120x90_0_autohomecar__wKgFWlmf1biAAQx8AAGQryjne7A794.jpg"></div>
                                <h3>2017成都车展：众泰T300新车售5.88万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>11.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906197"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017成都车展已经正式拉开帷幕，在本届车展上，众泰汽车发布了众泰T300双色版车型，该车在外观及内饰方面都与现款车型保持一...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905968">
                            <a href="http://www.autohome.com.cn/news/201708/905968.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g13/M0A/4E/3E/120x90_0_autohomecar__wKjBylmfxSWAJXGOAAFu6wyY-lM936.jpg"></div>
                                <h3>成都车展：汉腾X5高配车型预售9.88万</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>9.5万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905968"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  在本届成都车展上，汉腾汽车为我们带来了其紧凑型SUV——汉腾X5的预售消息，其官方目前仅发布一款车型的预售价，其价格为9.88万...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905965">
                            <a href="http://www.autohome.com.cn/news/201708/905965.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g5/M11/4F/A8/120x90_0_autohomecar__wKgH21mfxEiACZdEAAFmsvSmytM729.jpg"></div>
                                <h3>2017成都车展：斯威X7新车售10.19万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4.5万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905965"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]　 在本届成都车展上，斯威X7自动挡车型正式上市，新车价格区间为10.19-11.39万，新车共推出1.5T 自动智慧型、1.5...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906107">
                            <a href="http://www.autohome.com.cn/news/201708/906107.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g10/M0E/4C/9C/120x90_0_autohomecar__wKjBzVmf0aqAX883AAF23WX_5go276.jpg"></div>
                                <h3>2017成都车展：野马斯派卡预售5.98万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.6万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906107"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  本届成都车展上，野马汽车旗下首款MPV车型——斯派卡（Spica）正式开启预售。新车共包含2款车型，预售价分别为5.98万元...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906187">
                            <a href="http://www.autohome.com.cn/news/201708/906187.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g7/M15/4D/E0/120x90_0_autohomecar__wKjB0FmfvImAcxlUAAFqZsJgYwg934.jpg"></div>
                                <h3>2017成都车展：纳智捷U5预售7.58万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>7.6万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906187"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  2017成都车展已经拉开帷幕，东风裕隆宣布旗下全新小型SUV——纳智捷U5 SUV正式开启预售，新车预售价格区间是7.58-10...</p>
                            </a>
                        </li>
    
                    </ul>
    
                     <ul class="article" style="display:none;">
    
                        <li data-artIdAnchor="906185">
                            <a href="http://www.autohome.com.cn/news/201708/906185.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g18/M03/4F/C5/120x90_0_autohomecar__wKgH6FmfwHKAarWJAAGryi0p-sc340.jpg"></div>
                                <h3>2017成都车展：圣达菲7预售8万元起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906185"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  在刚刚开幕的成都车展上，圣达菲7四款车型正式开启预售，其预售价区间为8.0-9.5万元。据悉，新车将于今年9月正式上市。圣达菲7...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905889">
                            <a href="http://www.autohome.com.cn/news/201708/905889.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g7/M0B/51/2E/120x90_0_autohomecar__wKgH3VmfueeAZut_AAF-yamBU6I997.jpg"></div>
                                <h3>2017成都车展：华泰圣达菲5售7.68万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905889"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  本届成都车展上，华泰圣达菲5正式上市，新车推出共7款车型，官方指导价格区间为7.68-11.18万元。新车基本沿用了现款车型...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906184">
                            <a href="http://www.autohome.com.cn/news/201708/906184.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g19/M0A/29/5D/120x90_0_autohomecar__wKgFWFmfs46AadWGAAFi4I97ZpI353.jpg"></div>
                                <h3>2017成都车展：新款甲壳虫售19.58万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>12.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906184"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在本届成都车展上，2018款大众甲壳虫车型上市销售，新车售价与老款车型保持一致，仍为19.58-27.46万元。新车相比老款...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906119">
                            <a href="http://www.autohome.com.cn/news/201708/906119.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g23/M01/2B/E3/120x90_0_autohomecar__wKgFXFmfsuWAIGJ-AAEZELJQ7as447.jpg"></div>
                                <h3>2017成都车展：新款东南DX7售8.99万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>11.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906119"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  本届成都车展上，2018款东南DX7正式上市。新车推出搭载2种动力的共计15款车型，售价区间为8.99-13.99万元。新车...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906183">
                            <a href="http://www.autohome.com.cn/news/201708/906183.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g23/M00/24/A8/120x90_0_autohomecar__wKgFV1mfsuSAYApmAAG8LvqmfpA687.jpg"></div>
                                <h3>成都车展：2018款Tiguan售26.28万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>22.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906183"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017成都车展上，进口大众2018款Tiguan车型正式上市，新车同样推出4款车型，售价区间为26.28-39.18万元，...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906182">
                            <a href="http://www.autohome.com.cn/news/201708/906182.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g14/M14/4C/12/120x90_0_autohomecar__wKjByVmfsQ2AVozdAAG4_n1ook4180.jpg"></div>
                                <h3>2017成都车展：欧陆GT炫黑套件版首发 </h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906182"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  2017成都车展已经正式拉开帷幕，在本届车展上，宾利官方带来了基于欧陆GT V8 S打造的特别版车型，该车装配了Blackl...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906137">
                            <a href="http://www.autohome.com.cn/news/201708/906137.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g5/M06/48/47/120x90_0_autohomecar__wKgHzFmfqJuAQ_FcAAFjxejrzT4402.jpg"></div>
                                <h3>成都车展：新款奥迪A6系列售40.60万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>59.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906137"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在2017成都车展上，奥迪A6L 30周年年型版车型正式上市，其售价区间为40.60-69.80万元。与此同时，A6L 40...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905880">
                            <a href="http://www.autohome.com.cn/news/201708/905880.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g9/M05/53/86/120x90_0_autohomecar__wKgH31mfpV6ACzAzAAFN_q-YC6I561.jpg"></div>
                                <h3>2017成都车展：远景X3售价5.09-6.59万</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>20.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905880"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  本届成都车展上，吉利远景X3正式上市，官方指导价格区间为5.09-6.59万元。新车共推出1.5L-MT 进取型、1.5L-...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905926">
                            <a href="http://www.autohome.com.cn/news/201708/905926.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g10/M14/4C/3D/120x90_0_autohomecar__wKjBzVmfo2iAYXdqAAFLQflYqEg214.jpg"></div>
                                <h3>2017成都车展：艾瑞泽5e售21.28万元起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.6万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905926"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在本届成都车展上，奇瑞艾瑞泽5e正式上市，补贴前指导价格区间为21.28-23.28万，补贴后价格区间为13.98-15.9...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905925">
                            <a href="http://www.autohome.com.cn/news/201708/905925.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g6/M0B/4B/83/120x90_0_autohomecar__wKgHzVmfogeAA5myAAFwP-ovC7g030.jpg"></div>
                                <h3>2017成都车展：宝沃BX5新车售12.38万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>17.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905925"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  本届成都车展上，宝沃BX5 1.4T车型正式上市，官方指导价格区间为12.38-15.58万元。新车型的推出将进一步丰富宝沃...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905927">
                            <a href="http://www.autohome.com.cn/news/201708/905927.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g11/M07/49/70/120x90_0_autohomecar__wKgH0lmfnkWAYejkAAGHOGEOX3A688.jpg"></div>
                                <h3>2017成都车展:铃木英格尼斯售12.90万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>10.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905927"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]　 在本届成都车展上，铃木英格尼斯（IGNIS）正式上市，该车为进口引入，新车共推出1.2L两驱CVT豪华版（无导航配置）/（导...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906104">
                            <a href="http://www.autohome.com.cn/news/201708/906104.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g14/M0F/48/33/120x90_0_autohomecar__wKgH1VmfnOWAbVABAAF8_-AqOJA434.jpg"></div>
                                <h3>2017成都车展：新款奥迪A7售59.80万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>33.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906104"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在本届成都车展上，2018款奥迪A7正式上市，新车提供三种动力，共五款车型，售价区间为59.80-89.80万元。奥迪新款A...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905983">
                            <a href="http://www.autohome.com.cn/news/201708/905983.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g22/M03/C8/7C/120x90_0_autohomecar__wKgFW1mfnJ-ADP1JAAGpd4SERk0924.jpg"></div>
                                <h3>成都车展：2018款奥迪S7售135.80万元</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>6.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905983"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在2017成都车展上，2018款奥迪S7将正式上市销售，新车整体外观造型与现款车型基本保持一致，主要针对细节方面进行一些调整...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906160">
                            <a href="http://www.autohome.com.cn/news/201708/906160.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g6/M09/A4/C9/120x90_0_autohomecar__wKgH3Fmfms6ASFWXAAFsA-65vvw362.jpg"></div>
                                <h3>2017成都车展：广汽讴歌TLX-L正式亮相</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>7.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906160"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  2017成都车展刚刚开幕，在本届车展上，广汽讴歌TLX-L量产版正式亮相。新车基本沿用概念车的设计语言，不过在细节方面处理的...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906106">
                            <a href="http://www.autohome.com.cn/news/201708/906106.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g20/M05/24/66/120x90_0_autohomecar__wKgFVFmfmuCAUxPZAAFYZK1j0DQ622.jpg"></div>
                                <h3>2017成都车展：新款欧蓝德售15.98万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>34.8万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906106"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在刚刚开幕的2017成都车展上，广汽三菱2018款欧蓝德正式上市，售价区间为15.98-22.38万元。相比现款车型，新车主...</p>
                            </a>
                        </li>
    
                    </ul>
    
                     <ul class="article" style="display:none;">
    
                        <li data-artIdAnchor="906112">
                            <a href="http://www.autohome.com.cn/news/201708/906112.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g17/M01/47/0C/120x90_0_autohomecar__wKjBxlmfmX6AZJfvAAFd3lRuqx0590.jpg"></div>
                                <h3>2017成都车展：新款帕杰罗售36.98万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>23.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906112"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]　 在刚刚开幕的2017成都车展上，新款帕杰罗正式上市，新车共推出3款车型，其售价区间为36.98-42.98万元。相比现款车型...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906111">
                            <a href="http://www.autohome.com.cn/news/201708/906111.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g5/M02/48/28/120x90_0_autohomecar__wKgHzFmfmR2AZ77wAAGo14IauE4569.jpg"></div>
                                <h3>2017成都车展：新款劲炫ASX售11.48万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>20.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906111"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]　 在刚刚开幕的2017成都车展上，广汽三菱新款劲炫ASX正式上市，其售价区间为11.48-14.98万元。相比老款车型，新车主...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905872">
                            <a href="http://www.autohome.com.cn/news/201708/905872.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g21/M02/25/DB/120x90_0_autohomecar__wKjBwlmfl66AV8SbAAGHEAg8oq4656.jpg"></div>
                                <h3>2017成都车展:雪铁龙天逸预售15.37万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>24.6万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905872"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017成都车展已经正式拉开帷幕，东风雪铁龙旗下全新紧凑型SUV——天逸 C5 AIRCROSS正式开启预售，新车共推出2款...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906165">
                            <a href="http://www.autohome.com.cn/news/201708/906165.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g6/M06/50/17/120x90_0_autohomecar__wKjB0VmflkqAB0XDAAEzS593A7g805.jpg"></div>
                                <h3>2017成都车展：新款911 GT3售价202.8万</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>9.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906165"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在2017成都车展期间，保时捷新款911 GT3车型完成了在国内的首次亮相，该车的正式售价为202.8万元。新车除了针对外观...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906153">
                            <a href="http://www.autohome.com.cn/news/201708/906153.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g7/M09/4D/93/120x90_0_autohomecar__wKjB0FmflXiAYvfEAAFePlunuTY915.jpg"></div>
                                <h3>成都车展：瑞风S2/S3智驱版售5.98万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906153"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  日前，江淮汽车旗下的瑞风S2/S3智驱系列在2017成都车展期间正式上市，其中瑞风S2智驱版售价区间为5.98-7.68万元...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905755">
                            <a href="http://www.autohome.com.cn/news/201708/905755.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g12/M05/46/08/120x90_0_autohomecar__wKgH01mfkpWAEi1nAAGoeqKAAXE388.jpg"></div>
                                <h3>2017成都车展：M3/M4限量版售106.8万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905755"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在2017成都车展上，宝马M3/M4车迷限量版（以下简称宝马M3/M4）正式上市，新车较现款车型采用了独特的外观涂装，其指导...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905827">
                            <a href="http://www.autohome.com.cn/news/201708/905827.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g11/M11/4B/CE/120x90_0_autohomecar__wKjBzFmfk1mAOBYIAAFrFHFWl6M535.jpg"></div>
                                <h3>2017成都车展：新款XC90 T8 99.80万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8.8万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905827"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在2017成都车展期间，2018款沃尔沃XC90 E驱混动T8车型正式上市，新车将继续推出搭载2.0T混动系统的三款车型，动...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906121">
                            <a href="http://www.autohome.com.cn/news/201708/906121.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g4/M13/4E/50/120x90_0_autohomecar__wKjB01mfj-uADlHHAAFN6LtUh3Q540.jpg"></div>
                                <h3>2017成都车展：起亚全新福瑞迪正式亮相</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906121"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  在本届成都车展上，起亚全新福瑞迪正式亮相，新车整体外观造型采用了全新的设计风格，进一步提升市场竞争力，此外，该车还搭载了起亚...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905799">
                            <a href="http://www.autohome.com.cn/news/201708/905799.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g4/M11/48/EA/120x90_0_autohomecar__wKgHy1mfkiqAE07KAAF8rWW4bRg823.jpg"></div>
                                <h3>2017成都车展：探界者RS售22.09万元起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>23.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905799"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在正在进行的2017成都车展上，雪佛兰RS旗下的探界者RS车型正式上市。此次上市的车型共3款，指导价格为22.09-25.0...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906179">
                            <a href="http://www.autohome.com.cn/news/201708/906179.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g22/M06/C8/55/120x90_0_autohomecar__wKgFW1mfkVmAFqdvAAFXa5fC_94798.jpg"></div>
                                <h3>成都车展：新款奔驰S级预售95-155万元</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>31.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906179"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  2017成都车展上，新款奔驰S级正式公布了预售价格，其未来将推出5款车型，预售价95—155万元。新车在外观上相比现款车型进行了...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906166">
                            <a href="http://www.autohome.com.cn/news/201708/906166.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g22/M12/C6/35/120x90_0_autohomecar__wKjBwVmfkUWANoFfAAFMzTyaDrw939.jpg"></div>
                                <h3>2017成都车展:东风风神AX4预售价7-11万</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5.5万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906166"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2017成都车展已经正式拉开帷幕，东风风神首款小型SUV——AX4也于本次车展正式开启预售，新车搭载了1.6L和1.4T两款...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905804">
                            <a href="http://www.autohome.com.cn/news/201708/905804.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g20/M0C/29/CC/120x90_0_autohomecar__wKgFWVmfkMmAG6P7AAGWtsppehU673.jpg"></div>
                                <h3>2017成都车展：宝马5系标轴售46.58万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>23.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905804"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  在2017成都车展上，全新宝马5系标准轴距版的进口车型正式上市。新车搭载2.0T和3.0T汽油发动机，共推出3款车型，指导价...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905835">
                            <a href="http://www.autohome.com.cn/news/201708/905835.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www3.autoimg.cn/newsdfs/g5/M0E/4A/30/120x90_0_autohomecar__wKjB0lmfkL-AF02RAAHuRGAl7cs016.jpg"></div>
                                <h3>成都车展:奔驰C 300轿跑车璨夜特别版</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>12.1万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905835"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  在本届成都车展上，奔驰C 300轿跑璨夜特别版正式亮相，该车以奔驰C级轿跑版为基础，增加了很多个性化配置。    奔驰C 3...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="905723">
                            <a href="http://www.autohome.com.cn/news/201708/905723.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g16/M0F/4D/10/120x90_0_autohomecar__wKjBx1mfjKGAOfyuAAFRsFdKy2k981.jpg"></div>
                                <h3>2017成都车展：LX570特别版售146.90万</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>14.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="905723"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]　 在本届成都车展上，雷克萨斯带来了LX570巅峰特别限量版正式上市，其售价区间为146.90元。该车的整体外观造型与之前海外发...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="906178">
                            <a href="http://www.autohome.com.cn/news/201708/906178.html#pvareaid=102624">
                                <div class="article-pic"><img src="http://www2.autoimg.cn/newsdfs/g20/M13/24/3F/120x90_0_autohomecar__wKgFVFmfi5SACyzpAAEKuWksihc478.jpg"></div>
                                <h3>E-PACE/XEL等 捷豹路虎国产新车计划</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="906178"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  在刚刚开幕的2017成都车展上，捷豹路虎正式发布了其未来的国产计划，其计划在3年内推出5款新车（包括极光和发现神行），其中包括捷...</p>
                            </a>
                        </li>
    
                    </ul>
    
    
</div>

<a target="_self" style="display:none;" id="btnLoading" class="loading" href="javascript:void(0);"><span class="loading-cont">加载中</span><img src="http://www.autohome.com.cn/channel2/channel/images/btn-loading.gif"></a>                                                                                                                        
<div id="channelPage" class="page">
<a class="page-item-prev page-disabled" target="_self" href="javascript:void(0);"><b></b>上一页</a>
<a class="current" href="javascript:void(0);">1</a><a target="_self"  href="/news/2/#liststart">2</a><a target="_self"  href="/news/3/#liststart">3</a><a target="_self"  href="/news/4/#liststart">4</a><a target="_self"  href="/news/5/#liststart">5</a><a target="_self"  href="/news/6/#liststart">6</a><a target="_self"  href="/news/7/#liststart">7</a><a target="_self"  href="/news/8/#liststart">8</a><a target="_self"  href="/news/9/#liststart">9</a><span class="page-item">...</span><a target="_self" href="/news/3772/#liststart">3772</a>
<a class="page-item-next" target="_self" href="/news/2/#liststart">下一页<b></b></a></div>

		        <!--文章内容结束-->
            </div>
			<div class="column grid-7 grid-right">
				<div class="hot">
                    <!--热门文章开始-->
		            
            <div class="hot-title">热门文章</div>
        <div class="hot-article-wrap">
	        <ul>
        
                <li>
			    <h2><a href="http://www.autohome.com.cn/news/201708/905649-5.html#pvareaid=102625">讴歌TLX-L等12款 成都车展新车前瞻(下)</a></h2>
			    <a href="http://www.autohome.com.cn/news/201708/905649.html#pvareaid=102625"><img src="http://www2.autoimg.cn/newsdfs/g4/M03/47/64/120x90_0_autohomecar__wKgH2lmZmSaAF5CsAAGewY91y_8805.jpg" /></a>
			    <p class="hot-intro">[汽车之家 新闻]  在经过了几个月的修整之后，忙碌的车展又将一一到来，其中距离我们最近的...</p>
		    </li>
        
                <li>
			    <h2><a href="http://www.autohome.com.cn/news/201708/906094.html#pvareaid=102625">新款Ghibli等31款 成都车展探馆汇总</a></h2>
			    <a href="http://www.autohome.com.cn/news/201708/906094.html#pvareaid=102625"><img src="http://www2.autoimg.cn/newsdfs/g15/M00/4A/1F/120x90_0_autohomecar__wKjByFmdaouAVW1rAAGbG2ypMFM397.jpg" /></a>
			    <p class="hot-intro">[汽车之家 新闻]  2017成都车展将在8月25日正式拉开帷幕，日前我们汽车之家前方报道...</p>
		    </li>
        
                <li>
			    <h2><a href="http://www.autohome.com.cn/news/201708/906002.html#pvareaid=102625">9月2日上市/8款车型 揽胜星脉实车到店</a></h2>
			    <a href="http://www.autohome.com.cn/news/201708/906002.html#pvareaid=102625"><img src="http://www3.autoimg.cn/newsdfs/g18/M0D/3F/7E/120x90_0_autohomecar__wKgH2VmasAKAf30VAAEhqRSiiZ4296.jpg" /></a>
			    <p class="hot-intro">[汽车之家 新闻]  日前，我们从经销商处拍摄到揽胜星脉的到店实车图，该车将提供包括2.0...</p>
		    </li>
        
            </ul>
            </div>
        


	    
		            <!--热门文章结束-->
                    
                    <div class="advbox monkey monkey_box fn-hide">
                      <div id="s2851" data-adparent=".monkey"></div>
                    </div>

                    <!--热门评论开始-->
		            
<style type="text/css">

.hot-more{ float:right; font-weight:normal; font-style:normal; font-size:12px;}

    .hot-article-rec {
        padding-top: 10px;
    }
        .hot-article-rec img {
            vertical-align: top;
        }
        .hot-article-rec li {
            float: left;
            width: 140px;
            margin: 6px 10px 0 0;
            text-align: center;
        }
            .hot-article-rec li p {
                margin: 5px 0;
            }
</style>

<div class="hot">
    
    <div class="hot-title"><a class="hot-more" href="http://www.autohome.com.cn/channel2/union/list.html?pvareaid=103651#class_1" target="_blank">更多&gt;&gt;</a>精彩分类</div>
    
    <div class="hot-article-rec fn-clear">
        <ul>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/54/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516250500461.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/54/0/1/conjunction.html#pvareaid=103651">新车首次发布</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/26207/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516222909794.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/26207/0/1/conjunction.html#pvareaid=103651">销量风云榜</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/15346/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516232440502.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/15346/0/1/conjunction.html#pvareaid=103651">行情分析</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/28371/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/9/1/140x80_0_2014090121282441437.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/28371/0/1/conjunction.html#pvareaid=103651">数说新车</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/4561/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516330468985.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/4561/0/1/conjunction.html#pvareaid=103651">产销数据</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/28098/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/9/22/140x80_0_2014092209160808624.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/28098/0/1/conjunction.html#pvareaid=103651">电动车新闻</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/11079/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516444021707.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/11079/0/1/conjunction.html#pvareaid=103651">新车官图</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="http://www.autohome.com.cn/25948/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="http://www1.autoimg.cn/newspic/2014/8/26/140x80_0_2014082615054173139.jpg" ></a>
                  <p><a href="http://www.autohome.com.cn/25948/0/1/conjunction.html#pvareaid=103651">海外车展</a></p>
                                              
                
             </li>
            
        </ul>
    </div>
</div>

		            <!--热门评论结束-->
                    
                    <div class="advbox monkey monkey_box fn-hide">
                      <div id="s2852" data-adparent=".monkey"></div>
                    </div>

                    <!--编辑博客开始-->
					

<div class="editorblog">
	<div class="editorblog-title-container">
		<div class="editor-change" style="display:none;">
			<i class="icon12 icon12-repeat"></i>
			<a id="switchByRan" href="javascript:void(0);" target="_self">换一换</a>
		</div>
		<div class="editorblog-title">编辑博客</div>
	</div>
	<div class="editor-wrap">
		<ul id="tagInfo">
			
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_5070.html#pvareaid=102628"><img src="http://www3.autoimg.cn/newsdfs/g16/M05/24/AE/40x0_0_autohomecar__wKgH11aA97iAE379AACaUNwR9bA709.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_5070.html#pvareaid=102628">耿源</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">责任编辑</div>
			        </li>
                
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_5314.html#pvareaid=102628"><img src="http://www2.autoimg.cn/newsdfs/g8/M11/1D/64/40x0_0_autohomecar__wKgHz1i1Q_mAYbksAABSXj84qt4395.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_5314.html#pvareaid=102628">陈浩</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">责任编辑</div>
			        </li>
                
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_5868.html#pvareaid=102628"><img src="http://www3.autoimg.cn/newsdfs/g19/M13/91/F9/40x0_0_autohomecar__wKgFWFdrORWAXY15AABt_tkqweE990.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_5868.html#pvareaid=102628">张晓丹</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_5927.html#pvareaid=102628"><img src="http://www2.autoimg.cn/newsdfs/g12/M0B/A0/B3/40x0_0_autohomecar__wKjBy1gsNDOAVOnoAABzAbQ1vn8807.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_5927.html#pvareaid=102628">刁昊</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_6103.html#pvareaid=102628"><img src="http://www2.autoimg.cn/newsdfs/g12/M0A/72/B7/40x0_0_autohomecar__wKgH4lf8mmaAcLdHAABtEXGkyjw380.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_6103.html#pvareaid=102628">吴昱晨</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_6191.html#pvareaid=102628"><img src="http://www3.autoimg.cn/newsdfs/g20/M01/6C/49/40x0_0_autohomecar__wKgFVFkLzPOAIeFwAABVF9Qm2fw900.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_6191.html#pvareaid=102628">李长宁</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="http://www.autohome.com.cn/ExpertBlog/editor_6263.html#pvareaid=102628"><img src="http://www2.autoimg.cn/newsdfs/g22/M06/73/32/40x0_0_autohomecar__wKjBwVl1wpyAbMQvAABraWL6Mpg740.jpg"></a>
				        <div class="editorname"><a href="http://www.autohome.com.cn/ExpertBlog/editor_6263.html#pvareaid=102628">王梓冰</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
		</ul>
		<div class="fn-clear"></div>
	</div>
</div>

                    <!--编辑博客结束-->
                    <!-- 平安车险入口 -->
				    <div class="advbox monkey monkey_box">
                      <a href="http://baoxian.autohome.com.cn/manage/insurance/detail?type=2#pvareaid=2023288" target="_blank"><img src="http://x.autoimg.cn/www/index/2016/images/pingan-in-pic-new.png" alt=""></a>
                      <div class="monkey__icon"></div>
                    </div>
                    
                    <!--合作媒体开始-->
					
<div class="coo-media">
	<div class="hot-title">合作媒体报道<a class="hot-more" href="http://www.autohome.com.cn/list/c131-1.html">更多&gt;&gt;</a></div>
	<div class="hot-article-wrap">
		<ul>
			<li>
				<h2><a href="/news/201503/863334.html#pvareaid=103490">[北京晚报] 超7成消费者望提高燃油标准</a></h2>
				<a href="/news/201503/863334.html#pvareaid=103490"><img src="http://www2.autoimg.cn/newsdfs/g13/M07/A2/F0/120x90_0_autohomecar__wKgH1FgyrQeAaiznAACOtcnYVA8629.jpg"></a>
				<p class="hot-intro">近日，笼罩在北京乃至我国整个中东部地区的雾霾再次成为大家热议的话题，“雾霾”、“PM2.5...</p>
			</li>
		</ul>
		<div class="media-abstract">
            
                <p><a href="/news/201503/863329.html#pvareaid=103490">[山东商报]雾霾问题到底该不该怨私家车</a></p>
            
                <p><a href="/news/201503/863327.html#pvareaid=103490">[新闻晨报]超7成用户希望提高燃油标准</a></p>
            
                <p><a href="/news/201503/841974.html#pvareaid=103490">【金陵晚报】新车年检政策你了解多少</a></p>
            
		</div>
    </div>
</div>

                    <!--合作媒体结束-->
                    
				</div>
			</div>
		</div>
        <div data-toggle="gotop" class="gotop02" style="bottom: 10px;">
			<a class="gotop02-con" href="http://www.autohome.com.cn/bug/default.aspx">
				<i class="icon16 icon16-book3"></i>
				<span>意见反馈</span>
			</a>
		    <a data-gotop="true" data-scroll="true" class="gotop02-con" href="javascript:void(0);" style="display: none;">
			    <i class="icon16 icon16-top"></i>
			    <span>返回顶部</span>
		    </a>
		</div>
	</div>
   
    <style type="text/css">
/***汽车之家 - 公共底部版权***/
	.footer_auto{ width:990px; margin:10px auto 0 auto; padding:7px 0 10px 0; border-top:3px solid #3b5998; text-align:center; color:#7c7c7c; font-size:12px;}
	.footer_auto p{ line-height:24px; margin:0; padding:0;}
	.footer_auto p a{ display:inline-block; margin:0 9px;}
	.footer_auto p a.footimg{ border:1px solid #c2c2c2; margin:5px 5px 0 5px;}
	.footer_auto p a.footimg img{ border:0;}
	.footer_auto p .fline{ color:#bfbfbf; margin:0 3px;}
	.footer_auto p .footarial{ font-family:Arial, Helvetica, sans-serif;}

	.footer_auto .footios,.footer_auto .footand,.footer_auto .footwp,.footer_auto .footphone,.footer_auto .footauto{ display:inline-block; padding-left:19px; background:url(//x.autoimg.cn/news/footicon2.png) no-repeat;}
	.footer_auto .footios{ background-position:0 3px;}
	.footer_auto .footand{ background-position:0 -27px;}
	.footer_auto .footwp{ background-position:0 -57px;}
	.footer_auto .footphone{ background-position:0 -87px;}
	.footer_auto .footauto{ padding:0 22px 0 21px; background-position:0 -117px;}

	.footer_auto p a:link,.footer_auto p a:visited{ color:#7c7c7c; text-decoration:none;}
	.footer_auto p a:hover{ color:#d60000; text-decoration:none;}

</style>
    
<div style="clear:both;"></div>
<div class="footer_auto">
	<p>
		<a href="//www.autohome.com.cn/about/index.htm" target="_blank">关于我们</a><a href="//www.autohome.com.cn/about/lianxi.htm" target="_blank">联系我们</a><a href="http://autohome.hirede.com/" target="_blank">招贤纳士</a><span class="fline">|</span><a class="footios" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">iPhone客户端</a>/<a href="//app.autohome.com.cn/apps/main/1.html" target="_blank">iPad客户端</a><a class="footand" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">Android客户端</a><a class="footwp" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">WP客户端</a><a class="footphone" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">手机版</a><span class="fline">|</span><a class="footauto" href="http://weibo.com/qichezhijia" target="_blank">汽车之家</a><span class="fline">|</span><a href="//www.autohome.com.cn/bug/default.aspx" target="_blank">意见反馈</a>
        <script type="text/javascript">
                    var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");
                    document.write(unescape("%3Cspan id='cnzz_stat_icon_1262640694'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s19.cnzz.com/z_stat.php%3Fid%3D1262640694%26show%3Dpic1' type='text/javascript'%3E%3C/script%3E"));
        </script>
	</p>
	<p>
		<span class="footarial" id="footarial">&copy; 2004-2016 www.autohome.com.cn All Rights Reserved.</span> 汽车之家 版权所有
	</p>
</div>
<script type="text/javascript">
    var __myDate = new Date();
    var __year = __myDate.getFullYear();
    document.getElementById("footarial").innerHTML = '&copy; 2004-' + __year + ' www.autohome.com.cn All Rights Reserved.';
</script><!-- update 8/28/2017 9:48:04 AM r:utf-8 s:utf-8 -->
<!-- hit cache 2017/8/28 9:48:10 Unicode (UTF-8)-->
</body>
    <script type="text/javascript" src="http://x.autoimg.cn/as/js-1.0.5/sea.js"></script>
    <script type="text/javascript" src="http://sou.autohome.com.cn/js/SouSeriesAndSpec_130708.js?v1"></script>
    <!--[if IE 6]><script type="text/javascript">
    seajs.use(['jquery'],function($){
	    $('.news-item .focusimg,.news-item .focusimg-bt').mouseenter(function(){
		    $('.news-item .focusimg-bt-left,.news-item .focusimg-bt-right').show();
	    });
	    $('.news-item .focusimg').mouseleave(function(){
		    $('.news-item .focusimg-bt-left,.news-item .focusimg-bt-right').hide();
	    });
    });
    </script><![endif]-->


    <script type="text/javascript">
        seajs.config({version: "201402281736",alias: {'articlereply': 'http://x.autoimg.cn/www/common/js/articlereply.js'}});
       
        seajs.use(["jquery", "focus", "articlereply","gotop"], function ($, focus, articlereply) {
            $('#focus-1').focus({anim: true,keyboard: true,interval: 7000,pause: 'hover'});
            $('#focus-1 li.clone').removeAttr('id');
  
            //搜索js
            var brands='卡罗拉,科鲁兹,新君威,瑞虎3,速腾,新君越,福克斯,POLO,朗逸,景程,蒙迪欧-致胜,风云2,A3,奔腾B50';var ite=brands.split(',');$('#q').val(ite[Math.floor(Math.random()*ite.length)]);$("#q").blur(function(){if($('#q').val()=="")$('#q').val(ite[Math.floor(Math.random()*ite.length)])});$("#q").on("focus",function(){$(this).val("")});function tagContent(){$.ajax({type:"Get",url:"http://www.autohome.com.cn/ashx/channel/EditorBlogSwith.ashx?timestamp="+Math.random(),success:function(data){$("#tagInfo").html(decodeURIComponent(data))}})};$("#switchByRan").click(function(){tagContent()});
            //导航栏浮动
            $(function(){var win=$(window),nav=$('#ulNav'),lastTop=win.scrollTop(),isIE6=!!window.ActiveXObject&&!window.XMLHttpRequest,up=false,navTop=155,wtop,timer;win.scroll(function(){timer&&clearTimeout(timer);timer=setTimeout(function(){wtop=win.scrollTop();if(lastTop==wtop){return}up=lastTop>wtop?true:false;lastTop=wtop;if(up&&wtop>navTop){nav.addClass('navFixed');isIE6&&nav.css('top',wtop)}else{nav.removeClass('navFixed');isIE6&&nav.css('top',0)}},13)})});
        
            //二级分类导航左右滚动
            $.fn.switchNavgation = function () {
                return this.each(function () {
                    var $parent = this,
                        $left=$('#left',$parent),
                        $right=$('#right',$parent),
                        $ul = $('.div-fouc-tx ul', $parent);
                    if ($ul.size() == 1) return;
                    var tab = function ($elem, type) {
                        $elem[type]().animate({
                            'opacity': 1
                        },
                            400,
                            function () {
                                $(this).css({
                                    'zIndex': 20,
                                    'filter': 'alpha(opacity=100)'
                                }).addClass('fouc-current');
                            });
                        $elem.animate({
                            'opacity': 0
                        },
                            0,
                            function () {
                                $(this).css('zIndex', 10).removeClass('fouc-current');
                            });
                        type == 'prev' ? $('a', $right).removeClass('disabled') : $('a', $left).removeClass('disabled');
                        if ($elem[type]()[type]().size() == 0) {
                            type == 'prev' ? $('a', $left).addClass('disabled') : $('a', $right).addClass('disabled');
                        }
                    };
                    $left.on('click',
                        function () {
                            var $now = $('ul.fouc-current', $parent);
                            if ($now.prev().size() > 0) {
                                tab($now, 'prev');
                            }
                        });
                    $right.on('click',
                        function () {
                            var $now = $('ul.fouc-current', $parent);
                            if ($now.next().size() > 0) {
                                tab($now, 'next');
                            }
                        });
                    $ul.each(function (i) {
                        if (i == 0) {
                            $(this).css({
                                'opacity': 1,
                                'zIndex': 20,
                                'filter': 'alpha(opacity=100)'
                            }).addClass('fouc-current');
                        } else {
                            $(this).css({
                                'opacity': 0,
                                'zIndex': 10
                            });
                        }
                    });
                });
            };

            
                $('.div-fouc').switchNavgation();
            

            var channelClassId=0,curPage=1,excptArtIds='906087,906208,906246';
            function getQueryString(name) {
                var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
                var r = window.location.search.substr(1).match(reg);
                if (r != null) {
                    return unescape(r[2]);
                }
                return null;
            }
            var p=getQueryString("p");
            if(p)
            {
                $('#div-fouc-tx li').removeClass("current");
                window.location.hash="liststart";
                window.location = window.location;
            }

            
           
            function setPage(container, count, pageindex) {
                if(count==1)
                {
                    return;
                }
                var container = container;
                var count = count;
                var pageindex = pageindex;
                var a = [];
                //总页数少于10 全部显示,大于10 显示前3 后3 中间3 其余....
                if (pageindex == 1) {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-prev page-disabled\">上一页</a>";
                } else {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-prev\">上一页</a>";
                }
                function setPageList() {
                    if (pageindex == i) {
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"current\">" + i + "</a>";
                    } else {
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\">" + i + "</a>";
                    }
                }
                //总页数小于10
                if (count <= 10) {
                    for (var i = 1; i <= count; i++) {
                        setPageList();
                    }
                }
                    //总页数大于10页
                else {
                    if (pageindex <= 4) {
                        for (var i = 1; i <= 5; i++) {
                            setPageList();
                        }
                        a[a.length] = "<span class=\"page-item\">...</span><a href=\"javascript:void(0);\" target=\"_self\">" + count + "</a>";
                    } else if (pageindex >= count - 3) {
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\">1</a><span class=\"page-item\">...</span>";
                        for (var i = count - 4; i <= count; i++) {
                            setPageList();
                        }
                    }
                    else { //当前页在中间部分
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\">1</a><span class=\"page-item\">...</span>";
                        for (var i = pageindex - 2; i <= pageindex + 2; i++) {
                            setPageList();
                        }
                        a[a.length] = "<span class=\"page-item\">...</span><a href=\"javascript:void(0);\" target=\"_self\">" + count + "</a>";
                    }
                }
                if (pageindex == count) {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-next page-disabled\">下一页</a>";
                } else {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-next\">下一页</a>";
                }
                container.html( a.join(""));
                //事件点击
                var pageClick = function() {
                    var oAlink = container.children("a");
                    var temp=0;
                    var inx = pageindex; //初始的页码
                    oAlink[0].onclick = function() { //点击上一页
                        if (inx == 1) {
                            return false;
                        }
                        inx--;
                        curPage = inx;
                        setPage(container, count, inx);
                        $.fn.AjaxChannelArticles(channelClassId,curPage);
                        return false;
                    }
                    for (var i = 1; i < oAlink.length - 1; i++) { //点击页码
                        oAlink[i].onclick = function() {
                            inx = parseInt(this.innerHTML);
                            curPage =inx;
                            setPage(container, count, inx);
                            $.fn.AjaxChannelArticles(channelClassId,curPage);
                            return false;
                        }
                    }
                    oAlink[oAlink.length - 1].onclick = function() { //点击下一页
                        if (inx == count) {
                            return false;
                        }
                        inx++;
                        curPage =inx;
                        setPage(container, count, inx);
                        $.fn.AjaxChannelArticles(channelClassId,curPage);
                        return false;
                    }
                } ()
            }


            $.fn.AjaxChannelArticles=function(classId)
            {
                var html='<ul class="article">';
                $.get('http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page='+curPage+'&ExcptArtIds='+excptArtIds+'&class2Id='+classId,function(o){
                    o = eval("("+o+")");
                    if(o[0].Article==undefined)
                    {
                        $("#auto-channel-lazyload-article").empty();
                        $("#btnLoading").hide();
                        $("#channelPage").hide();
                        return;
                    }
                    for (var i = 0; i < o[0].Article.length; i++) {
                        html+="<li><a href=\"http://www.autohome.com.cn"+o[0].Article[i].Dir+o[0].Article[i].PublishTime+"/"+o[0].Article[i].Id+(o[0].Article[i].SerializeStartPage==1?"":"-"+o[0].Article[i].SerializeStartPage)+".html#pvareaid=102624\"><div class=\"article-pic\"><img src=\""+o[0].Article[i].Img+"\"></div><h3>"+o[0].Article[i].Title+"</h3><div class=\"article-bar\"><span class=\"fn-left\">"+o[0].Article[i].ShowTime+"</span><span class=\"fn-right\"><em><i class=\"icon12 icon12-eye\"></i>"+o[0].Article[i].ClickCountStr+"</em><em data-articleid=\""+o[0].Article[i].Id+"\" data-class=\"icon12 icon12-infor\"><i class=\"icon12 icon12-infor\"></i>0</em></span></div><p>"+o[0].Article[i].Summary+"</p></a></li>";
                    }
                    html+='</ul>';
                    $('#auto-channel-lazyload-article').html(html);
                    var count=1;
                    if(o[0].Total>60)
                    {
                        count=(o[0].Total-60)%15==0?parseInt((o[0].Total-60)/15+1):parseInt((o[0].Total-60)/15+2);
                    }
                    else
                    {
                        count=1;//(o[0].Total)%15==0?parseInt((o[0].Total)/15):parseInt((o[0].Total)/15+1);
                    }
                    if(count==1)
                    {
                        $("#channelPage").hide();
                        $("#btnLoading").hide();
                    }
                    else
                    {
                        $("#channelPage").show();
                        $("#btnLoading").show();
                    }
                    $("#btnLoading").hide();
                    setPage($('.page'),count,curPage);
                    $(function () {
                        var objs = $("[data-articleid]");
                        var ids = [];

                        for (var i = 0; i < objs.length; i++) {
                            ids.push($(objs[i]).attr('data-articleid'));
                        }

                        if (ids.length > 0) {
                            $.ajax({
                                type: "get",
                                cache: false,
                                url:"http://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?appid=1&dateType=jsonp&objids=" + ids.join('.'),
                                dataType: "jsonp",
                                success: function (data) {
                                    if (data == undefined || data.commentlist == null || data.commentlist.length == 0)
                                        return;

                                    var list = data.commentlist;
                                    for (var i = 0; i < list.length; i++) {
                                        var item = list[i];
                                        for (var j = 0; j < objs.length; j++) {
                                            var obj = $(objs[j]);
                                            if (obj.attr('data-articleid') == item.objid)
                                                obj.html('<i class="' + (obj.attr('data-class') ? obj.attr('data-class') : "icon icon-infor") + '"></i>' + item.replycountall);
                                        }
                                    }
                                }
                            });
                        }
                    });
                });
                window.location.hash="liststart";
                window.location = window.location;
            }

            //loazyLoadArticles
            $('#div-fouc-tx [data-toggle="tab"]').on('click', function () {
                var _this = this;
                //var liList =$('#div-fouc-tx [data-toggle="tab"]');
                //var length=liList.length;
                //for (var i = 0; i < length; i++) {
                //    if(_this==liList)
                //    {
                //        $(_this).addClass("current");
                //        break;
                //    }else
                //    {
                //        $(liList[i]).removeClass();
                //    }
                //}
                $("h3.h3cur").removeClass("h3cur");
                $('#div-fouc-tx li').removeClass("current");
                $(_this).parent().addClass("current");
                var classId=_this.getAttribute('data-class');
                channelClassId = classId;
                //tab切换时 改成默认第一页
                curPage=1;
                $.fn.AjaxChannelArticles(classId,curPage);

                //ar.init('auto-index-lazyload-article');
                //autoIndexObj.lazyloadImages($(_this).attr('data-target').replace('#', ''));
               
            });

            var class2Id =0;
            if(class2Id!=0)
            {
                var liList=$('#div-fouc-tx [data-toggle="tab"]');
                var length =liList.length;
                for (var i = 0; i < length; i++) {
                    if(liList[i].getAttribute('data-class')==class2Id)
                    {
                        $(liList[i]).addClass('current');
                        break;
                    }
                }
            }

        });
        //懒加载
        Function.prototype.bind=function(bindObj,args){var _self=this;return function(){return _self.apply(bindObj,[].concat(args))}};Object.extend=function(destination,source){for(var property in source){destination[property]=source[property]}return destination};seajs.config({version:"1394506138411"});seajs.use(["jquery"],function($){function LazyLoad(args){this.areaList=args;Object.extend(this,args);this.init()}LazyLoad.prototype={getClient:function(){var l,t,w,h;l=document.documentElement.scrollLeft||document.body.scrollLeft;t=document.documentElement.scrollTop||document.body.scrollTop;w=document.documentElement.clientWidth;h=document.documentElement.clientHeight;return{'left':l,'top':t,'width':w,'height':h}},getSubClient:function(p){var l=0,t=0,w,h;w=p.offsetWidth;h=p.offsetHeight;while(p.offsetParent){l+=p.offsetLeft;t+=p.offsetTop;p=p.offsetParent}return{'left':l,'top':t,'width':w,'height':h}},intens:function(rec1,rec2){var lc1,lc2,tc1,tc2,w1,h1;lc1=rec1.left+rec1.width/2;lc2=rec2.left+rec2.width/2;tc1=rec1.top+rec1.height/2;tc2=rec2.top+rec2.height/2;w1=(rec1.width+rec2.width)/2;h1=(rec1.height+rec2.height)/2;return Math.abs(lc1-lc2)<w1&&Math.abs(tc1-tc2)<h1},autoCheck:function(){var prec1=this.getClient();var prec2;for(var i=this.areaList.length-1;i>=0;i--){var d=document.getElementById(this.areaList[i]);if(d){prec2=this.getSubClient(d);if(this.intens(prec1,prec2)){this.execLoad(d);delete this.areaList[i]}}}},execLoad:function(obj){},init:function(){var _this=this;_this.autoCheck();if(window.addEventListener){window.addEventListener("scroll",_this.autoCheck.bind(_this),false);window.addEventListener("resize",_this.autoCheck.bind(_this),false)}else if(window.attachEvent){window.attachEvent("onscroll",_this.autoCheck.bind(_this));window.attachEvent("onresize",_this.autoCheck.bind(_this))}}};var pageIndex=2,pageCount=3775,objLoading=$("#btnLoading"),objArticle=$("#articleList");var temp=0;$(".page").hide();var _lazy=new LazyLoad({areaList:[],execLoad:function(obj){setTimeout(function(){$(".article-wrapper ul").eq(pageIndex-1).show(0,function(){pageIndex++;if(pageIndex>4){$(".page").show();objLoading.hide()}else{_lazy.areaList.push('btnLoading');$(".article-wrapper ul").eq(pageIndex-1).show();if(pageCount<=4){objLoading.hide()}}})},150)}});$(function(){var Anchor=window.location.hash;if(Anchor.length>0){var artId=Anchor.substring(Anchor.indexOf('=')+1,Anchor.length);$('[data-artIdAnchor]').each(function(index,item){if(artId==$(item).attr('data-artIdAnchor')){var pager=parseInt(index/15,10);if(index%15>0)pager+=1;pageIndex=pager+1;$(".article-wrapper ul:lt("+(pager)+")").show();$(".article-wrapper ul").eq(pager).show(0,function(){$(window).scrollTop($(item).offset().top)})}})}pageIndex<=4&&1==1&&objLoading.show()&&_lazy.areaList.push('btnLoading');pageIndex>4&&$(".page").show()})});
    </script>
    
   

    <script language="javascript" type="text/javascript">
        var pvTrack = function(){};
        pvTrack.site = 1;
        pvTrack.category = 401;
        pvTrack.subcategory = 2151;
        pvTrack.object = 0;
        pvTrack.series = 0;
        pvTrack.type = 0;
        pvTrack.typeid = 0;
        pvTrack.spec = 0;
        pvTrack.level = 0;
        pvTrack.dealer = 0;
    </script>
    <script type="text/javascript">
    (function(doc){
        var _as = doc.createElement('script');
        _as.type = 'text/javascript';
        _as.async = true;
        _as.src = '//x.autoimg.cn/bi/mda/ahas_body.min.js?d=' + (new Date()).toLocaleDateString().replace(/\//g, "");
        var s = doc.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(_as, s);
    })(document);
</script>
<SCRIPT language=javascript type=text/javascript>
var url_stats="//stats.autohome.com.cn/pv_count.php?SiteId=";
(function (){
    if (typeof(pvTrack)!="undefined"){				
		setTimeout("func_stats()",3000);		
		var doc = document,t=pvTrack;
		var pv_site,pv_category ,pv_subcategory,pv_object,pv_series,pv_type,pv_typeid,pv_spec,pv_level,pv_dealer,pv_ref,pv_cur;
		pv_ref=escape(doc.referrer);pv_cur=escape(doc.URL);
		pv_site=t.site;pv_category=t.category ;pv_subcategory= t.subcategory;pv_object=t.object;pv_series=t.series;pv_type=t.type;pv_typeid=t.typeid;pv_spec=t.spec;pv_level=t.level;pv_dealer=t.dealer;
		url_stats+= pv_site+(pv_category != null ? "&CategoryId=" + pv_category : "")+ (pv_subcategory != null ? "&SubCategoryId=" + pv_subcategory : "")+ (pv_object != null ? "&objectid=" + pv_object : "")+ (pv_series != null ? "&seriesid=" + pv_series : "")+ (pv_type != null ? "&type=" + pv_type : "")+ (pv_typeid != null ? "&typeid=" + pv_typeid : "")+ (pv_spec != null ? "&specid=" + pv_spec : "")+ (pv_level != null ? "&jbid=" + pv_level : "")+ (pv_dealer != null ? "&dealerid=" + pv_dealer : "")+ "&ref=" + pv_ref + "&cur=" + pv_cur+"&rnd="+Math.random();
		var len_url_stats =url_stats.length;
		}
})();
//document.write('<iframe id="PageView_stats" src="" style="display:none;"></iframe>');
function func_stats(){
	var image=new Image();
	image.src=url_stats;
//document.getElementById('PageView_stats').src =url_stats;
}
</SCRIPT>
<script type='text/javascript'>
  var _ahs = _ahs || {};
  window._ahs = _ahs;
  (function() {
  if (typeof(pvTrack) !== "undefined") {
  _ahs['site'] = pvTrack['site'];
  _ahs['category'] = pvTrack['category'];
  _ahs['subcategory'] = pvTrack['subcategory'];
  }
  var ahs = document.createElement('script');
  ahs.type='text/javascript';
  ahs.async = true;
  ahs.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'x.autoimg.cn/bi/risk/ah_fp.min.js';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(ahs, s);
  })();
</script>
<script type='text/javascript'>
    var _ahs = _ahs || {};
    window._ahs = _ahs;
    (function () {
        if (typeof (pvTrack) !== "undefined") {
            _ahs['site'] = pvTrack['site'];
            _ahs['category'] = pvTrack['category'];
            _ahs['subcategory'] = pvTrack['subcategory'];
        }
        var ahs = document.createElement('script');
        ahs.type = 'text/javascript';
        ahs.async = true;
        ahs.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'x.autoimg.cn/bi/risk/ah_fp.min.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ahs, s);
    })();
</script>
    <script type="text/javascript" src="http://x.autoimg.cn/engine/root/fggxl.js?2015v1"></script>
    
          <script type="text/javascript"> _aad.Loader('2823,904,2851,2852,907,908,909,910,911,912','155');</script>
    
</html>"""
soup = BeautifulSoup(html,'html.parser')
li_list = soup.find(id='auto-channel-lazyload-article').find_all(name='li')
for li in li_list:
    title = li.find('h3')
    if not title:
        continue

    summary = li.find('p').text


    # li.find('a').attrs,字典
    # li.find('a').attrs['href'],字典
    url = li.find('a').get('href')

    img = li.find('img').get('src')
    print(title.text, url,summary,img)

    res = requests.get(img)
    file_name = "%s.jpg" %(title,)
    with open(file_name,'wb') as f:
        f.write(res.content)








