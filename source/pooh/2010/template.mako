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
<link rel="stylesheet" type="text/css" href="${PATH('/css/2010.css')}"/>
<link rel="stylesheet" type="text/css" href="${PATH('/css/jquery.lightbox.css')}"/>
</%def>
</head>
<body>
<div class='header'>
    <div class='holder'>
        <div class='title'></div>
    </div>
</div>
<div class='main'>
    <div class='holder'>
        <div class='content'>
            <div class='menu'>
                <div class='menu_body'>
                    <div class='buttons'>
                        <a href='index.html'><div class='button'></div></a>
                        <a href='participants.html'><div class='button'></div></a>
                        <a href='organizers.html'><div class='button'></div></a>
                        <a href='programm.html'><div class='button'></div></a>
                        <a href='video.html'><div class='button'></div></a>
                        <a href='photo.html'><div class='button'></div></a>
                        <a href='where.html'><div class='button'></div></a>
                        <a href='contacts.html'><div class='button'></div></a>
                        <a href='feedback.html'><div class='button'></div></a>
                    </div>
                <div class='menu_end'></div>
                </div>
            </div>
        <div id='content'>${self.body()}</div>
        </div>
    </div>
</div>
<div class='footer'>
    <div class='holder'>
        <div class='copyright'></div>
    </div>
</div>
</body>
</html>