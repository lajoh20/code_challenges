Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:aa6:c3c3:0:b029:9b:dab3:97be with SMTP id b3csp3673388lkq;
        Mon, 23 Nov 2020 09:02:43 -0800 (PST)
X-Google-Smtp-Source: ABdhPJx78m1hjIbj0Wk1HVsa4UZngtVUvmv+QkpM7/HXzGwjOYp7I8O3whFyw9DhKlaffl93I1Xb
X-Received: by 2002:a37:66d4:: with SMTP id a203mr387864qkc.362.1606150962657;
        Mon, 23 Nov 2020 09:02:42 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1606150962; cv=none;
        d=google.com; s=arc-20160816;
        b=kV5FzH5dRgmxURHCa1flSo5h4xJl0dZ+FGUffNRbEtZ1sKexqbgDnDz/7SrbLT3z8C
         Jtw4CASM4vq5zBm7ktgHEMH/kZ6LmoDNEPN1N2J9KPsOLKQatOZRdLru8a5zv47xw9OF
         eFYJHcnl6gmvqV37sQ17rj6W1eeUfn/mjFGTS0rMbowwkvLt1G/maBeFgw8ivYic7Gr0
         WD2qjg4ycMfxBTQ7h4WCtsepwNhQvaNjFVuQmU1vRzesuLvdvdtQFqQrjTvYLRrRpawy
         yMOq4dmF3SwsOSZXeU1fIlW/+HMoKgd/xJKzSLVKjMBQDVe1iNcq5Mc+6fMhBQgEcUvm
         Ijig==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=zi8PHhdvpne4bYNS1kG3M6aafhSp+JYf7NO785wuugU=;
        b=p3h1WmYB5Yo16l1TYDwLIMbD10/3i4grNj/jU0dp0Q7Mb01UzuwJdvRhBRgaR5LZ0A
         G+l09wORUbEQ8VZeWj3os/PO62yUqsn5drnPIJ/SNHxp9biYGTq424XN8XM9jzrO1Jkn
         2nfVYaMghfrhN9KrVbBOOKRYWXTgy2Llo9299UCgSqDcdqRHDGt8VYrHlczRD+M1aWht
         BwdB4/mXFqfKAnGi808TEwhzFy5Xju115KWMUe1IneO2Xf7Fgk8k+kdpN+OxcTUKSzq4
         tD8vM5XiAnD5KpZqdEEJjV21Ivv2nDnM3+QFsIpLYutalxdN0o7fgdnHTiy1R77CFwU1
         qCRw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=H9j5RYoL;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=WTrDQriU;
       spf=pass (google.com: domain of 01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@amazonses.com
Return-Path: <01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id l22si6317633qkk.27.2020.11.23.09.02.42
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Mon, 23 Nov 2020 09:02:42 -0800 (PST)
Received-SPF: pass (google.com: domain of 01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=H9j5RYoL;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=WTrDQriU;
       spf=pass (google.com: domain of 01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1606150962;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=3P2xO9leJ1ANAwK2LeXqCupAXpWcMbNL+Pfsh60LWzA=;
	b=H9j5RYoLScu0a5RcYD0NkM/0gqFi/tclXM0IyFbEJPhf0Fgh3h2rsQ2HWvlzEXf6
	fpWibcwJxFZWz/kW/e2pmZ/bouCvfVzgevLZZT0o7WY7PQR/R+zjneG/9WPvG+QIrrr
	6Mc3OigDcwEGB6PODFUL/uFRw8LtnyTjdIlIwv3M=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1606150962;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=3P2xO9leJ1ANAwK2LeXqCupAXpWcMbNL+Pfsh60LWzA=;
	b=WTrDQriUDmDhco+ezL5oeCTdIuDv8JjQp83XYleyWmR1gNK5ijkmGyb3KhiXFDYL
	iCDkQcwzTFAx0kmR1E86COPUOKkouknjDP2J23PHwNpw0MN+UYbwTySz2HSz/+aakrt
	QsiiH8t/SbSOgh3BM4/AbLf114Scw0Iaa9IMWZPc=
Content-Type: multipart/alternative;
 boundary="--_NmP-4868992462a93a8c-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #273 [Easy] 
Message-ID: <01000175f60ebbf9-8476dcd7-2051-4580-be39-3c74feed4d21-000000@email.amazonses.com>
Date: Mon, 23 Nov 2020 17:02:42 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.11.23-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-4868992462a93a8c-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A fixed point in an array is an element =
whose value is equal to its index. Given
a sorted array of distinct =
elements, return a fixed point, if one exists.
Otherwise, return False.=20

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8],=
 you
should return False.


-----------------------------------------------=
---------------------------------

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%4=
0gmail.com]=20
and get in-depth solutions to every problem, including this =
one.=20

If you liked this problem, feel free to forward it along so they =
can subscribe
here [https://www.dailycodingproblem.com/]! As always, shoot =
us an email if
there's anything we can help with!


---------------------------------------------------------------------------=
-----

Master algorithms together on Binary Search [https://binarysearch.=
io/?ref=3Ddcp].
Create a room, invite your friends, and race to finish the =
problem!


----------------------------------------------------------------=
----------------

No more? Snooze or unsubscribe
[https://dailycodingproble=
m.com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b=
8f89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-4868992462a93a8c-Part_1
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
    <title>Daily Coding Problem: Problem #273 [Easy]
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
Apple.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">A fixed point in an array =
is an element whose value is equal to its index. Given a sorted array of =
distinct elements, return a fixed point, if one exists. Otherwise, return =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">False</code>. </p>
<p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">For example, given <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">[-6, 0, 2, =
40]</code>, you should return <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">2</code>. Given =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">[1, 5, 7, 8]</code>, you should return <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">False</code>.</p>
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
----_NmP-4868992462a93a8c-Part_1--