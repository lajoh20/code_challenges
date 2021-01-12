Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1385:0:0:0:0 with SMTP id f5csp2158423ejc;
        Sun, 12 Jul 2020 08:45:34 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyjTVBJ8aVykYmtIa15eMQLX1/LdOh71oVxKLBwz+c9nR3J0z79QLErByPseLqQet/+iX3t
X-Received: by 2002:a0c:bd88:: with SMTP id n8mr78341849qvg.194.1594568734803;
        Sun, 12 Jul 2020 08:45:34 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1594568734; cv=none;
        d=google.com; s=arc-20160816;
        b=q7UBE8mBFegiO1cRaZW7pPtiY0sQvyvmtK/GkNKWCHxu86UaMLS5b+QkqoK0xcqtIQ
         j+B5A2Hwddd1n5j9Nt0WOFgXW0t4+RxlbxRqLFvGVh8eOl5g+NCf+Sq34BzeZyU5Om1P
         CYyoyj9MlEkNBlZhsDdrwtbnBr6QG48j6emPX0Ss6oruAg8zW1kNpfExsTjXetCs8V6k
         Tm03g2AjRyVxiU9YojCCg01Wt82dNiHK2jKqXz7lPUppAv7W8iTYwyXZC1npykWPyn3J
         Itndh7MttjS0fRivHkM1QmpKyyNuTegCTn07Tt1WLrmI1Q+XHRnIOV3iSyWjDRhtbQ14
         sQmg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=Ga/7cfhAQxqOih0moH48pdP3ahlk7+XBaufR/wouyLc=;
        b=d6M8IywIDHzN4W0DwsGfVGK0cAelbq7YKmnCzhKYMeV0K9AfGjrjaICUoxFQLUTpsr
         6O/2VTIrII1ez+hxgP/HYEUINGQnQoOMHEuKlLXyxi+Lz6anL+zGPJrAhONzwJXEFaK5
         73rONnsSB2bZ8F5xk5meWALfaOGZrmA8bRMv0SHPDSV9eYKuetob4dM3oPrgdTTWtd3J
         ukX8zRocCpcLaYoBDTWhjLvk37nw75FCtoCMn3wKmuSgo4gMxjSAP2ig/1EGN4dFBtNI
         ICjN08XXTMgcI6nd6JQC0jrbm2KEuvoyNxw5Tygz4orNQTS3SVQfQWC7I+tHBdqt2S0C
         obDg==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=fap4spFw;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=fXkpdlOv;
       spf=pass (google.com: domain of 0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@amazonses.com
Return-Path: <0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id j3si8862606qko.181.2020.07.12.08.45.34
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Sun, 12 Jul 2020 08:45:34 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=fap4spFw;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=fXkpdlOv;
       spf=pass (google.com: domain of 0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1594568733;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=yjSAOVD86yvPpTmTWwf9J0GoTuBhlV+zubC4RhpALbY=;
	b=fap4spFw4GjBrSgYT24Fo9SudB0JtXDhnKlcQUtuXJevbG17H9wcVdO30Pc1JUbS
	+O0YUOeMVwru5zCYp8tgT9YzY1Khx6NODcfUzfsq2EaEPA74Ar0gPGD/BDkJwk/W7W9
	oxtINPR+e2DFWWsSm6etC6qQpHL9JTTsraPTeyls=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1594568733;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=yjSAOVD86yvPpTmTWwf9J0GoTuBhlV+zubC4RhpALbY=;
	b=fXkpdlOvBQ9+2okicXcrHMB3t2zF5Qu3J2dmLHcDkEJzsekJAumuespPUbb3sCJv
	hWE8z2g5tL+U+yT+m5v+ZE8os6KTubispTfh4fepGA8izyu4lvEieGZcRiRqgCYN2Nl
	9osgh9Ng3iLBnTWXzUYiv0j8UfeH+EdVCunKVF4U=
Content-Type: multipart/alternative;
 boundary="--_NmP-fa8aaa247bf07843-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #140 [Medium] 
Message-ID: <0100017343b3f4a9-c2079a55-3c4a-4ed0-9708-faec2f0c88e3-000000@email.amazonses.com>
Date: Sun, 12 Jul 2020 15:45:33 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.07.12-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-fa8aaa247bf07843-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of integers in which =
two elements appear exactly once and all
other elements appear exactly =
twice, find the two elements that appear only
once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. =
The
order does not matter.

Follow-up: Can you do this in linear time and =
constant space?


---------------------------------------------------------=
-----------------------

Upgrade to premium
[https://www.dailycodingproblem=
.com/subscribe?email=3Dlewisjohnson1066334%40gmail.com]=20
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
----_NmP-fa8aaa247bf07843-Part_1
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
    <title>Daily Coding Problem: Problem #140 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">Given an array of integers=
 in which two elements appear exactly once and all other elements appear =
exactly twice,
find the two elements that appear only once.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given the array <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">[2, 4, 6, 8, 10, 2, 6, 10]</code>, return <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">4</code> and <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">8</code>. The =
order does not matter.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Follow-up: Can you do this in linear time and constant space?=
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
----_NmP-fa8aaa247bf07843-Part_1--
