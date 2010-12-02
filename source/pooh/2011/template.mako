<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
${self.head()}
<%def name="head()">
<title>Пух и все-все-все</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
<script type="text/javascript" src="${PATH('/js/jquery.js')}"></script>
<script type="text/javascript" src="${PATH('/js/jquery.lightbox.js')}"></script>
<link rel="stylesheet" type="text/css" href="${PATH('/css/2011.css')}"/>
<link rel="stylesheet" type="text/css" href="${PATH('/css/jquery.lightbox.css')}"/>
</%def>
</head>
<body>
<div class='main'>
    <div class='holder'>
        <div class='head'></div>
        <div class='buttons at_${self.page_id()}'>
                   <span class='btn_main_head'>
            </span><span class='btn_main'>
            </span><span class='btn_prog'>
            </span><span class='btn_video'>
            </span><span class='btn_photo'>
            </span><span class='btn_where'>
            </span><span class='btn_cont'>
            </span><span class='btn_cont_tail'>
            </span>
            <div class='links'>
                       <a href='index.html'><span class='link_main'>
                    Главная
                </span></a><a href='programm.html'><span class='link_prog'>
                    Программа
                </span></a><span class='link_video'>
                    Видео
                </span><span class='link_photo'>
                    Фото
                </span><a href='where.html'><span class='link_where'>
                    Как добраться?
                </span></a><a href='contacts.html'><span class='link_cont'>
                    Контакты
                </span></a>
            </div>
        </div>
        <div id='content'>${self.body()}</div>
        <div class='footer'></div>
    </div>
</div>
</body>
</html>