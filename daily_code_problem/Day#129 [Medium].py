Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1385:0:0:0:0 with SMTP id f5csp627207ejc;
        Wed, 1 Jul 2020 08:53:33 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJwtmp48pZ3ClCMp7ex9aZPt2xLeqF2kNv1pvWvXxkJbXEN2MbS53AjU7clR7wZDpJ++fv2X
X-Received: by 2002:ac8:1b8b:: with SMTP id z11mr14311277qtj.6.1593618813508;
        Wed, 01 Jul 2020 08:53:33 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1593618813; cv=none;
        d=google.com; s=arc-20160816;
        b=QjenQk+cAVtDikPEMtteel1bh0iNsqKVgWI14hw14y3ijvz9Wx3cZBm2UEXp06jZJx
         DlTu5iM0eaGh7b6edTDPnaSVIL9dEy3viK50ihtnfgJJM7VFn585nJhKq2iV5sOhQ8+p
         Zrjcc6SJfpSe5NmrNJRcbSs2V4B1/pfdbv/m9/YQWYGADOcNzpzeGLNzGTfj2hMelCWH
         YR/RVAd8v2UF9FkoAyuwt29z9F6bwQ4emZ+fWDPl7KxtQT1nEzdTbwHlbSDb+lmbDDOx
         D2KzQ0NjcAWeSRrbb7xyfRPjIowyXZ8qtALoZ+d7/kfS10O6pUnYBmYpc/EEOOo/gnqJ
         240g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=kLzhogqY82AL3U0vRYZyVKX5PteVq8vmiZ+5xamOLT4=;
        b=nl0hD70LmEyToy+waKJNEDMJCVWaFCb0oF6oju7M3O0j+npv8dpA38GS6157t6nqdn
         VL7Kt0Ye/KNKl6cZTOzimzNiahAVIbZyAEBp/suI93pgiJwsfOtsQInd2gxTiOj008bs
         79t7FvHmxFmDZEOd/W7v5LDLVMCBSzyrT0CbBrkZiQuTxc+GMR4Tmil6C9TPpNJ1+N2q
         88b1gZAeJoSFvC0WsD/Jlk9w1txgWL0Wg9OKfYbWnY/PqtKbwpybgYGJbK2t7IMXK37g
         8/OqBlhO1Z1nYvlEPjaRPrNBIMh+f0tBz2TsI9E3eCfD3/IlgMnBsetkfF/CFlXeqcBD
         evbA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=dh3CQbqc;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LtpMYXNR;
       spf=pass (google.com: domain of 010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@amazonses.com
Return-Path: <010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id v9si1326699qkf.255.2020.07.01.08.53.33
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Wed, 01 Jul 2020 08:53:33 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=dh3CQbqc;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LtpMYXNR;
       spf=pass (google.com: domain of 010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1593618813;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=KKQYO9ZRbzZDqWn/G/FtKbLuMGRvbf32kjZIJBrOr/E=;
	b=dh3CQbqcltSresfMd6W238mL5CnORG4PM6QdpoTxmpokhP+INOgqPifD54wJcHbL
	Qrp28ngG7iIR5r61x8anBWJqzBVSTZue++A3+ujF2fd77R6O9rGgMky/8PuKHIys22B
	rSjoTtU4xK0yYnivNSeN5Rq3RMOYKJw/Gr035E48=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1593618813;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=KKQYO9ZRbzZDqWn/G/FtKbLuMGRvbf32kjZIJBrOr/E=;
	b=LtpMYXNR/NqM3efNoMTC4gzKNCHria7kV7B1qARF3aUkfWfH0fOpHaEGFaTQqKqT
	pNM2UDIbBrZPUa+7Iflvtd0Uticit9TkN8lDkbUFLG10At0tS4HAPg+63WgQxSnHWB/
	LzG6nL5eEhhGjO/lmPJMkP5gI6VpsV74V0FAstBQ=
Content-Type: multipart/alternative;
 boundary="--_NmP-c2a098a89bb0cc9a-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #129 [Medium] 
Message-ID: <010001730b155047-084884dd-6832-490d-a406-c692eff632e3-000000@email.amazonses.com>
Date: Wed, 1 Jul 2020 15:53:33 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.07.01-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-c2a098a89bb0cc9a-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n =3D =
9,
return 3.


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
----_NmP-c2a098a89bb0cc9a-Part_1
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
    <title>Daily Coding Problem: Problem #129 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">Given a real number <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">n</code>, find the square root of n. For example, =
given <code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px;=
 white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8;=
 border-radius: 3px;">n =3D 9</code>, return <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">3</code>.=
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
----_NmP-c2a098a89bb0cc9a-Part_1--
