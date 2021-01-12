Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:76c2:0:0:0:0 with SMTP id q2csp4116518ejn;
        Sun, 26 Jul 2020 08:46:43 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyxIrUpPqbPSxn9SfCa7UFePANQLyA+16gr9bXije+hWskRVYLIQuF4QjqQdYzbIqS3Ji3y
X-Received: by 2002:a37:444c:: with SMTP id r73mr19132238qka.141.1595778403319;
        Sun, 26 Jul 2020 08:46:43 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1595778403; cv=none;
        d=google.com; s=arc-20160816;
        b=NMXKAgP3ByohM5rWD2Xb5O5Q8Xg0WNnvKcWKM5yxnVn/uIjIkMdE4WZ0fn1LyjZI9R
         HvrgLnwsicAaMqWPpbKBmUkH3MFHeXLOhhWp1sik+bb82a7snQ6lxB1+vlE1rCPpu4QR
         23mNoI7NBlr5ne2o2S3CjRJMwR48JtSXuiilbvs7FXCYzMmg9koROSFv0Wnn04XV1HCy
         oheiETSjVBcbGyYR8eZBjrq/bGwN0Db5GeKt4LJJEIZ8BhuUDK7g6sbNFSmyTtaDI4og
         8N6H+inVjNWlmAIBzOz4vLZC47gwL+/upgQj0pOxBgJMEdl8oMUpSuDWxYMMW/+CloDB
         aceg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=y9+b7w/L1laVyy8G4/9Y1VrNwBGT3HA2m8Yg99drqDI=;
        b=ac+0fzFVN+BV4STULQn3cn6LTj1pPm95BftOnetTBLMN4t+aFRQ2+DJxzkH3MOenY8
         FKT9uFyMlOZt9OEiyBR3+0hnOWgRIPm4W+e81I68Tmj/s1Rg/JY2v656kS0NPzxyHNv4
         ikdu+9ZXGiE7NMEj930qWc+JrNjeo/gik410CrzlmQif28kyX9UL3dJCRhv36bzInFcY
         z3ehHtihz7YCBXfDlM+O4n8u7ntHJ6SRPhl+idkpm70oPK4TV4kL0+KnREVln+jcU0b9
         fcNwYMvAcotdJTX8US2HQWuyySjpaMRr5k3nkrWh69OE+ubN8spT4JezQT4UpoxRQZaw
         ajjQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=NW0lXH4x;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LdLPDUf1;
       spf=pass (google.com: domain of 010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@amazonses.com
Return-Path: <010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id e2si5059312qtw.309.2020.07.26.08.46.42
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Sun, 26 Jul 2020 08:46:43 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=NW0lXH4x;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LdLPDUf1;
       spf=pass (google.com: domain of 010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1595778402;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=7DSHxeSPPdnUWoRaPBCN2G+HP6cWhy6JvT6Mx66EzlU=;
	b=NW0lXH4xM1UnFcO8fLQURVoHmkm9Ci7qEDCA1lnSTvmEsTWl7lK1zatS+nh5WzTC
	8eiILnd1w5Z14HRNSoqKux1olmiRW8oh4beuc1SUeXh71iuRfIQCvMP0jnxUQk1x2+9
	widD/Hj99Ry5T3Szv/+G70vdthFANSSxeDinJIjo=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1595778402;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=7DSHxeSPPdnUWoRaPBCN2G+HP6cWhy6JvT6Mx66EzlU=;
	b=LdLPDUf1Z/Y0mRXL6Q1RJ0OFfbcyti3v+DMROxddvsZEQFPFf/aajDv/HyezXh8g
	REttF2E6j5vCsgC9puJFD1j3KnkvBacIxkYKxha+8XLOdvCqFMngb2CDCkKOukDpPlP
	IkkHHsQOkxuaTM1NfyJnnW4z3j7yQw9k7GxFoz/o=
Content-Type: multipart/alternative;
 boundary="--_NmP-5e8b2d5e51b9db91-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #154 [Easy] 
Message-ID: <010001738bce05fc-eaac8cb9-8b13-4147-88e7-60d7dc6a8a54-000000@email.amazonses.com>
Date: Sun, 26 Jul 2020 15:46:41 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.07.26-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-5e8b2d5e51b9db91-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack API using only a heap.=
 A stack implements the following
methods:

 * push(item), which adds an =
element to the stack
 * pop(), which removes and returns the most recently =
added element (or throws
   an error if there is nothing on the stack)

Recall that a heap has the following operations:

 * push(item), which adds=
 a new key to the heap
 * pop(), which removes and returns the max value of=
 the heap


---------------------------------------------------------------=
-----------------

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
----_NmP-5e8b2d5e51b9db91-Part_1
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
    <title>Daily Coding Problem: Problem #154 [Easy]
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
Amazon.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Implement a stack API =
using only a heap. A stack implements the following methods:</p>
<ul style=3D"text-align: left; color: #555; font-size: 16px; line-height: 1=
.5em; padding-left: 24px; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">push(item)</code>, which adds an element to the =
stack</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;"><code style=3D"font-family: monospace;=
 margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">pop()</code>, =
which removes and returns the most recently added element (or throws an =
error if there is nothing on the stack)</li>
</ul>
<p style=3D"margin-top: =
0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Recall that a heap has the following operations:</p>
<ul style=3D"text-align: left; color: #555; font-size: 16px; line-height: 1=
.5em; padding-left: 24px; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">push(item)</code>, which adds a new key to the =
heap</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;"><code style=3D"font-family: monospace;=
 margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">pop()</code>, =
which removes and returns the max value of the heap</li>
</ul>
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
----_NmP-5e8b2d5e51b9db91-Part_1--
