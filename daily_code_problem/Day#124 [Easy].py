Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1385:0:0:0:0 with SMTP id f5csp670282ejc;
        Fri, 26 Jun 2020 08:42:41 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJzW2RI6Y9ChJG/RuKpaY2bHTVdULSVsjknZnaoKlMNEuy0dnfRlinK98O8FX+fwL3baUBe7
X-Received: by 2002:ac8:479a:: with SMTP id k26mr3564166qtq.264.1593186161646;
        Fri, 26 Jun 2020 08:42:41 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1593186161; cv=none;
        d=google.com; s=arc-20160816;
        b=cAEqHIrQgk62zEMyaWeOqOHZ8wvOOu8HS+L9e4Xuz7RQX8QL6Wc3AEBIwj+7y8Vanv
         dDHT1iCbJZthgOYXv4e5RjKRoKMQLu5Z+WcdZCF/r5ex8YsVaLK1l/JipkI03AGkhJFT
         nRmg6xfUgEwd/vyjf2Mfc9f14uCUNd7FCCTy7606M4SEI53hrQiH8pCg1E/rB+Cx6iGF
         QIg0DrlmutvhXqrybxCaAynNRMp7QmjPZfkmDjPIPvuyEzRgHdtVx/EDoDqjffuj/d0e
         gDajqQ2qWr6puebxo/u/dqoF7tqRuFAnhrYsGhhUQ/41nJS9RIfOT4ORnA02fmRXroXK
         cECg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=vGScButf4D5nyFkJOSrah2irmgHAceRr2yoGkuSDPPg=;
        b=YjHdLGCqpEbbvTo/ntEQCg02YqnucLIeKW12D1yN9YW+72m4LiOj72gWOODkhDHwAs
         P3oYpAQ2Wwwp08RxXH2eJBpyx246bFvMIMIEp93ge9cXlxtIXhFl40LIfw5ztdNBzzQa
         OBLLU3SfRsYXlP9A/eU63Qio743h1pQKMGsF5cuqF1F8a6/CB7TG93Vt5VdVMKQ+/CCY
         g1m9ttnMVQA7wOsK9iUTxCkT6cg8W2VfcUoN+t7888c6BsT5IYwxCi4dLx6suyTizBUl
         4ST2Cb3b+0XYznFAxZtMlYUV1t7LAp15xVG58hnfpHNBnYc9s4hRttkEU9QcUiOXDe3a
         JVJQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=Y3aG5CI7;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=QTqmjfTa;
       spf=pass (google.com: domain of 01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@amazonses.com
Return-Path: <01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id p7si14348325qkj.20.2020.06.26.08.42.41
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 26 Jun 2020 08:42:41 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=Y3aG5CI7;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=QTqmjfTa;
       spf=pass (google.com: domain of 01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1593186160;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=OezS/1B81VInvBJKJsk62OfGNA1YsPmi+GMayCbM6mU=;
	b=Y3aG5CI7m3fY0WgX5Gvx8SV9jOn49jczRtV2n79ZBWLU50KntB7UV43YamcAU2PS
	k0MFID6SLjUHJhxoFrZYXEAAETA2cw0IbgJ/uXYoJcQxZbDuSNNloTS0P9BaHaLaQho
	1STPYx6qS6Yw3FQaaWAKDHj8o+r8M7xRNyqiPlOU=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1593186160;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=OezS/1B81VInvBJKJsk62OfGNA1YsPmi+GMayCbM6mU=;
	b=QTqmjfTaoZvuNcF9ez8bBWx8oNcxr1ZyGMV1YVV4VGoDrYeM84U8JWI5qKVDzywY
	oIdzfwhxAKiMCBvPBfJsKOTZO7AdfC4F72ytGHmyQRl2yedMB06seCgW6yENvMYkDrW
	7V0ygQWsOPLH9CaLPMpzBclqk1f4zOtNM+OeJNl4=
Content-Type: multipart/alternative;
 boundary="--_NmP-9426d0f1ec86b7e8-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #124 [Easy] 
Message-ID: <01000172f14b90a2-6f9f6916-6375-4f6f-9116-cdc0d6968e96-000000@email.amazonses.com>
Date: Fri, 26 Jun 2020 15:42:40 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.06.26-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-9426d0f1ec86b7e8-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You have n fair coins and you flip =
them all at the same time. Any that come up
tails you set aside. The ones =
that come up heads you flip again. How many rounds
do you expect to play =
before only one coin remains?

Write a function that, given n, returns the =
number of rounds you'd expect to
play until one coin remains.


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
----_NmP-9426d0f1ec86b7e8-Part_1
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
    <title>Daily Coding Problem: Problem #124 [Easy]
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
Microsoft.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">You have <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">n</code> fair coins and you flip them all at the same =
time. Any that come up tails you set aside.
The ones that come up heads you=
 flip again. How many rounds do you expect to play before only one coin
remains?</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Write a function that, =
given <code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px;=
 white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8;=
 border-radius: 3px;">n</code>, returns the number of rounds you&#39;d =
expect to play until one coin remains.</p>
<hr style=3D"font-family: Arial,=
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
----_NmP-9426d0f1ec86b7e8-Part_1--
