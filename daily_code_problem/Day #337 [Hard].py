Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a05:6520:12b2:b029:b0:a332:2bfe with SMTP id do18csp4222171lkb;
        Tue, 26 Jan 2021 08:55:42 -0800 (PST)
X-Google-Smtp-Source: ABdhPJzwdtcb6k5+YDOszNs3jeP9sGtTNrjt12Z1Pg3a/4dfhfegLZZFRCCrPqY+kaW3u9VSDLHg
X-Received: by 2002:ad4:55ee:: with SMTP id bu14mr6396811qvb.30.1611680140669;
        Tue, 26 Jan 2021 08:55:40 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1611680140; cv=none;
        d=google.com; s=arc-20160816;
        b=PN8o61PTx3iTyNWuuEPr58gdY+2i2aeCkX/1s9NiviFEFvQHlGq42nRLhGGUHlERyv
         OCmrM2+JBnwBDK+snzXGxLmPWrn4fSiprn27Y14yTkX4rC2dXVixVLXWtefDQb7Tvn2B
         rWo5yXSMKpU1kUtyuX/ytjFnEx6FSAEG1+RIwvzGnSUq2ih5KXYXfrP2HKPSlFKesqIN
         u3X6YVBKibs3h9djThYWdT3BrBqO87mfYlPkBSnDDDPfAgTfKV5JpQIckCnH6GcyN7rd
         P7SwpCafUWxSLoJ6yRWWwniUxuWTAnYyttJj59DwnS1wjGCe1mINBcN8CdmllDNN8+sn
         qXww==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=gy4NuNJoob2qaLatWB91UvW/9UXcUEP7lqKDXLlzVtE=;
        b=H2zGoGD5+svthYGZ9ys/xF9RrVChkvxuKcmDaSl+HKTjuWAB98v07t+xJMTkIGiYjl
         TN5q2RBWFEkTEUqYFa/HiaSmWObUt+1+kF5paKEWINwqpO2+BYB45G6ex9xEZ6bt8SJK
         9kdZDpV7Ag2iY8PsAlAPpMU8AbF7pBirrHzO4PU/eypw1rDHgk1K/HVznOLr6oMWkdzK
         0kI3upZbWhjpaGuktu+1l4evHR8XouDSj2j4ddE9kmXIMh5On/kze7iQgiBTpQq2Cg/k
         bmil3Sax8RiCkoe1scJcs1W7aDX6qoTEHRtbkgvK+IKMx5V2y6HjhCNjZuIDOu7VOkmB
         29SQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=CCovWB9Q;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Hry+SOZl;
       spf=pass (google.com: domain of 010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@amazonses.com
Return-Path: <010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id v22si8072535qtb.143.2021.01.26.08.55.40
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Tue, 26 Jan 2021 08:55:40 -0800 (PST)
Received-SPF: pass (google.com: domain of 010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=CCovWB9Q;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Hry+SOZl;
       spf=pass (google.com: domain of 010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1611680140;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=4Zg8F33o3oLvmumH7aVySyEPO5qzUsv9yWQSVakKQYQ=;
	b=CCovWB9Q9M9dJfJHZPnMz5Qub0QLbURzftD5NfuYcSJ92MJacgcr/KnaAlKrM206
	sNkd1IIA9YZ1JJA0bzUxSrBBZM6tVS+0w4t9BnPVxrdhrn+NE6bSk5H//5Csoqs72Uj
	VSdCwtdyMWx7RrIs/L9j5VV34wAsEQUyJn0R25+M=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1611680140;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=4Zg8F33o3oLvmumH7aVySyEPO5qzUsv9yWQSVakKQYQ=;
	b=Hry+SOZl5vLenfrDZIua0W4SPCRFKtlueHpqcMLf/FiAr0PSOAn5bYzh2KTO06V8
	mBBUIKuOvgiOwf5ZrJgmyohMBKsd4621xrIv/QF+6Z628uRoP8fFcbUc0rVqZ3MwtEN
	L8VzAHRGj5XSxtD3mwiZNh6Ji3SYiZZF0OEghYMI=
Content-Type: multipart/alternative;
 boundary="--_NmP-25c135238c845c9c-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #337 [Hard] 
Message-ID: <010001773f9f49f0-2a74f173-b9ff-4c0f-93f2-7d0584d62cc7-000000@email.amazonses.com>
Date: Tue, 26 Jan 2021 16:55:39 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2021.01.26-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-25c135238c845c9c-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Given a linked list, uniformly shuffle =
the nodes. What if we want to prioritize
space over time?


---------------------------------------------------------------------------=
-----

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe?=
email=3Dlewisjohnson1066334%40gmail.com]=20
and get in-depth solutions to =
every problem, including this one.=20

If you liked this problem, feel free=
 to forward it along so they can subscribe
here [https://www.=
dailycodingproblem.com/]! As always, shoot us an email if
there's anything we can help with!


--------------------------------------=
------------------------------------------

Master algorithms together on =
Binary Search [https://binarysearch.io/?ref=3Ddcp].
Create a room, invite your friends, and race to finish the problem!


---------------------------------------------------------------------------=
-----

No more? Snooze or unsubscribe
[https://dailycodingproblem.=
com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b8f=
89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-25c135238c845c9c-Part_1
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
    <title>Daily Coding Problem: Problem #337 [Hard]
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
 Helvetica, sans-serif; box-sizing: border-box;">Given a linked list, =
uniformly shuffle the nodes. What if we want to prioritize space over time?=
</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><a=
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
----_NmP-25c135238c845c9c-Part_1--
