Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a05:6520:4581:b029:9e:2c6b:28d9 with SMTP id s1csp1798165lkv;
        Sun, 6 Dec 2020 09:04:07 -0800 (PST)
X-Google-Smtp-Source: ABdhPJyQw4gdf3UPI5POypeqgzNk30r9N/WZDXGZAcB5Gzf850wxR4EIEVqnB9NA8xfH5NT5u5xZ
X-Received: by 2002:ac8:5b86:: with SMTP id a6mr19463216qta.41.1607274247280;
        Sun, 06 Dec 2020 09:04:07 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1607274247; cv=none;
        d=google.com; s=arc-20160816;
        b=IPwKRVTwW56yLMlXLZHWZ8KHaGS7W0K0kRyT2RZw8DjFMRTU/25RRCdGMc77Y3rTFV
         Pt4bldjlLAyN17RYLf0pwJZnmYDtA05nz5pDYt7/+kQvetJ5S1VLeV01yPfkzBSic+MM
         DwI9x+QLZQ1fX3KePVNwOZZL+2UrdW1HuhTm3ctVUXocwJ0t/PnXpeiRmdSrvs2C7RdG
         R0JbSypikgDxFxSO0HNcA3dOqRV4vwHaZSS8lvBHy9dRnRFsb1jyGYIVf49zmxeeWaXD
         mbsEynot+/LW/w6VFGPDwZ/jEp7eXBn3s2qj0fWXyNLkfH4Sab0hZM3UIfpMMnBfp5BH
         +BaA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=D7l/q9SZ7+X6s53m2fwYmGE6WoXjpo0uJPJrUAWqa4s=;
        b=PLcsj0aE7HKvImYVkk2G6cRhDmAsPNcOrhWPeBzzeV5x1z6hNrlsW9cZqaIb0cR7Mx
         5pIR47+ve1CTYoRvgmIy7qyMjgav44+NWflptsVLZixhZV6GQo62gXEyxDG+p5tpZ0cv
         tqjMnBBX9IVnMPZhMd3O7U+Z/5+4yfHhz2HoEw8GN/VvazfSo5+cl53zWY28T41Czt53
         27FQOCsUc5YtFqrH34vhW6RszkXfdJL+H/YDHUiO5X+1xXu6OFU+fVYiYuYveKeMPAVf
         TWE+9bYBijhNDhlX9lfibUL+Qbt2FcUWx19bOykizCynZJ26yxeOIXKVmRcVJZh5ldfr
         WmZQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=dDmOKQqM;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=NSOphGWW;
       spf=pass (google.com: domain of 010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@amazonses.com
Return-Path: <010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id u64si6552384qka.20.2020.12.06.09.04.06
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Sun, 06 Dec 2020 09:04:07 -0800 (PST)
Received-SPF: pass (google.com: domain of 010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=dDmOKQqM;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=NSOphGWW;
       spf=pass (google.com: domain of 010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1607274246;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=n5eIz/+8G96zNbfskYKcLXge/HKbRmPRmAd1+zaLuYY=;
	b=dDmOKQqMu2qPGJFRyHhMBFy406drTW/vnZdwDF2OL4Z/9Fn12fxvVNi9Dya1H7pk
	qwe7x2XcmIRNWqqJI4Jxm82wy/90jhicGZSMiufH9fTqw1sXI7CpDanTfx2FJrZKdi8
	DQYsVHrasYL0lMOKukYjRFB04yrL0A9A98xxn8QU=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1607274246;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=n5eIz/+8G96zNbfskYKcLXge/HKbRmPRmAd1+zaLuYY=;
	b=NSOphGWWspwWQSWeyvf5JLWKMjxD754o2zILfhK/2Wr5sd9bausBcPRggD4W+9aj
	Vz7l+om5I+u3tRT8gWJfYhQ0yBzPU6m6pOwQURaJVuiDg1i79qTsa6eSToT4QDVWwEC
	c8/WyGA3RsTshpX21SmNPEqhW/tOcvhdasVYsW+4=
Content-Type: multipart/alternative;
 boundary="--_NmP-e1c3a957119a25a9-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #286 [Hard] 
Message-ID: <010001763902b00a-725e1d02-969c-4dc8-a839-775491ba5417-000000@email.amazonses.com>
Date: Sun, 6 Dec 2020 17:04:06 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.12.06-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-e1c3a957119a25a9-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by VMware.

The skyline of a city is composed of =
several buildings of various widths and
heights, possibly overlapping one =
another when viewed from a distance. We can
represent the buildings using =
an array of (left, right, height) tuples, which
tell us where on an =
imaginary x-axis a building begins and ends, and how tall it
is. The skyline itself can be described by a list of (x, height) tuples, =
giving
the locations at which the height visible to a distant observer =
changes, and
each new height.

Given an array of buildings as described =
above, create a function that returns
the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, =
11,
5), (19, 23, 4)]. In aggregate, these buildings would create a skyline =
that
looks like the one below.=20

     ______ =20
    |      |        ___
 ___|      |___    |   |=20
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------


As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0)=
, (19,
4), (23, 0)].


----------------------------------------------------=
----------------------------

Upgrade to premium
[https://www.=
dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%40gmail.=
com]=20
and get in-depth solutions to every problem, including this one.=20

If you liked this problem, feel free to forward it along so they can =
subscribe
here [https://www.dailycodingproblem.com/]! As always, shoot us =
an email if
there's anything we can help with!


--------------------------=
------------------------------------------------------

Master algorithms together on Binary Search [https://binarysearch.io/?=
ref=3Ddcp].
Create a room, invite your friends, and race to finish the =
problem!


----------------------------------------------------------------=
----------------

No more? Snooze or unsubscribe
[https://dailycodingproble=
m.com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b=
8f89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-e1c3a957119a25a9-Part_1
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.=
w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns=3D"http://www.w3=
.org/1999/xhtml">
  <head>
    <meta name=3D"viewport" =
content=3D"width=3Ddevice-width, initial-scale=3D1.0">
    <meta http-equiv=3D"Content-Type" content=3D"text/html; =
charset=3DUTF-8">
    <title>Daily Coding Problem: Problem #286 [Hard]
</title>
    <style type=3D"text/css" rel=3D"stylesheet" media=3D"all">
@media only screen and (max-width: 600px) {
  .email-body_inner,
.email-footer {
    width: 100% !important;
  }
}
@media only screen and =
(max-width: 500px) {
  .button {
    width: 100% !important;
  }
}
</style>
  </head>
  <body style=3D"height: 100%; margin: 0; line-height: 1.4; =
background-color: #F2F4F6; color: #74787E; -webkit-text-size-adjust: none; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box; width: 100%;">
    <table class=3D"email-wrapper" =
width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 100%; margin: 0; padding: 0; -premailer-width: 100%; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; background-color: =
#F2F4F6;" bgcolor=3D"#F2F4F6">
      <tr>
        <td align=3D"center" =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
          <table =
class=3D"email-content" width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; width: 100%; margin: 0; padding: 0; =
-premailer-width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: =
0;">
            <table class=3D"email-head_inner" align=3D"center" =
width=3D"570" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 570px; margin: 0 auto; padding: 0; -premailer-width: 570px; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0;">
              <tr>
                <td class=3D"email-masthead" style=3D"word-break: =
break-word; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; padding: 25px 35px; height: 30px; vertical-align: =
middle; border-collapse: collapse;" height=3D"30" valign=3D"middle">
                  <a href=3D"https://www.dailycodingproblem.com/" =
class=3D"email-masthead_logo_link" style=3D"color: #3869D4; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 30px; height: 30px; vertical-align: middle; text-decoration: none; =
padding: 0; margin: 0; display: inline-block;">
                    <img =
class=3D"email-masthead_logo" src=3D"https://www.dailycodingproblem.=
com/static/icon-round.png" width=3D"30" height=3D"30" style=3D"font-family:=
 Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 30px; height: 30px; border: 0; vertical-align: middle;">
                  </a>
                  <a href=3D"https://www.=
dailycodingproblem.com/" class=3D"email-masthead_link" style=3D"color: =
#3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; height: 30px; vertical-align: middle; padding-left:=
 6px; text-decoration: none;">
                    <span =
class=3D"email-masthead_name" style=3D"font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box; font-size: 14px; =
font-weight: bold; color: #343434; text-decoration: none; text-shadow: 0 =
1px 0 white; height: 50px;">Daily Coding Problem</span>
                  </a>
                </td>
              </tr>
            </table>
            <!-- Email Body -->
            <tr>
              <td class=3D"email-body" width=3D"100%" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"word-break: break-word; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; width: =
100%; margin: 0; padding: 0; -premailer-width: 100%; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; border-top: 1px solid=
 #EDEFF2; border-bottom: 1px solid #EDEFF2; background-color: #FFFFFF;" =
bgcolor=3D"#FFFFFF">
                <table class=3D"email-body_inner" =
align=3D"center" width=3D"570" cellpadding=3D"0" cellspacing=3D"0" =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; width: 570px; margin: 0 auto; padding: 0; =
-premailer-width: 570px; -premailer-cellpadding: 0; -premailer-cellspacing:=
 0; background-color: #FFFFFF;" bgcolor=3D"#FFFFFF">
                  <!-- Body content -->
                  <tr>
                    <td class=3D"content-cell" style=3D"word-break: =
break-word; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; padding: 35px;">
											<p style=3D"margin-top:=
 0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Good morning! Here&#39;s your coding interview problem for =
today.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">This problem was asked by =
VMware.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">The skyline of a city is =
composed of several buildings of various widths and heights, possibly =
overlapping one another when viewed from a distance. We can represent the =
buildings using an array of <code style=3D"font-family: monospace; margin: =
0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">(left, right, =
height)</code> tuples, which tell us where on an imaginary x-axis a =
building begins and ends, and how tall it is. The skyline itself can be =
described by a list of <code style=3D"font-family: monospace; margin: 0 =
2px; padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">(x, height)</code> tuples, =
giving the locations at which the height visible to a distant observer =
changes, and each new height.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Given an =
array of buildings as described above, create a function that returns the =
skyline.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">For example, suppose the =
input consists of the buildings <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">[(0, 15, 3), (4, =
11, 5), (19, 23, 4)]</code>. In aggregate, these buildings would create a =
skyline that looks like the one below. </p>
<pre style=3D"background-color:=
 #f8f8f8; border: 1px solid #cccccc; font-size: 13px; line-height: 19px; =
overflow: auto; padding: 6px 10px; border-radius: 3px;"><code =
style=3D"border-radius: 3px; font-family: monospace; margin: 0; padding: 0;=
 white-space: pre; background: transparent; background-color: transparent; =
border: none;">     ______ =20
    |      |        ___
 ___|      |___    |   |=20
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------
</code></pre><p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">As a result, your function=
 should return <code style=3D"font-family: monospace; margin: 0 2px; =
padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">[(0, 3), (4, 5), (11, 3), =
(15, 0), (19, 4), (23, 0)]</code>.</p>
<hr style=3D"font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;"><a href=3D"https://www.=
dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%40gmail.com" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Upgrade to premium</a> and get =
in-depth solutions to every problem, including this one. </p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">If you liked this problem, feel free =
to forward it along so they can <a href=3D"https://www.dailycodingproblem.=
com/" style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">subscribe here</a>! As =
always, shoot us an email if there&#39;s anything we can help with!</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Master =
algorithms together on <a href=3D"https://binarysearch.io/?ref=3Ddcp" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Binary Search</a>. Create a room, =
invite your friends, and race to finish the problem!</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box; font-size: 0.7em;">
  No more? <a href=3D"https://dailycodingproblem.com/unsubscribe?=
unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b8f89172d630e6f6de6=
58c7d6d6b960ec" style=3D"color: #3869D4; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">Snooze or =
unsubscribe</a>.
</p>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
						<!-- Email Footer -->
						<tr>
              <td =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
                <table =
class=3D"email-footer" align=3D"center" width=3D"570" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"font-family: Arial, 'Helvetica Neue', Helvetica,=
 sans-serif; box-sizing: border-box; width: 570px; margin: 0 auto; padding:=
 0; -premailer-width: 570px; -premailer-cellpadding: 0; =
-premailer-cellspacing: 0; text-align: center;">
                  <tr>
                    <td class=3D"content-cell" align=3D"center" =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box; padding: 35px;">
                      <p class=3D"sub align-center" style=3D"margin-top: 0;=
 line-height: 1.5em; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box; text-align: center; color: #AEAEAE; =
font-size: 12px;">&copy; 2019 Daily Coding Problem. All rights reserved.=
</p>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
----_NmP-e1c3a957119a25a9-Part_1--
