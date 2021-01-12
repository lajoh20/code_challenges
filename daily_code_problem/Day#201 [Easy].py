Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:55d0:0:0:0:0 with SMTP id z16csp495832ejp;
        Fri, 11 Sep 2020 08:50:34 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJwVZiiPo3SXJQh5XiL+DFqdh7YI0yeGjuDhAi3WVeesYF8FebRN5a7RAjT0jE72zU0AE7lU
X-Received: by 2002:a05:620a:65a:: with SMTP id a26mr1996336qka.424.1599839433897;
        Fri, 11 Sep 2020 08:50:33 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1599839433; cv=none;
        d=google.com; s=arc-20160816;
        b=xmsSbXIOHiV06fk7hjSjecrjguVngJ3UjFHQQ+II7SkDcoyheFSTEeZD7eKjlV62LN
         6AA2nqCLB3r+EmiasxB6rjt9uN6dBDwzvYsXCxPEXNfkrT9FnGA6hLz2ssLa5QiMuXve
         beAXo6usbqGGcz4tk09CxQvA3qEq8bZpcMydENWtIaGhZoHwaabpYEr/8N1WXNSSj+tJ
         D3LkBlhebTdF/IwXwhylLpdhDj2b6KdVOU6mKRlC1glv1/iQk9bWUSny83A/57pX3NPb
         aY/d0HgyqJsXdgiNAIFlzM6aUazP085MP4M0hVC1lysoDL/9CUCLtAdtgfn4DDbyInSD
         EHJQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=Wh4hk34NBTOMCVQgg1G//YyXxIbLzRa7ZaxacHfvjvY=;
        b=Wf4Pm7s5i81waesOBbR1AHJesExJhx7cLQhyjilDmnWoBHC7XXMUmZC7X2L7/Ncspb
         iSTNgd1qqvt4fs3J1xpC3yuPAGl02DK+qmQlr5A7Pj82XEKorUcqlHW+gVt3hZDf1143
         tS827Kr9jRV3s3SomkY7S1vhbUm33wbFjSiUTzzISCEej7FUObNnnwOT1KIqQuvc0idJ
         yrWLadwZk6ZmQIcLew5tcCdJ9ZC6t4AED1wIW7b9EIdFtEurSqZzOO2qoEj1SHJOwjNW
         tIbIj2dZ2dUU1ak8QQg9xVad6cEjobNK0VXOkRrIE8KIx8K4vt0u2XJ3+qPV/T8pi18z
         ewug==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=S0crzek7;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=AdJVO+Ue;
       spf=pass (google.com: domain of 010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@amazonses.com
Return-Path: <010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id i10si1488254qkl.119.2020.09.11.08.50.33
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 11 Sep 2020 08:50:33 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=S0crzek7;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=AdJVO+Ue;
       spf=pass (google.com: domain of 010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1599839433;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=sqAHT8il73wAjrNt5ORNKihJjrnSksUlBlHJhY+wEn8=;
	b=S0crzek7bvddRDuBNinW1meYK4ze3qHXEu0Hb5u407/8yA39Nvlken1Z6ucOplTO
	8WVlugGol5WuGSsUUWqi5SvMbSOy8sORx0xiySf0wA/oBeKSyJLsWtjwO95p2NO1JvM
	EkKxrGdrYSvSlHdIAyo0tZZiu6SzzyWPXVEc/y3Y=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1599839433;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=sqAHT8il73wAjrNt5ORNKihJjrnSksUlBlHJhY+wEn8=;
	b=AdJVO+UeMAWXHu3htoEh+8QBH/Ny18tILJHdH4VAV7ZExKY6fZtYzzFriJLzWibn
	a2O9edOGHC0Ibz9cZn791fAZQgA4qHIIUA/Uu0qmex8OMkpydhupIenoYSSmwCujI7/
	I7lnocdW7oq0VT3pgrhNUMv9rIemuKqJqOHNedxE=
Content-Type: multipart/alternative;
 boundary="--_NmP-7d5b94c6022e3a88-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #201 [Easy] 
Message-ID: <010001747ddc7212-f028d3bf-8459-462c-8a10-03b061778663-000000@email.amazonses.com>
Date: Fri, 11 Sep 2020 15:50:33 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.09.11-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-7d5b94c6022e3a88-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of arrays of =
integers, where each array corresponds to a
row in a triangle of numbers. =
For example, [[1], [2, 3], [1, 5, 1]] represents
the triangle:

  1
 2 3
1 5 1


We define a path in the triangle to start at the top and go down =
one row at a
time to an adjacent value, eventually ending with an entry on =
the bottom row.
For example, 1 -> 3 -> 5. The weight of the path is the sum=
 of the entries.

Write a program that returns the weight of the maximum =
weight path.


------------------------------------------------------------=
--------------------

Upgrade to premium
[https://www.dailycodingproblem.=
com/subscribe?email=3Dlewisjohnson1066334%40gmail.com]=20
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
----_NmP-7d5b94c6022e3a88-Part_1
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
    <title>Daily Coding Problem: Problem #201 [Easy]
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
Google.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">You are given an array of =
arrays of integers, where each array corresponds to a row in a triangle of =
numbers.
For example, <code style=3D"font-family: monospace; margin: 0 2px;=
 padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">[[1], [2, 3], [1, 5, =
1]]</code> represents the triangle:</p>
<pre style=3D"background-color: =
#f8f8f8; border: 1px solid #cccccc; font-size: 13px; line-height: 19px; =
overflow: auto; padding: 6px 10px; border-radius: 3px;"><code =
style=3D"border-radius: 3px; font-family: monospace; margin: 0; padding: 0;=
 white-space: pre; background: transparent; background-color: transparent; =
border: none;">  1
 2 3
1 5 1
</code></pre><p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">We define a path in the triangle to start at the top and go =
down one row at a time to an adjacent value, eventually ending with an =
entry on the bottom row. For example, 1 -&gt; 3 -&gt; 5. The weight of the =
path is the sum of the entries.</p>
<p style=3D"margin-top: 0; color: #555;=
 font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Write a =
program that returns the weight of the maximum weight path.</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><a =
href=3D"https://www.dailycodingproblem.com/subscribe?=
email=3Dlewisjohnson1066334%40gmail.com" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Upgrade to premium</a> and get in-depth solutions to every =
problem, including this one. </p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">If you =
liked this problem, feel free to forward it along so they can <a =
href=3D"https://www.dailycodingproblem.com/" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">subscribe here</a>! As always, shoot us an email if =
there&#39;s anything we can help with!</p>
<hr style=3D"font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Master algorithms together on <a =
href=3D"https://binarysearch.io/?ref=3Ddcp" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Binary Search</a>. Create a room, invite your friends, and =
race to finish the problem!</p>
<hr style=3D"font-family: Arial, 'Helvetica=
 Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; line-height: 1.5em; text-align: =
left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; font-size: 0.7em;">
  No more? <a =
href=3D"https://dailycodingproblem.com/unsubscribe?unsubscribeKey=3D15bb434=
5a533060b01c0f75abaabcc917938df8b8f89172d630e6f6de658c7d6d6b960ec" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Snooze or unsubscribe</a>.
</p>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
						<!-- Email Footer -->
						<tr>
              <td style=3D"word-break: break-word; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
                <table class=3D"email-footer" align=3D"center" =
width=3D"570" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 570px; margin: 0 auto; padding: 0; -premailer-width: 570px; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; text-align: center;">
                  <tr>
                    <td class=3D"content-cell" =
align=3D"center" style=3D"word-break: break-word; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; padding: =
35px;">
                      <p class=3D"sub align-center" =
style=3D"margin-top: 0; line-height: 1.5em; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box; text-align: center; =
color: #AEAEAE; font-size: 12px;">&copy; 2019 Daily Coding Problem. All =
rights reserved.</p>
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
----_NmP-7d5b94c6022e3a88-Part_1--
