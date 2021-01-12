Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a05:6520:4581:b029:9e:2c6b:28d9 with SMTP id s1csp4867824lkv;
        Thu, 10 Dec 2020 09:04:35 -0800 (PST)
X-Google-Smtp-Source: ABdhPJy6h14OZY0xYVuavbcIOWoa5BKvtSeE4VWdpsYSUDn5sliiDg1A9UPaKRUHcag8BA/lS06p
X-Received: by 2002:a67:2e16:: with SMTP id u22mr4199412vsu.12.1607619873097;
        Thu, 10 Dec 2020 09:04:33 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1607619873; cv=none;
        d=google.com; s=arc-20160816;
        b=U9GBm3yjDRrGWJKoEJCT1amjSmQ53cRVni60iym9BJ7PFUWDv1oC6LrGXCb1QNsLqa
         ogtLvCUMIrB24yvmsJbEfQWowzu+Qq1RmbVoLNBZbCnvUJD8xIj+kjGu6MZ7isyJZeUd
         jIQ4QC1IyqSoHlx3cZo7mIYpF5NNJvsL7uIoeXwsZf8wV5FoilQTtEEtp03KdC6cWqGQ
         vxCrL5KTUE9q+XOUZ5nrTCnZNF3ilfnZzC0SJKfPIXv5YdGj8a5zzIc2Is04jBVwTi9x
         VMwSqUOYtJSsQIp9cErJ+NGNnD/O0PHErUcEfGnVJwMKnJ6x+BaPmi7IiYXHe29pLI5A
         XH9g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=/pqm4B3XCEgjS+fK980itoEfXBk/W4ZdsoBOkYMtTPQ=;
        b=WV1U/JBKMxC6/1VwBRf+eLAibHBgggYLgpJAk5UELqc2Fx/0AFWzvGcP0pHkZn1LlZ
         nD8EhkZXF2FTno2FxRIMgbtAwGQvtMd/yGfbaOYUXrfIydoqy9NeeJTbv8wEXlr8qhsY
         bCFALNFIRDWSz+3iLhnloWZCNt7kns2MZ4IFkTspFvaL70I2C7U9AncZCrgmbHT+FgWr
         l4y8R1P54U8ykfnbB9HJMQs9FgW87ZWc7IfWCht/2YGPhn3E1So4tiZi73JCE+77AddR
         iXVqIvC105c5pc43B3oPgQdGNzkXYqPQtVHSBz7CCWWHVL3qlmUUxmDRGMK+lsnnAlIo
         /5dg==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=XzhdTcfn;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=J51DoXkK;
       spf=pass (google.com: domain of 010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@amazonses.com
Return-Path: <010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id s141si935652vkb.85.2020.12.10.09.04.32
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 10 Dec 2020 09:04:33 -0800 (PST)
Received-SPF: pass (google.com: domain of 010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=XzhdTcfn;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=J51DoXkK;
       spf=pass (google.com: domain of 010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1607619872;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=ghFD8Y9vS0Bd/I0FJffbqUlh+DXk1ZMYCI2OAgtSe08=;
	b=XzhdTcfnQPMHQqfsXm7zTRxaPdaDXuiBVfMPZp0XszVL5+WndF/52PcF621I2NGS
	YHBxmJykJz+NL/p4aI0d1whihNwnUXJlsFMVmelGNhrps46Q/NrOiGZ6xaWhNoHGWFI
	eLe+ntIH93vlyEZM/Czzn7RG8iximElWt3MpC8j0=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1607619872;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=ghFD8Y9vS0Bd/I0FJffbqUlh+DXk1ZMYCI2OAgtSe08=;
	b=J51DoXkKmqt1ozQaphU0mPmYsVI1NU5Z0r/1j4DKrt4NEn6pb0KfD/ruGG/FAgkQ
	AlcwZQTzFFAnou1iUnZsdu8okmEDchupLPodUdeahSe1ft6TINIkPEyHbt4QSfSKS/7
	mFWpTFvC2pYuDxiiWHx1upqr5qSfOwpcUjgc6swM=
Content-Type: multipart/alternative;
 boundary="--_NmP-6a6c859ab2bd49bf-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #290 [Easy] 
Message-ID: <010001764d9c8744-7e9960ba-fde8-42a1-afd1-d86288755917-000000@email.amazonses.com>
Date: Thu, 10 Dec 2020 17:04:32 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.12.10-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-6a6c859ab2bd49bf-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

On a mysterious island there are =
creatures known as Quxes which come in three
colors: red, green, and blue. =
One power of the Qux is that if two of them are
standing next to each other=
, they can transform into a single creature of the
third color.

Given N Quxes standing in a line, determine the smallest number of them
remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to =
end up
with a single Qux through the following steps:

        Arrangement       |   Change
--------------------------------------=
--
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, =
G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                |=
 (B, G) -> R
['R']                     |



-------------------------------=
-------------------------------------------------

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
----_NmP-6a6c859ab2bd49bf-Part_1
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
    <title>Daily Coding Problem: Problem #290 [Easy]
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
Facebook.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">On a mysterious island =
there are creatures known as Quxes which come in three colors: red, green, =
and blue. One power of the Qux is that if two of them are standing next to =
each other, they can transform into a single creature of the third color.=
</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: =
1.5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Given <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">N</code> =
Quxes standing in a line, determine the smallest number of them remaining =
after any possible sequence of such transformations.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given the input <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">[&#39;R&#39;, &#39;G&#39;, &#39;B&#39;, &#39;G&#39;, =
&#39;B&#39;]</code>, it is possible to end up with a single Qux through the=
 following steps:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px =
solid #cccccc; font-size: 13px; line-height: 19px; overflow: auto; padding:=
 6px 10px; border-radius: 3px;"><code style=3D"border-radius: 3px; =
font-family: monospace; margin: 0; padding: 0; white-space: pre; =
background: transparent; background-color: transparent; border: none;">    =
    Arrangement       |   Change
----------------------------------------
[&#39;R&#39;, &#39;G&#39;, &#39;B&#39;, &#39;G&#39;, &#39;B&#39;] | (R, G) =
-&gt; B
[&#39;B&#39;, &#39;B&#39;, &#39;G&#39;, &#39;B&#39;]      | (B, G) =
-&gt; R
[&#39;B&#39;, &#39;R&#39;, &#39;B&#39;]           | (R, B) -&gt; G
[&#39;B&#39;, &#39;G&#39;]                | (B, G) -&gt; R
[&#39;R&#39;]                     |
</code></pre><hr style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
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
----_NmP-6a6c859ab2bd49bf-Part_1--
