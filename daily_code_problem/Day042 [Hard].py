Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1ed5:0:0:0:0 with SMTP id m21csp2617243ejj;
        Sun, 5 Apr 2020 08:37:45 -0700 (PDT)
X-Google-Smtp-Source: APiQypK6jB9ISv47UYEMYCU4UwvbJJUVksv6sSNwLYqFnNvrotkwKk4YGrUxrWhgKFdy40GtGLjR
X-Received: by 2002:a37:383:: with SMTP id 125mr8678987qkd.192.1586101065494;
        Sun, 05 Apr 2020 08:37:45 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1586101065; cv=none;
        d=google.com; s=arc-20160816;
        b=ujZlb+ohOmz5MPfOVz6jIh3wzvTyAMdFre6fJohhe1LqqXPKM/G8KdUtXhZyfNh1+n
         Dz6DrfDtbJWYYqp8rNqxwHK5FHdN5EOL6GDpx9TBOud97H9Csl/R1fY6FMgoCzR8Slqp
         /cnvkR89ejgp59mOFQZvOsu/CluGidyekvI0SFAAexiCSilbksFRXVcbwlHy5mVEQTjB
         gisQPhagfad2CIsUQZmMNcOhhi9iUE0lSgiZFyR1MTyIt0/qEGnzg0UCoM/FZ6njGX13
         KD7WsyyRFHeIlGddcdhhoFfQzg2aWp7Etk+6DRbIpgjT6DhGLt2le0Kdh4HIpirBR8WK
         kHYg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=Ep5GWSO6w9XRlRlP3lXLK6w0cM0F/38jgYv8Tj+IMR4=;
        b=PMSU6xxCdDeagGGi0toA8uoOjE5BmUdnshXWJTtJAx1p3wHK58kJ5o6N9AHaErXxqD
         O+GxCIeNXXsVWO1sjbOxwh5R57rXcTGO2yLp7o1Bg+dcbVoUpZleHomQSJG9oFMkb8uN
         6J7nzuwp+NE0rrj0pAG7DIkzP0r1YmtNRDnzWu906aQrklsMQUypw0glT6ilHZaYAQG3
         yuFhs2sxc1vypMDhxFlZ5lvMYKHkg7Vm3jlWuldfyQnW2QnAUYWBjxIbuHnDKEorjqmW
         iCqITR4l57OwaspsS8SjLx7WpL9cl1RC4MI49ddFHn3RqfDhAp22mwofpOuzPKPoh9Nz
         nBGA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=FBtskQcP;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LDVhWcOJ;
       spf=pass (google.com: domain of 010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@amazonses.com
Return-Path: <010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id q75si8463228qvq.150.2020.04.05.08.37.45
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-SHA bits=128/128);
        Sun, 05 Apr 2020 08:37:45 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=FBtskQcP;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LDVhWcOJ;
       spf=pass (google.com: domain of 010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1586101065;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=lkouc82968ESqMSROK4SuVoe1Okb8yap6imj6IVQKEY=;
	b=FBtskQcPNh4w64Eo0MgKHmOJ6aAKdMvGplnDYfMlGFFD0CrCL4wcFIx81E6C1JUa
	yoO3xHirX2PU1M7RSqlIUYUv2K+IjepreeEWScbvp+xC00y9xaC4m08AJpi1gTc+1g/
	vekMFhC5XtdPDfvhcsdh4KKIWuJbbF93PAroHzOc=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1586101065;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=lkouc82968ESqMSROK4SuVoe1Okb8yap6imj6IVQKEY=;
	b=LDVhWcOJvScIXFymMWmcFJKJ1LrZRwQ3JS9XH+Ity4JblYi8RbXmNwoSp/TeW1Lx
	AyQ3T1NJuNeXWhqdnBYZs6ne3ndrjbES6dheMJNp3fq52rFNh45dYDU0VqFMPJZHxtn
	uuRd3/2teRE8dFcVEaTH6M4S1unh+KSOCic4ilfs=
Content-Type: multipart/alternative;
 boundary="--_NmP-aeb6a1b3ea7e6200-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #42 [Hard] 
Message-ID: <010001714afd9501-0cdc53d2-6db0-487d-9b2d-a7e700a2642b-000000@email.amazonses.com>
Date: Sun, 5 Apr 2020 15:37:44 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.04.05-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-aeb6a1b3ea7e6200-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a list of integers S and a target =
number k, write a function that returns
a subset of S that adds up to k. If=
 such a subset cannot be made, then return
null.

Integers can appear more =
than once in the list. You may assume all numbers in
the list are positive.

For example, given S =3D [12, 1, 61, 5, 9, 2] and k =3D 24, return [12, 9,=
 2, 1]
since it sums up to 24.


------------------------------------------=
--------------------------------------

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
----_NmP-aeb6a1b3ea7e6200-Part_1
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
    <title>Daily Coding Problem: Problem #42 [Hard]
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
 Helvetica, sans-serif; box-sizing: border-box;">Given a list of integers S=
 and a target number k, write a function that returns a subset of S that =
adds up to k.
If such a subset cannot be made, then return null.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Integers can appear more than once in =
the list. You may assume all numbers in the list are positive.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given S =3D [12, 1, 61, 5=
, 9, 2] and k =3D 24, return [12, 9, 2, 1] since it sums up to 24.</p>
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
----_NmP-aeb6a1b3ea7e6200-Part_1--
